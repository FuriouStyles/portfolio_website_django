from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Notes
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django import template


# def notes(request):
#     return render(request, 'notes/notes_home.html')


class ClassesListView(ListView):
    model = Notes
    template_name = 'notes/notes_home.html'
    context_object_name = 'notes'
    ordering = ['-date_posted']
    paginate_by = 10


class ClassesDetailView(DetailView):
    model = Notes


class ClassesCreateView(LoginRequiredMixin, CreateView):
    model = Notes
    fields = ['title', 'notes', 'colab', 'youtube', ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ClassesUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Notes
    fields = ['title', 'notes', 'colab', 'youtube', ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        note = self.get_object()
        if self.request.user == note.author:
            return True
        return False


class ClassesDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Notes
    success_url = '/notes'

    def test_func(self):
        note = self.get_object()
        if self.request.user == note.author:
            return True
        return False
