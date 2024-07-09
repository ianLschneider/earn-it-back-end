
from rest_framework.decorators import action
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from rest_framework import status

from .models import Earner, Task, Reward
from .serializers import EarnerSerializer, TaskSerializer, RewardSerializer


class EarnerViewSet(viewsets.ModelViewSet):
    queryset = Earner.objects.all()
    serializer_class = EarnerSerializer
    permissions_class = [permissions.AllowAny]


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permissions_class = [permissions.AllowAny]

class EarnerTasks(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        """
        Gets tasks belonging to a specific earner.
        """
        return super().get_queryset().filter(
            earner_id=self.kwargs['pk']
        )


class RewardViewSet(viewsets.ModelViewSet):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer
    permissions_class = [permissions.AllowAny]

class EarnerRewards(generics.ListAPIView):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer

    def get_queryset(self):
        """
        Gets rewards rewarded to a specific earner.
        """
        return super().get_queryset().filter(
            earner=self.kwargs['pk']
        )

    # def get_queryset(self):
    #     """
    #     Optionally restricts the returned purchases to a given user,
    #     by filtering against a `username` query parameter in the URL.
    #     """
    #     queryset = Earner.objects.all()
    #     name = self.request.query_params.get('name')
    #     age = self.request.query_params.get('age')
    #     if name and age is not None:
    #         queryset = queryset.filter(name=name, age=age)
    #     return queryset