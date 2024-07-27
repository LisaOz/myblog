from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # post views
    # path('', views.post_list, name='post_list'),  # this view is mapped to the post_list view
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', # this view is mapped to the post_detail view
    views.post_detail, 
    name='post_detail'),
path('<int:post_id>/share/', views.post_share, name='post_share'),
path('<int:post_id>/comment/', views.post_comment, name='post_comment'), # URL for comment submission
]

