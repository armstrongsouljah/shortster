from signal import raise_signal
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView,
    CreateAPIView,
)

from shortener.models import Shortener

from .serializers import ShortenerSerializer, ShortenedUrlSerializer

# Create your views here.
class ShortenedUrlsView(ListAPIView):
    serializer_class = ShortenerSerializer
    
    def get_queryset(self):
        user = self.request.user
        qs  = Shortener.objects.filter(author=user)
        return qs

class ShortenedUrlDetailView(RetrieveAPIView):
    serializer_class = ShortenedUrlSerializer
    lookup_fields = ['short_code']

    def get_object(self):
        short_code = self.kwargs.get('short_code')
        site_obj = get_object_or_404(Shortener, short_code=short_code)
        if site_obj:
            link = site_obj.website
            return HttpResponseRedirect(redirect_to=f'{link}')
        return site_obj


class ShortenerCreateView(CreateAPIView):
    """
    Class for shortening  provided url

    """
    serializer_class = ShortenerSerializer
    queryset = Shortener.objects.last()
    
    def create(self, request, *args, **kwargs):
        user = self.request.user
        req = self.request.POST
        print('user.... ', user)
        website = req.get('website')
        short_code = req.get('short_code')
        serializer_data = {
            'website': website,
            'short_code': short_code,
            'author': user
        }
        serializer = self.serializer_class(data=serializer_data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=user)

        return Response(serializer.data)

def redirect_to_site_view(request, *args, **kwargs):
    short_code = kwargs.get('short_code')
    site_obj = get_object_or_404(Shortener, short_code=short_code)
    link = site_obj.website
    if link:
        return HttpResponseRedirect(f"{link}")
