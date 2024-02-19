from django.shortcuts import render, redirect


# Create your views here.
def create(request):
    return render(request, 'profile/create-profile.html')

def details(request):
    return render(request, 'profile/details-profile.html')

def edit(request):
    return render(request, 'profile/edit-profile.html')

def delete(request):
    return render(request, 'profile/delete-profile.html')
