from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)

    def create(self, validated_data):
        tasklist = Task(**validated_data)
        tasklist.save()
        return tasklist

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class TaskSerializer2(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    class Meta:
        model=Task
        fields = ('id', 'name')

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    created_at = serializers.DateTimeField(required=True)
    due_on = serializers.DateTimeField(required=True)
    status = serializers.CharField(required=True)
    tasklist = TaskSerializer2()