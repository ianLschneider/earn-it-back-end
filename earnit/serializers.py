from .models import Earner, Task, Reward
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class EarnerSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Earner
		fields = ['id', 'name', 'age', 'points', 'createdOnDate', 'modifiedOnDate']
		
class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = ['id', 'earner', 'task', 'completed', 'points', 'iconType','completeByDate', 'createdOnDate', 'modifiedOnDate']
		
class RewardSerializer(serializers.ModelSerializer):
	class Meta:
		model = Reward
		#'earner',
		fields = ['id', 'name', 'points', 'iconType', 'createdOnDate', 'modifiedOnDate']