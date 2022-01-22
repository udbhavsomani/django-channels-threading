from django.contrib import admin
from django.urls import path
import home.views

urlpatterns = [
    path('', home.views.home, name='home'),
    path('api/', home.views.generate_data, name='generate_data'),
    path('admin/', admin.site.urls),
]
