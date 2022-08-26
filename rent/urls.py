from django.urls import path

from rent import views

app_name = 'rent'

urlpatterns = [
    path('', views.index,  name='index'),
    path('avg-count/', views.avg_count, name='avg-count'),
    path('reservation/', views.reservation_count_avg_price, name='reservation'),
    path('avg-reviews/', views.avg_reviews, name='avg-reviews'),
]
