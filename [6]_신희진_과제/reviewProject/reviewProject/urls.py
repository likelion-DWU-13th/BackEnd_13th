from django.contrib import admin
from django.urls import path, include
from reviews import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path ("", views.home, name = "home"),
    path("posts/", include("reviewPosts.urls")),

    path('create/', views.create, name='create'),
]
