from django.urls import path
from add_tags.views import add_tags, retrive_tags


urlpatterns = [
    path('', retrive_tags ),
    path('add_tags/', add_tags )
]
