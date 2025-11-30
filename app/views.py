from django.http import HttpRequest, HttpResponse
from django.core.cache import cache
from django.shortcuts import render
from django.conf import settings


def show_number(request: HttpRequest) -> HttpResponse:
    """Show the number of times the page has been visited."""
    key = settings.NUMBER_CACHE_KEY
    cache.add(key, 0)
    number = cache.incr(key)
    return render(request, "number.html", {"number": number})
