from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # post views
    path('', views.post_list, name='post_list'),  # this view is mapped to the post_list view
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', # this view is mapped to the post_detail view
    views.post_detail, 
    name='post_detail'
    ),  
]

