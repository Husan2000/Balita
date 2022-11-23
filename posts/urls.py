from django.urls import path
from .views import home_view, post_detail_view


urlpatterns = [
    path('', home_view, name='home'),
    path('detail/<slug:slug>/', post_detail_view, name='detail'),
]
