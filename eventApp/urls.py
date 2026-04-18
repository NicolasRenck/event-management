from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from .views import EventList, AddEvent, EditEvent, DeleteEvent, EventDetail, BuyTicket, TicketSuccess

urlpatterns = [
    path('', TemplateView.as_view(template_name='registration/welcome.html'), name='home'),
    path('events/', EventList.as_view(), name='events'),
    path('event/<int:pk>/', EventDetail.as_view(), name='event_detail'),
    path('event/<int:pk>/ticket/', BuyTicket.as_view(), name='buy_ticket'),
    path('event/<int:pk>/ticket/success', TicketSuccess.as_view(), name='ticket_success'),
    path('add/', AddEvent.as_view(), name='add_event'),
    path('edit/<int:pk>/', EditEvent.as_view(), name='edit_event'),
    path('delete/<int:pk>/', DeleteEvent.as_view(), name='delete_event'),
    path('logout/', LogoutView.as_view(), name='logout'),
]