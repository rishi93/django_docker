from django.http import HttpResponse, JsonResponse
from django.views.decorators.cache import cache_page

from .models import Person

# Create your views here.
@cache_page(60*15) # Cache for 15 mins
def index(request):
    return HttpResponse("Hello world!")

@cache_page(60*30) # Cache for 30 mins
def users(request):
    users = Person.objects.all()
    users = [user.full_name for user in users]
    return JsonResponse(users, safe=False)