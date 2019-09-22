from django.contrib import admin
from django.urls import include, path

from pages.views import index, index2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('', index, name='home'),

]
