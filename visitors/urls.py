from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_visitor, name='add_visitor'),
    path('list/', views.visitor_list, name='visitor_list'),  # Ensure this line is present
    path('update/<int:visitor_id>/', views.update_visitor, name='update_visitor'),
    path('delete/<int:visitor_id>/', views.delete_visitor, name='delete_visitor'),
]
