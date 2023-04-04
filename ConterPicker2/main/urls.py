from . import views
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from .views import RegisterUser, LoginUser, logout_user

urlpatterns = [
    path('', views.index, name='home'),
    path('damn', views.damn),
    path('create/', views.create),
    path('Abaddon', views.Abaddon, name='Abaddon'),
    path('Axe', views.Axe, name='Axe'),
    path('Morphling', views.Morphling, name='Morphling'),
    path('Pudge', views.Pudge, name='Pudge'),
    path('reg', RegisterUser.as_view(), name='register'),
    path('log', LoginUser.as_view(), name='log'),
    path('logout', logout_user, name='logout'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
