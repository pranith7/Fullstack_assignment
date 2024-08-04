from django.urls import path
from .views import InterestListCreate, InterestUpdate

urlpatterns = [
       path('interests/', InterestListCreate.as_view(), name='interest-list-create'),
       path('interests/<int:pk>/', InterestUpdate.as_view(), name='interest-update'),
   ]