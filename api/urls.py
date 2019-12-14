from django.urls import path

from api.views import CodeList, CodeDetail

urlpatterns = [
    path('code/', CodeList.as_view(), name='code_list'),
    path('code/<int:pk>', CodeDetail.as_view(), name='code_detail')
]
