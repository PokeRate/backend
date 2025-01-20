from rest_framework.routers import DefaultRouter

from .views import (PokemonAbilityViewset, PokemonMoveViewset,
                    PokemonTypeViewset, PokemonViewset)

router = DefaultRouter()
router.register(r'types', PokemonTypeViewset, basename='pokemon-type')
router.register(r'abilities', PokemonAbilityViewset,
                basename='pokemon-ability')
router.register(r'moves', PokemonMoveViewset, basename='pokemon-move')
router.register(r'', PokemonViewset, basename='pokemon')
urlpatterns = router.urls
