from django.urls import path
from . import views
from .views import ClassesListView, ClassesDetailView, ClassesCreateView

urlpatterns = [
    path('', ClassesListView.as_view(), name='class-notes'),
    path('<int:pk>/', ClassesDetailView.as_view(), name='note-detail'),
    path('new/', ClassesCreateView.as_view(), name='note-create')
]
