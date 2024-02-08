
from django.contrib import admin
from django.urls import path
from sotuv.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('salom/', salomlash),
    path('boqcha/', bosh_sahifa),
    path('cristiano/', cristiano),

    path('editNazoratchi/', editNazoratchi),
    path('ustoz/<int:id>/tahrirlash/', edit_Oqituvchi),

    path('hamma_kurslar/', hamma_kurslar),
    path('kurs/<int:id>/tahrirlash/', kursni_tahrirlash),

    path('hamma_fanlar/', hamma_fanlar),
    path('edit/<int:id>/tahrirlash/', fanlar_edit),

# form bilan qo'shish
    path('fan_add/', fan_add),

    path('ustoz_add/', ustoz_add),

    path('kurs_add/', kurs_add),
]
