from django.urls import path

from . import views

urlpatterns = [
    path('', views.my_resumes, name='my-resumes'),
    path('edit-profile/', views.edit_profile, name='edit-profile'),
    path('delete/<int:pk>/', views.delete_resume, name='delete-resume'),
    path('create/resume/', views.ResumeWizard.as_view(views.FORMS), name='create-resume'),
    path('edit/resume/<int:pk>/', views.ResumeWizard.as_view(views.FORMS), name='edit-resume'),
    path('view/resume/<int:pk>/', views.view_resume, name='view-resume'),
]
