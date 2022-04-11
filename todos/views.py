from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer


# Create your views here.

@api_view(['GET', 'POST'])
def get_post_todos(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response({'error': 'data is not valid'}, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def upd_dlt_todos(request, primary_key):
    if request.method == 'GET':
        try:
            task = Task.objects.get(id=primary_key)
            serializer = TaskSerializer(task, many=False)
            return Response(serializer.data)
        except Exception as exc:
            resp = {'error':str(exc)}
            if isinstance(exc, Task.DoesNotExist):
                resp['status'] = 404
            else:
                resp['status'] = 400
            return Response(resp, status=resp['status'])
    elif request.method == 'PUT':
        task = Task.objects.get(id=primary_key)
        serializer = TaskSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        return Response({'error': 'data is not valid'}, status=400)

    elif request.method == 'DELETE':
        try:    
            instance = Task.objects.get(id=primary_key)
            instance.delete()
            return Response({'message': 'Todo deleted successfully','status':True}, status=200)
        except Exception as exc:
            return Response(exc)

    