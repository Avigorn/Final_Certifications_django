
from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    # path('recipes/', include('recipesapp.urls')),
    # path('admin/', admin.site.urls),
    # path('account/', include('users.urls')),
    # path('search/', views.search, name='search'),

    path('', include('django.contrib.auth.urls')),
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),


]
