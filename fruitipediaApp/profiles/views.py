from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from fruitipediaApp.fruits.models import Fruit
from fruitipediaApp.profiles.models import Profile


# Create your views here.
def create(request):
    return render(request, 'profile/create-profile.html')

class ProfileDetailView(TemplateView):
    template_name = 'profile/details-profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        context['fruit_posts'] = Fruit.objects.all().count
        return context

def edit(request):
    return render(request, 'profile/edit-profile.html')

def delete(request):
    return render(request, 'profile/delete-profile.html')
