from django.urls import path

from booking.views import IndexView, BookingView, get_schedule


app_name = 'booking'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('book/', BookingView.as_view(), name='booking'),
    path('get-schedule/', get_schedule, name='get_schedule'),
]
