from django.urls import path
from .views import AnalyzeTasks, SuggestTasks

urlpatterns = [
    path('analyze/', AnalyzeTasks.as_view(), name='analyze'),
    path('suggest/', SuggestTasks.as_view(), name='suggest'),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tasks/', include('tasks.urls')),
]

