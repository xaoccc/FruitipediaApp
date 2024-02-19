from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView

from fruitipediaApp.fruits.forms import FruitCreateForm, FruitEditForm, FruitDeleteForm
from fruitipediaApp.fruits.models import Fruit
from fruitipediaApp.profiles.models import Profile


class HomePageView(TemplateView):
    template_name = 'common/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        return context

def index(request):
    return render(request, 'common/index.html')


class DashboardView(ListView):
    model = Fruit
    template_name = 'common/dashboard.html'
    context_object_name = 'fruits'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = Profile.objects.first()
        return context

class FruitCreateView(CreateView):
    form_class = FruitCreateForm
    template_name = 'fruits/create-fruit.html'
    def get_success_url(self):
        return reverse('dashboard')

    # Set the first Profile model to become the owner of the fruit, since owner is required
    def form_valid(self, form):
        form.instance.owner = Profile.objects.first()
        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = Profile.objects.first()
        return context


class FruitDetailView(DetailView):
    template_name = 'fruits/details-fruit.html'
    model = Fruit

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = Profile.objects.first()
        return context


def details_fruit(request, pk):
    fruit = Fruit.objects.filter(pk=pk).get()

    context = {
        'fruit': fruit,
    }

    return render(request, 'fruits/details-fruit.html', context)


class FruitEditView(UpdateView):
    form_class = FruitEditForm
    template_name = 'fruits/edit-fruit.html'
    model = Fruit

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = Profile.objects.first()
        return context

    def get_success_url(self):
        return reverse('dashboard')




def delete_fruit(request, fruit_id):
    fruit = Fruit.objects.filter(pk=fruit_id).get()

    if request.method == 'GET':
        form = FruitDeleteForm(instance=fruit)
    else:
        form = FruitDeleteForm(request.POST, instance=fruit)

        if form.is_valid():
            fruit.delete()

            return redirect('dashboard')

    context = {
        'form': form,
        'fruit': fruit,
    }

    return render(request, 'fruits/delete-fruit.html', context)


