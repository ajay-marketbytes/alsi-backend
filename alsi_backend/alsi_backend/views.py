from django.http import HttpResponse
from services.models import Services, SpecializedService
from market.models import BlogEntry
from datetime import datetime

def sitemap_view(request):
    # Current date for static pages
    current_date = datetime.now().strftime('%Y-%m-%d')

    # Static pages
    urls = [
        {'loc': 'https://www.alsiglobal.com/', 'lastmod': current_date, 'changefreq': 'weekly', 'priority': '1.0'},
        {'loc': 'https://www.alsiglobal.com/services', 'lastmod': current_date, 'changefreq': 'weekly', 'priority': '0.9'},
        {'loc': 'https://www.alsiglobal.com/about-us', 'lastmod': current_date, 'changefreq': 'monthly', 'priority': '0.9'},
        {'loc': 'https://www.alsiglobal.com/our-network', 'lastmod': current_date, 'changefreq': 'monthly', 'priority': '0.9'},
        {'loc': 'https://www.alsiglobal.com/industries', 'lastmod': current_date, 'changefreq': 'monthly', 'priority': '0.8'},
        {'loc': 'https://www.alsiglobal.com/market-updates', 'lastmod': current_date, 'changefreq': 'weekly', 'priority': '0.7'},
        {'loc': 'https://www.alsiglobal.com/gallery', 'lastmod': current_date, 'changefreq': 'monthly', 'priority': '0.7'},
        {'loc': 'https://www.alsiglobal.com/contact-us', 'lastmod': current_date, 'changefreq': 'monthly', 'priority': '0.8'},
        {'loc': 'https://www.alsiglobal.com/careers', 'lastmod': current_date, 'changefreq': 'monthly', 'priority': '0.7'},
    ]

    # Services pages
    for service in Services.objects.filter(link_url__isnull=False).exclude(link_url=''):
        lastmod = service.updated_at.strftime('%Y-%m-%d') if hasattr(service, 'updated_at') and service.updated_at else current_date
        urls.append({
            'loc': f'https://www.alsiglobal.com/services/{service.link_url}',
            'lastmod': lastmod,
            'changefreq': 'monthly',
            'priority': '0.9',
        })

    # Specialized services
    for spec_service in SpecializedService.objects.filter(link_url__isnull=False).exclude(link_url=''):
        lastmod = spec_service.updated_at.strftime('%Y-%m-%d') if hasattr(spec_service, 'updated_at') and spec_service.updated_at else current_date
        urls.append({
            'loc': f'https://www.alsiglobal.com/services/{spec_service.link_url}',
            'lastmod': lastmod,
            'changefreq': 'monthly',
            'priority': '0.9',
        })

    # Blog entries
    for blog in BlogEntry.objects.filter(blog_slug__isnull=False).exclude(blog_slug=''):
        lastmod = blog.updated_at.strftime('%Y-%m-%d') if blog.updated_at else current_date
        urls.append({
            'loc': f'https://www.alsiglobal.com/market-updates/{blog.blog_slug}',
            'lastmod': lastmod,
            'changefreq': 'weekly',
            'priority': '0.8',
        })

    # Generate XML
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for url in urls:
        xml += '  <url>\n'
        xml += f'    <loc>{url["loc"]}</loc>\n'
        xml += f'    <lastmod>{url["lastmod"]}</lastmod>\n'
        xml += f'    <changefreq>{url["changefreq"]}</changefreq>\n'
        xml += f'    <priority>{url["priority"]}</priority>\n'
        xml += '  </url>\n'
    xml += '</urlset>'
    return HttpResponse(xml, content_type='application/xml')

def robots_txt(request):
    lines = [
        "User-agent: *",
        "Allow: /",
        "Disallow: /admin/",
        "Disallow: /api/",
        "Disallow: /private/",
        "Disallow: /*.json$",
        "Disallow: /*.txt$",
        "Sitemap: https://www.alsiglobal.com/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")