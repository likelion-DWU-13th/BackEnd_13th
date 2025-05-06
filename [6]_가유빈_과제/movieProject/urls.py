"""
URL configuration for movieProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), #메인페이지
    path('movies/', include('movies.urls')), #영화북마크페이지
    path('reviews/', include('reviews.urls')), #영화후기페이지
    path('accounts/', include('accounts.urls', namespace='accounts')), #회원가입,로그인
    path('authaccounts/', include('allauth.urls')), #소셜 로그인
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
