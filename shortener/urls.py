from django.urls import path

from .views import (
    ShortenedUrlsView,
    ShortenedUrlDetailView,
    redirect_to_site_view,
    ShortenerCreateView)


app_name = 'shortener'
urlpatterns = [ 
    path('', ShortenedUrlsView.as_view(), name='list'),
    path('<short_code>/', redirect_to_site_view),
    path('new/url/', ShortenerCreateView.as_view(), name='create')
]