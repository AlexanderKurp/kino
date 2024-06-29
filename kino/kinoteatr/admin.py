from django.contrib import admin
from .models import Genre, Director, Actor, Session, Ticket, Movie

admin.site.register(Genre)
admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Session)
admin.site.register(Ticket)
admin.site.register(Movie)
