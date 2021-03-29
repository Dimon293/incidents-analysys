from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Consiquence)
admin.site.register(Participant)
admin.site.register(Participantaction)
admin.site.register(Participantcategory)
admin.site.register(Violation)
admin.site.register(ParticipantViolationImmediate)
admin.site.register(ParticipantViolationAssociate)
