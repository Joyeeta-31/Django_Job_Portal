from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.post_job, name='post_job'),
    path('my-jobs/', views.my_jobs, name='my_jobs'),
    path('applicants/<int:job_id>/', views.applicants_list, name='applicants_list'),
    
    path('list/', views.job_list, name='job_list'),
    path('job/<int:job_id>/', views.job_detail, name='job_detail'),
    path('my-applications/', views.my_applications, name='my_applications'),
    path('job/<int:job_id>/delete/', views.delete_job, name='delete_job'),
]
