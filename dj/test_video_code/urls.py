from django.urls import path
from . import views


urlpatterns = [
    path('', views.main),
    path('type/', views.element_zodiac),
    path('month/<int:month>/<int:dayt>', views.month_to_zodiac),
    path('type/<element_to_zodiac>/', views.element_to_zodiac),
    path('<name_zodiac>/', views.zodiac),
    # path('aa/', views.aa),
]