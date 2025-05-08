from django.contrib import admin
from django.urls import path, include
from reviews import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path ("", views.home, name = "home"),
    path("posts/", include("reviewPosts.urls")),
    path("products/", include("products.urls")),

    path('create/', views.create, name='create'),

    path('accounts/',include('accounts.urls', namespace='accounts')),

    path('authaccounts/', include('allauth.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)