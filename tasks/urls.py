from django.urls import path
from .views import UserRegisterView,TaskCreateView,TaskListView,TaskDetailView,TaskUpdateView,TaskDeleteView
urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/",TaskDeleteView.as_view(),name="task-delete"),
    
]

