from django.contrib.auth.models import User
from django.conf import settings
from django import forms
from django.contrib.gis import forms as gis_forms
from django.contrib.gis.forms import widgets as gis_widgets
from django.core.serializers import serialize

from .models import AED

class LeafletPointWidget(gis_widgets.BaseGeometryWidget):
    template_name = 'leaflet/leaflet.html'

    class Media:
        css = {
            'all': ('leaflet/css/LeafletWidget.css',)
        }
        js = (
            'http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.js',
            'leaflet/js/LeafletWidget.js'
        )
        
    def render(self, name, value, attrs=None):
        # add point
        if value:
            attrs.update({ 'point': { 'x': value.x, 
                                      'y': value.y, 
                                      'z': value.z, 
                                      'srid': value.srid } 
                       })
        return super().render(name, value, attrs)

class AEDUpdateForm(forms.ModelForm):
    class Meta:
        model = AED
        fields = ['location',
                  'name', 'description',
                  'address', 'number', 'neighborhood', 
                  'city', 'state', 'country', 'zipcode',
                  'public', 'contact']
    contact = forms.ModelChoiceField(queryset=User.objects.all(), 
                                     disabled=True, empty_label=None)
    location = gis_forms.PointField(
        widget = LeafletPointWidget(attrs={'map_width': 500, 
                                           'map_height': 300}))

class AEDCreateForm(forms.ModelForm):
    class Meta:
        model = AED
        fields = ['location',
                  'name', 'description',
                  'address', 'number', 'neighborhood',
                  'city', 'state', 'country', 'zipcode',
                  'public']
    location = gis_forms.PointField(
        widget = LeafletPointWidget(attrs={'map_width': 500, 
                                           'map_height': 300}))
