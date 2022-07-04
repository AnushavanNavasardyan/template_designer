from django.urls import path
from .views import  HomePageListView, AboutPageListView, ExplorePageListView, TrendingPageListView, contact

urlpatterns = [
    # path('base/', BaseFooterListView.as_view(), name='index'),

    path('', HomePageListView.as_view(), name='index'),
    path('about/', AboutPageListView.as_view(), name='about'),
    path('explore/', ExplorePageListView.as_view(), name='explore'),

    path('trending/', TrendingPageListView.as_view(), name='trending'),

    path('contact/', contact, name='contact'),


]