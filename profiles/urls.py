from django.urls import path
from django.contrib.auth import views as auth_views

from profiles import views

urlpatterns = [
    path('profile_data/', views.profile_data, name="profile_data"),
    path('profile_security/', views.profile_security, name="profile_security"),
    path('profile_events/', views.profile_events, name="profile_events"),
    path('profile_accreditation/', views.profile_accreditation, name="profile_accreditation"),
    path('profile_certificates/', views.profile_certificates, name="profile_certificates"),
    path('profile_content/', views.profile_content, name="profile_content"),

    path('content/', views.content, name="content"),  # Proximamente

    # manejo de cuentas
    path('register/', views.register_profile, name="profile_register"),
    path('login/', views.AcademiaLogin.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),

    # api
    path('login/', views.api_create_profile, name="create_profile"),
]
