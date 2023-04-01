from django.urls import path
from . import views

urlpatterns = [
    path ('', views.index, name='home'),
    path ('addtest', views.addtest, name='addtest'),
    # path ('create', views.create, name = 'create')
]