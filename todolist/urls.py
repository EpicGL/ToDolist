from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('additem',views.additem, name='additem'),
    path('edit/<str:pk>',views.edit, name='edit'),

    path('crossoff/<str:pk>',views.crossoff, name='crossoff'),
    path('uncrossoff/<str:pk>',views.uncrossoff, name='uncrossoff'),

    path('delete/<str:pk>',views.delete, name='delete'),

]
