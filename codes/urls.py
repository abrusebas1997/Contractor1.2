from django.urls import path, include
from codes.views import CodesListView, CodesDetailView, CodesCreateView


urlpatterns = [
    path('', CodesListView.as_view(), name='codes-list-Code'),
    path('new_code/', CodesCreateView.as_view(), name='wiki-create-Code'),
    path('<str:slug>/', CodesDetailView.as_view(), name='wiki-details-Code'),

]
