from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm,UpdateProfileForm,CreateHoodForm
from django.http import HttpResponseRedirect, Http404
from . models import Profile,Neighbourhood
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
@csrf_exempt
def index(request):    
    return render(request,'index.html')

@csrf_exempt
@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user = request.user
    title = "Create Profile"
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return HttpResponseRedirect('/')

    else:
        form = ProfileForm()
    return render(request, 'profile/create_profile.html', {"form": form, "title": title})



@login_required(login_url='/accounts/login/')
def user_profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()

    return render(request,"profile/profile.html",{'profile':profile})

def update_profile(request,id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user = user)
    form = UpdateProfileForm(instance=profile)
    if request.method == "POST":
            form = UpdateProfileForm(request.POST,request.FILES,instance=profile)
            if form.is_valid():  
                
                profile = form.save(commit=False)
                profile.save()
                return redirect('profile') 
            
    return render(request, 'profile/update_profile.html', {"form":form})

@login_required(login_url='/accounts/login/')
def create_hood(request):
    current_user = request.user
    title = 'Create Hood'

    if request.method == 'POST':
        hood_form = CreateHoodForm(request.POST, request.FILES)
        if hood_form.is_valid():
            hood = hood_form.save(commit=False)
            hood.user = current_user
            hood.save()
        return HttpResponseRedirect('/hoods')

    else:
        hood_form = CreateHoodForm()
    return render(request, 'hood/create_hood.html', {"hood_form": hood_form, "title": title})

@login_required(login_url='/accounts/login/')
def hoods(request):
    hood = Neighbourhood.objects.all().order_by('-id')
    
    return render(request,'hood/hood.html',{'hood':hood})

@login_required(login_url='/accounts/login/')
def specific_hood(request,hood_name):
    hood = Neighbourhood.objects.get(hood_name=hood_name)
    return render(request,'hood/specific_hood.html',{'hood':hood})

@login_required(login_url='/accounts/login/')
def join_hood(request,hood_name):
    neighbourhood = get_object_or_404(Neighbourhood, hood_name=hood_name)
    request.user.profile.neighbourhood = neighbourhood
    request.user.profile.neighbourhood.save()
    return redirect('hoods')

# def join_hood(request, name):
#     neighbourhood = get_object_or_404(Neighborhood, name=name)
#     request.user.profile.neighbourhood = neighbourhood
#     request.user.profile.save()
#     return redirect('hood')