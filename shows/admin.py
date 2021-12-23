from django.contrib import admin


from .models import Shows

class ShowsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'watched', 'date_aired')


admin.site.register(Shows, ShowsAdmin)

