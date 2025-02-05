from django.urls import path
from .views import PartnerApplicationCreateView

urlpatterns = [
    path('apply/', PartnerApplicationCreateView.as_view(), name='apply'),
]
