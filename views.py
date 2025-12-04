from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .task_analyzer.serializers import TaskInputSerializer
from .task_analyzer.scoring import score_tasks

class AnalyzeTasks(APIView):
    def post(self, request):
        data = request.data
        if not isinstance(data, list):
            return Response({"error":"send a list of tasks"}, status=status.HTTP_400_BAD_REQUEST)
        ser = TaskInputSerializer(data=data, many=True)
        if not ser.is_valid():
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
        tasks = ser.validated_data
        for i,t in enumerate(tasks):
            if 'id' not in t:
                t['id'] = str(i+1)
        strategy = request.query_params.get('strategy', 'smart')
        scored = score_tasks(tasks, strategy=strategy)
        return Response(scored)

class SuggestTasks(APIView):
    def post(self, request):
        
        data = request.data
        ser = TaskInputSerializer(data=data, many=True)
        if not ser.is_valid():
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
        tasks = ser.validated_data
        scored = score_tasks(tasks, strategy=request.query_params.get('strategy','smart'))
        top3 = scored[:3]
        return Response(top3)
