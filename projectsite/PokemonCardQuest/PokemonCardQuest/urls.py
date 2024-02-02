"""
URL configuration for PokemonCardQuest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from CardQuest_app.views import Home, TrainerList, Collection, PokemonCard, TrainerCreateView, TrainerUpdateView, TrainerDeleteView
from CardQuest_app.views import PokemonCardCreateView, PokemonCardUpdateView, PokemonCardDeleteView, CollectionCreateView, CollectionUpdateView, CollectionDeleteView
from CardQuest_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home.as_view(), name='home'),
    path('trainer_list', TrainerList.as_view(), name='trainer-list'),
    path('collection', Collection.as_view(), name='collection'),
    path('pokemon_card', PokemonCard.as_view(), name='pokemon-card'),
    path('trainer_list/create', TrainerCreateView.as_view(), name='trainer_create'),
    path('trainer_list/<pk>', TrainerUpdateView.as_view(), name='trainer_update'),
    path('trainer_list/<pk>/delete',TrainerDeleteView.as_view(), name='trainer_delete'),
    path('pokemon_card/create', PokemonCardCreateView.as_view(), name='pokemoncard_create'),
    path('pokemon_card/<pk>', PokemonCardUpdateView.as_view(), name='pokemoncard_update'),
    path('pokemon_card/<pk>/delete',PokemonCardDeleteView.as_view(), name='pokemoncard_delete'),
    path('collection_list/create', CollectionCreateView.as_view(), name='collection_create'),
    path('collection_list/<pk>', CollectionUpdateView.as_view(), name='collection_update'),
    path('collection_list/<pk>/delete',CollectionDeleteView.as_view(), name='collection_delete'),
]
