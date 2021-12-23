from django.contrib import admin


from .models import Show

class ShowAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'watched', 'date_aired', 'image')


admin.site.register(Show, ShowAdmin)

