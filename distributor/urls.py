from django.urls import path
from .views import DistributorSignUpView

urlpatterns = [
    path('signup/', DistributorSignUpView.as_view(), name='distributor_signup'),
]
