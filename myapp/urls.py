from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.add_remove, name="addshow"),
    path('delete/<int:id>/', views.delete, name="delete"),
    path('update/<int:st>/', views.update_data, name="update"),
]