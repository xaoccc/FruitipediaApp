from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView
from fruitipediaApp.fruits.forms import FruitCreateForm, FruitEditForm, FruitDeleteForm
from fruitipediaApp.fruits.models import Fruit
from fruitipediaApp.profiles.models import Profile


class ReadonlyViewMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        for field in form.fields.values():
            field.widget.attrs["readonly"] = "readonly"
        return form

class GetProfileMixin:
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = Profile.objects.first()
        return context

class HomePageView(GetProfileMixin, TemplateView):
    template_name = 'common/index.html'

class DashboardView(ListView):
    model = Fruit
    template_name = 'common/dashboard.html'
    context_object_name = 'fruits'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = Profile.objects.first()
        return context

class FruitCreateView(GetProfileMixin, CreateView):
    form_class = FruitCreateForm
    template_name = 'fruits/create-fruit.html'
    def get_success_url(self):
        return reverse('dashboard')

    # Set the first Profile model to become the owner of the fruit, since owner is required
    def form_valid(self, form):
        form.instance.owner = Profile.objects.first()
        return super().form_valid(form)


class FruitDetailView(GetProfileMixin, DetailView):
    template_name = 'fruits/details-fruit.html'
    model = Fruit


class FruitEditView(GetProfileMixin, UpdateView):
    form_class = FruitEditForm
    template_name = 'fruits/edit-fruit.html'
    model = Fruit

    def get_success_url(self):
        return reverse('dashboard')


class FruitDeleteView(ReadonlyViewMixin, GetProfileMixin, DeleteView):
    model = Fruit
    form_class = FruitDeleteForm
    template_name = 'fruits/delete-fruit.html'
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs

