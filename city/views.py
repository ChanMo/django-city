import json
import urllib
from django.views.generic.base import View
from .models import City

class CityViewMixin(View):
    """
    City view mixin, set current city
    """
    def dispath(self, request, *args, **kwargs):
        try:
            city_name = request.session['city']
        except KeyError:
	    ip = get_ip(request)
            city_name = get_city_name(ip)
            request.session['city'] = city_name
        self.city = self.get_city(city_name)
        return super(CityViewMixin, self).dispatch(request, *args, **kwargs)

    def get_ip(self, request):
        """get client ip"""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def get_city_name(self, ip):
        """get city """
        url = 'http://restapi.amap.com/v3/ip?ip=%s&key=%s'\
                % (ip,'bf3561891ae40b0696600106787ebe26')
        with urllib.urlopen(url) as f:
            data = f.read().decode('utf-8')
            json_data = json.loads(data)
            if json_data['status'] == 1:
                city = json_data['city'][0:-1]
            else:
                city = ''
            return city

    def get_city(self, name):
        """get city model"""
        try:
            city = City.objects.get(name=name)
        except City.DoesNotExist:
            city = City.objects.first()
        return city
