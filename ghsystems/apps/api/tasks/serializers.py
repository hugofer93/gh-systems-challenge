from rest_framework.serializers import CharField, ChoiceField, Serializer, UUIDField

from ghsystems.apps.tasks.models import Tasks as TasksModel


class TasksSerializer(Serializer):
    id = UUIDField(read_only=True)
    title = CharField(max_length=30, required=True)
    description = CharField(max_length=80, required=False)
    status = ChoiceField(
        default=TasksModel.PENDING,
        choices=TasksModel.STATUS_CHOICES)

    def create(self, validated_data):
        return TasksModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        raise NotImplementedError


class TaskDetailSerializer(Serializer):
    id = UUIDField(read_only=True)
    title = CharField(max_length=30, required=False)
    description = CharField(max_length=80, required=False)
    status = ChoiceField(choices=TasksModel.STATUS_CHOICES, required=False)

    def create(self, validated_data):
        raise NotImplementedError

    def update(self, instance, validated_data):
        if instance.title != validated_data.get('title', instance.title) \
                or instance.description != validated_data.get(
                    'description', instance.description) \
                or instance.status != validated_data.get(
                    'status', instance.status):
            instance.title = validated_data.get('title')
            instance.description = validated_data.get('description')
            instance.status = validated_data.get('status')
            instance.save()
        return instance
