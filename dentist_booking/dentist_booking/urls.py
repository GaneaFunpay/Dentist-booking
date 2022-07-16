from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.api.urls', namespace='users')),
    path('booking/', include('booking.api.urls', namespace='booking')),
]
