from django.urls import path

from . import views

urlpatterns = [
    path('send/', views.send_view, name='mailchimp-send'),
    path('ping/', views.mailchimp_transactional_ping_view),
]