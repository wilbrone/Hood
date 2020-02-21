from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.views.generic import RedirectView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from .forms import *
from .models import *

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/registration.html', {'form': form})


@login_required(login_url='login')
def index(request):
    hoods = Neighborhood.objects.all()
    return render(request, 'all-dtls/index.html',{'hoods':hoods})


@login_required(login_url='login')
def profile(request):
    current_user = request.user
    profile = Profile.objects.all()

    if request.method == 'POST':
        u_form = UpdateUserForm(request.POST,instance=request.user)
        p_form = UpdateUserProfileForm(request.POST, request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            
            return render(request,'all-dtls/profile.html')
    else:
        u_form = UpdateUserForm(instance=request.user)
        p_form = UpdateUserProfileForm(instance=request.user.profile)


    context = {
        'u_form':u_form,
        'p_form':p_form
    }

    return render(request, 'registration/profile.html',locals())



def search_hoods(request):
    if 'search' in request.GET and request.GET['search']:
        search_term=request.GET.get('search')
        searched_hoods=Neighborhood.search_by_name(search_term)
        message=f'{search_term}'

        return render(request,'all-dtls/search.html',{"message":message,"searched_hoods":searched_hoods})

    else:
        message="You haven't searched for any term"

        return render(request, 'all-dtls/search.html',{"message":message})


@login_required(login_url='login')
def addNeighborhood(request):
    neighborform = NeighborhoodForm()
    if request.method == "POST":
        neighborform = NeighborhoodForm(request.POST,request.FILES)
        if neighborform.is_valid():
            post = neighborform.save(commit=False)
            post.user = request.user.profile
            post.save()
            return redirect ('index')
        else:
            neighborform=NeighborhoodForm(request.POST,request.FILES)

    return render(request,'all-dtls/hood_form.html',{"neighborform":neighborform})



@login_required(login_url='login')
def neighborhood_details(request,id):
    businesses=Business.objects.filter(neighborhood = id)
    posts=Post.objects.filter(neighborhood = id)
    neighborhood=Neighborhood.objects.get(pk = id)
    return render(request,'all-dtls/details.html',{'neighborhood':neighborhood,'businesses':businesses,'posts':posts})


@login_required(login_url='login')
def new_business(request,pk):
    current_user = request.user
    neighborhood = get_object_or_404(Neighborhood,pk=pk)
    if request.method == 'POST':
        business_form = NewBusinessForm(request.POST, request.FILES)
        if business_form.is_valid():
            business = business_form.save(commit=False)
            business.user = current_user
            business.neighborhood=neighborhood
            business.save()
        return redirect('details', id = neighborhood.id)

    else:
        business_form = NewBusinessForm()
    return render(request, 'all-dtls/new_business_form.html', {"form": business_form,'neighborhood':neighborhood})


@login_required(login_url='login')
def new_post(request,pk):
    current_user = request.user
    neighborhood = get_object_or_404(Neighborhood,pk=pk)
    if request.method == 'POST':
        post_form = NewPostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = current_user
            post.neighborhood=neighborhood
            post.save()
        return redirect('details',id = neighborhood.id)

    else:
        post_form = NewPostForm()
    return render(request, 'all-dtls/new_post_form.html', {"form": post_form,'neighborhood':neighborhood})
