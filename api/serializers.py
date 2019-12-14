from rest_framework.serializers import ModelSerializer

from project.models import Code

class CodeSerializer(ModelSerializer):
    class Meta:
        model = Code
        fields = '__all__'
