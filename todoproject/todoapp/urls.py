from .import views
from django.urls import path

urlpatterns = [
    path('',views.add, name='add'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbvhome/', views.TaskListView.as_view(), name='cbvhome'),
    path('details/<int:pk>/', views.TaskDetailView.as_view(), name='details'),
    path('edit/<int:pk>/', views.TaskUpdateView.as_view(), name='edit'),
    path('cbvdelete/<int:pk>/', views.TaskDeleteView.as_view(), name='cbvdelete'),
]
