from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import BlogBanner, BlogEntry
from .serializers import BlogBannerSerializer, BlogEntrySerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class BlogBannerViewSet(viewsets.ModelViewSet):
    queryset = BlogBanner.objects.all()
    serializer_class = BlogBannerSerializer
    permission_classes = [AllowAny]

class BlogEntryViewSet(viewsets.ModelViewSet):
    queryset = BlogEntry.objects.all().order_by('-created_at')
    serializer_class = BlogEntrySerializer
    permission_classes = [AllowAny]
    lookup_field = 'blog_slug'
    
    def retrieve(self, request, *args, **kwargs):
        try:
            blog_slug = kwargs.get('blog_slug')
            instance = get_object_or_404(BlogEntry, blog_slug=blog_slug)
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=500
            )