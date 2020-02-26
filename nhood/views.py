from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import News,Neighborhood,Business,UserProfile
from django.contrib import messages
from .forms import NewsForm,UserProfileForm,BusinessForm

# Create your views here.
def home(request):
    news=News.objects.all()
    business=Business.objects.all()
    profile=UserProfile.objects.all()
    hood=Neighborhood.get_hood()
    return render(request,'home.html',{"news":news,"business":business,"profile":profile,"hood":hood})

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

@login_required(login_url='/accounts/login/')
def search_neighborhood(request):
    if 'neighborhood' in request.GET and request .GET["neighborhood"]:
        search_term = request.GET .get("neighborhood")
        searched_categories= Neighborhood.search_by_name(search_term)
        message =f"{search_term}"
        
        return render(request,'searchhood.html',{"message":message, "hoodsearched":searched_categories})
    else:
        message="You haven't searched for any category"
        return render(request,"searchhood.html",{"message":message})
    
@login_required(login_url='/accounts/login')
def single_business(request,businessid):
    single_business=Business.single_business(businessid)
    return render(request,'singlebusiness.html',{'singlebusiness':single_business})   

@login_required(login_url='/accounts/login')
def single_news(request,newsid):
    single_post=News.single_news(newsid)
    return render(request,'singlenews.html',{"single_post":single_post})

@login_required(login_url='/accounts/login')
def single_profile(request,userid):
    profile=UserProfile.objects.all()
    try:
        singleprofile=UserProfile.single_profile(userid)
        businessowned=Business.businessowner(userid)
        newsbyuser=News.newsbyuser(userid)
        
    except UserProfile.DoesNotExist:
        messages.info(request,'The user has not created a profile yet')
        
    except Business.DoesNotExist:
        messages.info(request,'The user has no business posted')
    
    except News.DoesNotExist:
        messages.infor(request,'User has not postedany alerts.')
        
    return render(request,'profile.html',{"profile":profile}) 

@login_required(login_url='/accounts/login/')
def add_news(request):
    current_user=request.user
    if request.method == 'POST':
        form = NewsForm(request.POST, request.files)
        if form.is_valid:
            news=form.save(commit=False)
            news.editor=current_user
            news.save()
        return redirect('home')
    else:
        form=NewsForm()
    return render(request,'postnews.html',{"form":form})

@login_required(login_url='/accounts/login/')
def add_business(request):
    current_user = request.user
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid:
            business=form.save(commit=False)
            business.editor=current_user
            business.save()
        return redirect('home')
    else:
        form=BusinessForm()
    return render(request,'postbusiness.html',{"form":form})

@login_required(login_url='/accounts/login/')
def createprofile(request):
    current_user=request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile=form.save(commit=False)
            profile.editor=current_user
            profile.save()
        return redirect('home')
    else:
        form=UserProfileForm()
    return render(request,'postprofile.html',{"form":form})