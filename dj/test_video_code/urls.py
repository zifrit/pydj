from django.urls import path
from . import views


urlpatterns = [
    path('', views.main),
    path('<name_zodiac>/', views.zodiac),

    # path('aa/', views.aa),
]