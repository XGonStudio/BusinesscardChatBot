from django.urls import path
from .views import *


urlpatterns = [
    path('api/', MainInformationAPI.as_view(), name='api-main-info'),
    path('', index, name='index'),
    path('info', ContactsView.as_view(), name='contact')
]
