from django.urls import include, path

urlpatterns = [
    path('rest-auth/', include('dj_rest_auth.urls')),
    path('rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('users/', include('users.urls')),
]
