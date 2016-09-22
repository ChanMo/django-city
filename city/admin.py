from django.contrib import admin
from .models import City

class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'is_actived', 'created', 'updated')
    list_per_page = 12
    list_filter = ['is_actived', 'created', 'updated']
    search_fields = ['name']


class CityAdminMixin(admin.ModelAdmin):
    """
    City auth admin
    """
    list_display = ()
    list_filter = ()
    fields = ()
    exclude = ()
    readonly_for_city = ()

    def get_city(self, request):
        try:
            city = City.objects.get(user=request.user)
        except City.DoesNotExist:
            city = None
        return city


    def get_list_display(self, request):
        if self.get_city(request):
            return self.list_display
        else:

            if ('city,') in self.list_display:
                return self.list_display
            else:
                return ('city',) + self.list_display


    def get_list_filter(self, request):
        if self.get_city(request):
            return self.list_filter
        else:
            if ('city',) in self.list_filter:
                return self.list_filter
            else:
                return ('city',) + self.list_filter


    def add_view(self, request, form_url='', extra_context=None):
        if self.get_city(request):
            if ('city',) not in self.exclude:
                self.exclude += ('city',)
        return super(CityAdminMixin, self).\
                add_view(request, form_url, extra_context)


    def change_view(self, request, object_id, extra_context=None):
        """ If city has not add authority """
        if self.get_city(request):
            if ('city',) not in self.exclude:
                self.exclude += ('city',)
            #if self.readonly_for_city not in self.readonly_fields:
            #    self.readonly_fields += self.readonly_for_city
        return super(CityAdminMixin,self).\
                change_view(request, object_id, extra_context)


    def get_queryset(self, request):
        queryset = super(CityAdminMixin, self).get_queryset(request)
        city = self.get_city(request)
        if city:
            queryset = queryset.filter(city=city)
        return queryset


    def save_model(self, request, obj, form, change):
        """ Only for Add """
        city = self.get_city(request)
        if city:
            obj.city = city
        obj.save()


admin.site.register(City, CityAdmin)
