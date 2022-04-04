from django.urls import path
from . import views


app_name = 'communications'

urlpatterns = [
    # path('', views.com_list),
    # path('pp/', views.communications_list),
    # path('pp/add/', views.com_list),
    # path('about', views.CVg.as_view()),
    path('', views.list_coom, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail, name='post_detail'),
]
