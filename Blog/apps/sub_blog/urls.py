from django.urls import path
from .views import (
    SubPostDetailView,
    SubPostCreateView,
    SubPostUpdateView,
    SubPostDeleteView,
)
from . import views

urlpatterns = [
    path('subpost/<int:pk>/', SubPostDetailView.as_view(), name='sub_post-detail'),
    path('subpost/new/', SubPostCreateView.as_view(), name='sub_post-create'),
    path('subpost/<int:pk>/update/', SubPostUpdateView.as_view(), name='sub_post-update'),
    path('subpost/<int:pk>/delete/', SubPostDeleteView.as_view(), name='sub_post-delete'),
]