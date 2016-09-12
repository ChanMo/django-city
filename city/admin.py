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
    city = None

    def set_city(self, request):
        try:
            city = City.objects.get(user=request.user)
        except City.DoesNotExist:
            city = None
        self.city = city

    def get_list_display(self, request):
        self.set_city(request)
        if self.city:
            return self.list_display
        else:
            return ('city',) + self.list_display

    def get_list_filter(self, request):
        self.set_city(request)
        if self.city:
            return self.list_filter
        else:
            return ('city',) + self.list_filter

    def get_fields(self, request, obj=None):
        self.set_city(request)
        if self.city:
            return self.fields
        else:
            return ('city',) + self.fields

    def get_queryset(self, request):
        self.set_city(request)
        queryset = super(CityAdminMixin, self).get_queryset(request)
        if self.city:
            queryset = queryset.filter(city=self.city)
        return queryset

    def save_model(self, request, obj, form, change):
        self.set_city(request)
        if self.city:
            obj.city = self.city
        obj.save()

admin.site.register(City, CityAdmin)
