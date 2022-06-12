from django.urls import path
from .views import HomeView, ThankYouView, ContactFormView, TeacherCrateView, TeacherListView, TeacherDetailView

app_name = 'classroom'

urlpatterns=[
    path('',HomeView.as_view(), name='home'), # path expects a function!
    path('thank_you/',ThankYouView.as_view(), name='thank_you'),
    path('contact/',ContactFormView.as_view(), name='contact'),
    path('crate_teacher',TeacherCrateView.as_view(),name='create_teacher'),
    path('list_teacher', TeacherListView.as_view(), name='list_teacher'),
    #domain.com/classroom/detail_teacher/1/
    path('detail_teacher/<int:pk>',TeacherDetailView.as_view(), name='detail_teacher')
]