from django.urls import path

from . import views

app_name = 'heatpipe'

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.index, name='index'),
    path('<int:itemspec_list_id>/', views.detail, name='detail'),
] 