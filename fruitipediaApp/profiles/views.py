from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from fruitipediaApp.fruits.models import Fruit
from fruitipediaApp.profiles.forms import ProfileCreateForm, ProfileEditForm
from fruitipediaApp.profiles.models import Profile


class GetProfileMixin:
    def get_object(self, queryset=None):
        return Profile.objects.first()

class ProfileCreateView(CreateView):
    template_name = 'profile/create-profile.html'
    form_class = ProfileCreateForm

    def get_success_url(self):
        return reverse('dashboard')


class ProfileDetailView(GetProfileMixin, DetailView):
    template_name = 'profile/details-profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fruit_posts'] = Fruit.objects.all().count
        return context


class ProfileEditView(GetProfileMixin, UpdateView):
    template_name = 'profile/edit-profile.html'
    form_class = ProfileEditForm

    def get_success_url(self):
        return reverse('dashboard')


class ProfileDeleteView(GetProfileMixin, DeleteView):
    model = Profile
    template_name = 'profile/delete-profile.html'
    success_url = reverse_lazy('index')



