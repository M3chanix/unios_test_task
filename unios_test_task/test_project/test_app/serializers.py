from rest_framework import serializers
from test_app.models import State

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['Id', 'Title', 'Code', 'Time']

    def create(self, validated_data):
        return State.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.Title = validated_data.get('title', instance.title)
        instance.Code = validated_data.get('code', instance.code)
        instance.save()
        return instance

