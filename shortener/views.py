from django.http import (
    HttpResponseRedirect, 
    HttpRequest)
from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView,
    CreateAPIView,
)
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.request import Request
from shortener.models import Shortener

from .serializers import ShortenerSerializer, ShortenedUrlSerializer

from .utils import update_site_visits
from urllib.parse import urlparse


# Create your views here.
class ShortenedUrlsView(ListAPIView):
    serializer_class = ShortenerSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    
    def get_queryset(self):
        user = self.request.user
        qs  = Shortener.objects.filter(author=user)
        return qs
    

class ShortenedUrlDetailView(RetrieveAPIView):
    """
    Endpoint for viewing shortcode stats
    - last_visited : when the view was last accessed
    - visit_count
    """
    serializer_class = ShortenedUrlSerializer
    lookup_fields = ['short_code']
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_object(self):
        short_code = self.kwargs.get('short_code')
        site_obj = get_object_or_404(Shortener, short_code=short_code)
        return site_obj


class ShortenerCreateView(CreateAPIView):
    """
    Class for shortening  provided url

    """
    serializer_class = ShortenerSerializer
    queryset = Shortener.objects.last()
    permission_classes = (IsAuthenticatedOrReadOnly, )
    
    def create(self, *args, **kwargs):
        user = self.request.user
        req = self.request.POST
        website = req.get('website')
        short_code = req.get('short_code')
        serializer_data = {
            'website': website,
            'short_code': short_code,
            'author': user
        }
        url = urlparse(website)

        if not url.scheme:
            raise serializers.ValidationError("You must add website scheme e.g. http or https")
        
        if short_code:
            code_count = len(short_code) or 0
    
            if code_count > 4 or code_count < 4:
                raise serializers.ValidationError("User defined shortcode must be only 4 characters")

        serializer_context = dict(
            request=HttpRequest()
        )
        
        serializer = self.serializer_class(data=serializer_data, context=serializer_context)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=user)

        return HttpResponseRedirect('/api/')

def redirect_to_site_view(request, *args, **kwargs):
    short_code = kwargs.get('short_code')
    site_obj = get_object_or_404(Shortener, short_code=short_code)
    link = site_obj.website

    if link:
        update_site_visits(site_obj)
        return HttpResponseRedirect(f"{link}")
