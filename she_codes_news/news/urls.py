from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(), name="addNewsStory"),
    path('<int:pk>/update/', views.UpdateStoryView.as_view(), name='updateStory'),
    path('<int:pk>/delete/', views.DeleteStoryView.as_view(), name='deleteStory'),
    path('author/<int:pk>', views.AuthorView.as_view(), name='author'),
]