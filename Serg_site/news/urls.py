from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    path('test/', test),
    path('test2/', test2),

]
