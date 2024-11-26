from django.urls import path
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),  # Use `.as_view()` to convert the class into a callable view
]
