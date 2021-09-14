from django.contrib import admin
from django.urls import path



from frontend.views import (homepage)

urlpatterns = [
    path('', homepage),
]