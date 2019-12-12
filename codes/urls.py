from django.urls import path, include
from codes.views import CodesListView, CodesDetailView, CodesCreateView, CodesUpdateView, CodesDeleteView


urlpatterns = [
    path('', CodesListView.as_view(), name='codes-list-Code'),
    path('edit/<int:pk>/', CodesUpdateView.as_view(), name='codes-update-Code'),
    path('new_code/', CodesCreateView.as_view(), name='codes-create-Code'),
    path('<str:slug>/', CodesDetailView.as_view(), name='codes-details-Code'),
    path('delete/<int:pk>', CodesDeleteView.as_view(), name='codes-delete-Code'),

]
