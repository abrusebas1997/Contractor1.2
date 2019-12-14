from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from project.models import Code
from api.serializers import CodeSerializer


class CodeList(APIView):
    def get(self, request):
        codes = Code.objects.all()[:20]
        data = CodeSerializer(codes, many=True).data
        return Response(data)

class CodeDetail(APIView):
    def get(self, request, pk):
        code = get_object_or_404(Code, pk=pk)
        data = CodeSerializer(code).data
        return Response(data)
