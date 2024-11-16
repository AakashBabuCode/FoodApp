from django.urls import path
from .views import (
    home,
    register,
    login_view,
    admin_login_view,
    admin_dashboard,
    candidates_list,
    positions_list,
    add_candidate,
    vote,
)

urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login_view, name='voter_login'),
    path('admin/login/', admin_login_view, name='admin_login'),
    path('dashboard/', admin_dashboard, name='admin_dashboard'),  
    path('admin/candidates/', candidates_list, name='candidates_list'),
    path('admin/positions/', positions_list, name='positions_list'),
    path('candidates/', candidates_list, name='candidates_list'),
    path('add-candidate/', add_candidate, name='add_candidate'),
    path('vote/', vote, name='vote'),
]
