from django.urls import path
from . import views

urlpatterns = [
    path ('', views.tests_home, name='tests_home'),
    path ('create_test', views.create_test, name = 'create_test'),
    path ('<int:pk>', views.ShowTest.as_view(), name='test-name')
]