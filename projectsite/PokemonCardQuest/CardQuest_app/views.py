from typing import Any
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from CardQuest_app.models import PokemonCard, Trainer, Collection
from CardQuest_app.forms import TrainerForm, PokemonCardForm, CollectionForm
from django.urls import reverse_lazy

# Create your views here.
class Home(ListView):
    model = PokemonCard
    content_type_name = 'home'
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class TrainerList(ListView):
    model = Trainer
    context_object_name = 'trainer'
    template_name = "trainer.html"
    paginate_by = 15

class Collection(ListView):
    model = Collection
    context_object_name = 'collection'
    template_name = "collection.html"
    paginate_by = 15
    
class PokemonCard(ListView):
    model = PokemonCard
    context_object_name = 'pokemon-card'
    template_name = "pokemon-card.html"
    paginate_by = 15

# Create
class TrainerCreateView(CreateView):
    model = Trainer
    form_class = TrainerForm
    template_name = 'trainer_create.html'
    success_url = reverse_lazy('trainer-list')

class PokemonCardCreateView(CreateView):
    model = PokemonCard
    form_class = PokemonCardForm
    template_name = 'pokemon-card_create.html'
    success_url = reverse_lazy('pokemon_card')

class CollectionCreateView(CreateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'collection_create.html'
    success_url = reverse_lazy('collection')

# Update
class TrainerUpdateView(UpdateView):
    model = Trainer
    form_class = TrainerForm
    template_name = 'trainer_update.html'
    success_url = reverse_lazy('trainer-list')

class PokemonCardUpdateView(UpdateView):
    model = PokemonCard
    form_class = PokemonCardForm
    template_name = 'pokemon-card_update.html'
    success_url = reverse_lazy('pokemon_card')

class CollectionUpdateView(UpdateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'collection_update.html'
    success_url = reverse_lazy('collection')

#DELETE
class TrainerDeleteView(DeleteView):
    model = Trainer
    template_name = 'trainer_delete.html'
    success_url = reverse_lazy('trainer-list')

class PokemonCardDeleteView(DeleteView):
    model = PokemonCard
    template_name = 'pokemon-card_delete.html'
    success_url = reverse_lazy('pokemon_card')

class CollectionDeleteView(DeleteView):
    model = Collection
    template_name = 'collection_delete.html'
    success_url = reverse_lazy('collection')