from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import DetailView, CreateView, UpdateView

from fruitipediaApp.fruits.models import Fruit
from fruitipediaApp.profiles.forms import ProfileCreateForm, ProfileEditForm
from fruitipediaApp.profiles.models import Profile


class ProfileCreateView(CreateView):
    template_name = 'profile/create-profile.html'
    form_class = ProfileCreateForm

    def get_success_url(self):
        return reverse('dashboard')

class ProfileDetailView(DetailView):
    template_name = 'profile/details-profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fruit_posts'] = Fruit.objects.all().count
        return context

    def get_object(self, queryset=None):
        return Profile.objects.first()

class ProfileEditView(UpdateView):
    template_name = 'profile/edit-profile.html'
    form_class = ProfileEditForm

    def get_object(self, queryset=None):
        return Profile.objects.first()

    def get_success_url(self):
        return reverse('dashboard')


def delete(request):
    return render(request, 'profile/delete-profile.html')
