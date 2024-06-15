from django.urls import path

from . import views

app_name = 'todoapps'

urlpatterns = [
    path('', views.index, name='index'),
    path('update_task/<int:topic_id>', views.update_task, name='update_task'),
    path('delete_task/<int:topic_id>', views.delete_task, name='delete_task'),
    path('complete_task/<int:topic_id>', views.complete_task, name='complete_task'),
]
