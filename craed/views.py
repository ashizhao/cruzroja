# Create your views here.

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from braces import views

from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader

from django.contrib.gis.geos import Point

from .models import AED
from .forms import AEDUpdateForm, AEDCreateForm

class AEDListView(views.JSONResponseMixin, 
                  views.AjaxResponseMixin, 
                  ListView):
    model = AED
    context_object_name = 'aed_list'

    def get_ajax(self, request, *args, **kwargs):
        json = []
        entries = self.get_queryset()
        for entry in entries:
            json.append({
                'type': 'AED',
                'location': { 'x': entry.location.x, 
                              'y': entry.location.y },
                'name': entry.name
            })
        return self.render_json_response(json)

    def unverified(self):
        return self.request.GET.get('unverified')

    def private(self):
        return self.request.GET.get('private')

    def search(self):
        return self.request.GET.get('search')

    def nearby(self):
        return self.request.GET.get('nearby')

    def lat(self):
        return float(self.request.GET.get('lat') or 32.52174913333495)

    def lng(self):
        return float(self.request.GET.get('lng') or -117.0096155300208)
    
    def get_queryset(self, *args, **kwargs):

        # include unverified?
        if self.unverified():
            query = AED.objects.all()
        else:
            query = AED.objects.filter(verified__exact=True)

        # include private?
        if not self.private():
            query = query.filter(public__exact=True)

        # search?
        searchfor = self.search()
        if searchfor:
            query = query.filter(name__icontains=searchfor)

        return query.order_by('name')
    
class AEDDetailView(views.JSONResponseMixin, 
                    views.AjaxResponseMixin, 
                    DetailView):
    model = AED
    context_object_name = 'aed'

    def get_ajax(self, request, *args, **kwargs):
        entry = self.get_object()
        json = {
            'type': 'AED',
            'location': { 'x': entry.location.x, 
                          'y': entry.location.y },
            'name': entry.name,
            'description': entry.description,
            'address': entry.address,
            'number': entry.number,
            'neighborhood': entry.neighborhood,
            'city': entry.city,
            'state': entry.state,
            'country': entry.country,
            'zipcode': entry.zipcode,
            'public': entry.public,
            'date_created': entry.date_created,
            'date_verified': entry.date_verified,
            'date_modified': entry.date_modified,
        }
        return self.render_json_response(json)

class AEDUpdateView(UpdateView):
    model = AED
    context_object_name = 'aed'
    form_class = AEDUpdateForm
    success_url = reverse_lazy('list')
    
class AEDCreateView(CreateView):
    model = AED
    context_object_name = 'aed'
    form_class = AEDCreateForm
    success_url = reverse_lazy('list')

    def lat(self):
        return float(self.request.GET.get('lat') or 32.52174913333495)

    def lng(self):
        return float(self.request.GET.get('lng') or -117.0096155300208)

    def get_initial(self):
        point = Point(x = self.lng(), 
                      y = self.lat(), 
                      srid = 4326);
        return { 'location': point }

    def form_valid(self, form):
        # set contact to current user
        form.instance.contact = self.request.user
        return super(AEDCreateView, self).form_valid(form)

class AEDDeleteView(DeleteView):
    model = AED
    context_object_name = 'aed'
    success_url = reverse_lazy('list')
