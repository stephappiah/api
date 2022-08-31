from django.urls import path
from .views import BlogAPI


urlpatterns = [
    path('blog/', BlogAPI.as_view()),
]