from django.shortcuts import render
from .models import Publication
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin


class PublicationListView(ListView):
    model = Publication
    template_name = 'home.html'

class PublicationCreteView(LoginRequiredMixin, CreateView):
    model = Publication
    template_name = 'create.html'
    fields = ['title', 'content', 'author']
    success_url = reverse_lazy('publications-list')

class PublicationDetailView(LoginRequiredMixin, DetailView):
    model = Publication
    template_name = 'publication_detail.html'    
    
class PublicationUpdateView(UpdateView):
    model = Publication
    template_name = 'post_update.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('publications-list')

class PublicationDeleteView(DeleteView):
    model = Publication
    template_name = 'post_delete.html'
    success_url = reverse_lazy('publications-list')
    