import requests
from django.http import HttpResponse

class PrerenderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_agent = request.META.get('HTTP_USER_AGENT', '').lower()
        crawlers = ['googlebot', 'bingbot', 'yahoo', 'baiduspider']
        if any(crawler in user_agent for crawler in crawlers):
            prerender_url = f"https://service.prerender.io/https://www.alsiglobal.com{request.path}"
            response = requests.get(prerender_url, headers={'User-Agent': user_agent})
            if response.status_code == 200:
                return HttpResponse(response.content, content_type='text/html')
        return self.get_response(request)
