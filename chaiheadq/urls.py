from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib.auth.urls import views as auth_views

from tweet import views as tweet_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', tweet_views.register, name='register'),
    path('tweet/', include('tweet.urls')),
    path('', RedirectView.as_view(url='/tweet/', permanent=False)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)