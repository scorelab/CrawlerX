from django.urls import path
from .api_search_data_views import SearchData
urlpatterns = [
  path('', SearchData.as_view(), name='searching data'),
  ]