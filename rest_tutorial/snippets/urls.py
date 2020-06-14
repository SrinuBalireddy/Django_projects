from django.urls import path
from . import views

urlpatterns = [
    path('snippets/', views.snippet_list, name = 'Snippet-list'),
    path('snippets/<int:pk>/', views.snippet_detail, name= 'Snippet-detail')
]
