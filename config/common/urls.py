from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

""" urlpatterns = [
    path('', views.index, name='index'),
    path('<int:itemspec_list_id>/', views.detail, name='detail'),
]  """