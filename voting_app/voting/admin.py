# voting/admin.py

from django.contrib import admin
from .models import Voter, Position, Candidate, Vote

class VoterAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number') 

class PositionAdmin(admin.ModelAdmin):
    list_display = ('name', 'max_voters', 'priority')
    search_fields = ('name',)

class CandidateAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position')
    search_fields = ('full_name', 'position__name')

class VoteAdmin(admin.ModelAdmin):
    list_display = ('voter', 'candidate')
    search_fields = ('voter__user__username', 'candidate__full_name')

admin.site.register(Voter, VoterAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Vote, VoteAdmin)

