from django.urls import path
from .views import DatasetList, UsersList
from .views import MultiTen


urlpatterns = [
    path('users/', UsersList.as_view(), name='users_list'),

    # This is just an example. DELETE it when starting a new project!
    path('add/', MultiTen.as_view(), name='testinc_celery'),

    path('datasets/', DatasetList.as_view(), name='dataset_list'),
]