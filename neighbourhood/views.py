from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm,UpdateProfileForm,CreateHoodForm,BusinessForm,PostForm
from django.http import HttpResponseRedirect, Http404
from . models import Business, Profile,Neighbourhood,Post
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
@csrf_exempt
def index(request):    
    current_user = request.user
    profile.user = current_user

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
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    neighbourhood = Neighbourhood.objects.all()


    return render(request,"profile/profile.html",{'profile':profile,'neighbourhood':neighbourhood})

def update_profile(request,id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user = user)
    form = UpdateProfileForm(instance=profile)
    if request.method == "POST":
            form = UpdateProfileForm(request.POST,request.FILES,instance=profile)
            if form.is_valid():  
                
                profile = form.save(commit=False)
                profile.save()
                return redirect('/profile') 
            
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
    hoods = Neighbourhood.objects.all().order_by('-id')
    return render(request,'hood/hood.html',{'hoods':hoods})

@login_required(login_url='/accounts/login/')
def specific_hood(request,id):
    hood = Neighbourhood.objects.get(id=id)
    biznas = Business.get_business(id)
    posts = Post.get_post(hood)

    return render(request,'hood/specific_hood.html',{'hood':hood,'biznas':biznas,'posts':posts})

@login_required(login_url='/accounts/login/')
def join_hood(request,id):
    neighbourhood = Neighbourhood.objects.get(id=id)
    current_user = request.user
    current_user.profile.neighbourhood = neighbourhood
    current_user.profile.save()
    return redirect('hoods')

@login_required(login_url='/accounts/login/')
def leave_hood(request, id):
    hood = get_object_or_404(Neighbourhood, id=id)
    request.user.profile.neighbourhood = None
    request.user.profile.save()
    return redirect('hoods')

@login_required(login_url='/accounts/login/')
def create_business(request):
    current_user = request.user
    title = 'Create Business'

    if request.method == 'POST':
        biz_form = BusinessForm(request.POST, request.FILES)
        if biz_form.is_valid():
            biz = biz_form.save(commit=False)
            biz.user = current_user
            biz.save()
        return HttpResponseRedirect('/hoods')

    else:
        biz_form = BusinessForm()
    return render(request, 'business/create_biz.html', {"biz_form": biz_form, "title": title})

@login_required(login_url='/accounts/login/')
def create_post(request):
    current_user = request.user
    title = 'Write Post'

    if request.method == 'POST':
        p_form = PostForm(request.POST, request.FILES)
        if p_form.is_valid():
            pos = p_form.save(commit=False)
            pos.user = current_user
            pos.save()
        return HttpResponseRedirect('/hoods')

    else:
        p_form = PostForm()
    return render(request, 'post/create_post.html', {"p_form": p_form, "title": title})

@login_required(login_url="/accounts/login/")
def search(request):
    if 'search_term' in request.GET and request.GET["search_term"]:
        search_term = request.GET.get("search_term")
        searched_businesses = Business.objects.filter(business_name__icontains=search_term)
        message = f"Search For: {search_term}"

        return render(request, "results.html", {"message": message, "searched_businesses": searched_businesses})
    else:
        message = "You haven't searched for any term"
        return render(request, "results.html", {"message": message})