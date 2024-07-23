from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # post views
    path('', views.post_list, name='post_list'),  # this view is mapped to the post_list view
    path('<int:id>/', views.post_detail, name='post_detail'),  # this view is mapped to the post_detail view
]

