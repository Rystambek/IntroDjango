from django.contrib import admin
from django.urls import path

from .views import (
            home,
            index,
            get_num,
            get_sum,
            get_user
        )

urlpatterns = [
    path('',index),
    path('home/',home),
    path('get-num/',get_num),
    path('get-sum/',get_sum),
    path('get-user/<str:username>',get_user)
]