from django.contrib import admin
from football.models import Club, Player, Match


class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'foundation_date')
    search_fields = ('name',)


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'gender', 'club')
    list_filter = ('club',)
    search_fields = ('first_name', 'last_name')


class MatchAdmin(admin.ModelAdmin):
    list_display = ('city', 'date')
    filter_horizontal = ('players',)
    search_fields = ('city',)


# Register your models here.
admin.site.register(Club, ClubAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Match, MatchAdmin)
