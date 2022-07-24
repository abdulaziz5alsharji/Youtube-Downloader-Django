from django.urls import path
from . import views

app_name = "youtube_downloader"

urlpatterns = [
    path('', views.download, name="download")
]