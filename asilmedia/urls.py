from django.urls import path
from asilmedia.views import home, videoPage
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('video/', videoPage, name='video_page'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
