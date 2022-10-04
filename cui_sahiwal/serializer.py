from rest_framework import serializers
from cui_sahiwal import models

class LectureSerializer(serializers.Serializer):
    class Meta:
        model = models.Lecutues
        fields =['key']