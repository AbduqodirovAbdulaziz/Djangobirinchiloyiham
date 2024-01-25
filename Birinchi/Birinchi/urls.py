
from django.contrib import admin
from django.urls import path
from sotuv.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('salom/', salomlash),
    path('boqcha/', bosh_sahifa),
    path('cristiano/', cristiano),

]
