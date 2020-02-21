from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('account/', include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('search/', views.search_hoods, name='search'),
    path('addneighborhood',views.addNeighborhood,name="addNeighborhood"),
    path('details/<id>/' , views.neighborhood_details, name='details' ),
    
]