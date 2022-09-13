from django.urls import path
from . import views as p_views

urlpatterns =[
    path('create-email/',p_views.PostEmails.as_view(),name='create-email'),
    path('list-emails/',p_views.ListEmails.as_view(),name='list-emails'),
    ]