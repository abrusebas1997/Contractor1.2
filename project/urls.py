from django.urls import path, include
from project.views import CodeListView, CodeDetailView, CodeCreateView, CodeUpdateView, CodeDeleteView, Home


urlpatterns = [
    path('', Home.as_view(), name='home-page'),
    path('list_of_codes/', CodeListView.as_view(), name='code-list-project'),
    path('new_project/', CodeCreateView.as_view(), name='code-create-project'),
    path('<str:slug>/', CodeDetailView.as_view(), name='code-details-project'),
    path('edit/<int:pk>/', CodeUpdateView.as_view(), name='code-update-project'),
    path('delete/<int:pk>', CodeDeleteView.as_view(), name='code-delete-project'),

]
