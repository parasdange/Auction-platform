from django.urls import path

from . import views

urlpatterns=[

path('sellproduct/',views.sellproduct),

path('search/',views.search),

path('contact_us/',views.contact_us),

]