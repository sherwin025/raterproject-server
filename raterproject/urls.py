from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from raterprojectapi.models.game_review import GameReviews
from raterprojectapi.views import register_user, login_user
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

from raterprojectapi.views import GameView, CategoryView
from raterprojectapi.views.gamerating import RatingView
from raterprojectapi.views.gamereview import ReviewView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r"games", GameView, "game")
router.register(r"category", CategoryView, "category")
router.register(r"reviews", ReviewView, "reviews" )
router.register(r"ratings", RatingView, "reviews" )

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)