from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic import DetailView
from django.views.generic import View
from .models import Ticket
from .models import Events
from .forms import EventForm, TicketForm

from django.contrib.auth.forms import UserCreationForm




class EventList(LoginRequiredMixin, ListView):
    model = Events
    context_object_name = 'events'
    template_name = 'eventApp/list.html'

    def get_queryset(self):
        queryset = Events.objects.filter(user=self.request.user)
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(nameEvent__icontains=query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context




class AddEvent(LoginRequiredMixin, CreateView): 
    model = Events  
    form_class = EventForm
    success_url = reverse_lazy('events') 
    template_name = 'eventApp/add_event.html'


    def post(self, request, *args, **kwargs):  
        self.object = None
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)


    def form_valid(self, form): 
        form.instance.user = self.request.user 
        return super().form_valid(form)






class EditEvent(LoginRequiredMixin, UpdateView): 
    model = Events 
    form_class = EventForm
    success_url = reverse_lazy('events') 
    template_name = 'eventApp/edit_event.html'


    def get_queryset(self):
        return Events.objects.filter(user=self.request.user) 




class DeleteEvent(LoginRequiredMixin, DeleteView):
    model = Events 
    context_object_name = 'events' 
    success_url = reverse_lazy('events') 
    template_name = 'eventApp/conf_del.html' 

    def get_queryset(self):
        return Events.objects.filter(user=self.request.user)



class EventDetail(LoginRequiredMixin, DetailView):
    model = Events
    template_name = 'eventApp/event_detail.html'
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['already_registered'] = Ticket.objects.filter(
            event=self.object,
            user=self.request.user
        ).exists()
        context['ticket_count'] = self.object.tickets.count()
        return context




class BuyTicket(LoginRequiredMixin, View):
    def get(self, request, pk):
        event = get_object_or_404(Events, pk=pk)
        form = TicketForm()
        return render(request, 'eventApp/buy_ticket.html', {'event': event, 'form': form})

    def post(self, request, pk):
        event = get_object_or_404(Events, pk=pk)
        form = TicketForm(request.POST)
        if form.is_valid():
            Ticket.objects.get_or_create(user=request.user, event=event)
            return redirect('ticket_success', pk=pk)
        return render(request, 'eventApp/buy_ticket.html', {'event': event, 'form': form})



class TicketSuccess(LoginRequiredMixin, DetailView):
    model = Events
    template_name = 'eventApp/ticket_success.html'
    context_object_name = 'event'






class Registro(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
