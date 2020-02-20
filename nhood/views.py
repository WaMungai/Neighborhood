from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import News,Neighborhood,Business,UserProfile
# Create your views here.
def home(request):
    return HttpResponse('News from your neighbourly neighborhood')

@login_required(login_url='/accounts/login')
def search_business(request):
    if 'business' in request.GET and request.GET["business"]:
        search_term=request.GET.get("business")
        search_categories = Business.search_by_business(search_term)
        message = f"{search_term}"
        
        return render(request, "searchbusiness.html",{"message":message,"businesssearched": search_categories})
    else:
        message ="You haven't searched for any categories"
        return render(request, 'searchbusiness.html',{"message":message,"businesssearched":search_categories})