from django.contrib import admin, messages
from django.utils.safestring import mark_safe
from registrations.models import SMERegistration, SMEScore, Invitation
from admin_csv import CSVMixin
from registrations import utils
# Register your models here.


class SMEAdmin(CSVMixin, admin.ModelAdmin):
    list_display = ('company_name', 'type_of_business',
                    'company_sector', 'sme_scores', 'circuit', 'sme_form', 'invite_button',)
    csv_fields = ('company_name', 'type_of_business', 'company_sector', 'years_business', 'contact_person',
                  'company_person_designation', 'phone_number', 'email', 'website', 'description',
                  'date_incorporation', 'contact_person2', 'employed_person', 'annual_revenue',
                  'business_projection', 'challenges', 'outlets', 'improve_business', 'sme_scores',)
    readonly_fields = ('sme_scores',)

    actions = ['make_invitation']

    def invite_button(self, obj):
        if not obj.invite:
            return mark_safe("<a href='#'>Invite <img width='20px' src='/static/img/logos/invite-icon.png' ></a>")
        else:
            return mark_safe("<a disabled href='#'>Invitation Sent <img width='20px' src='/static/img/logos/invite-icon.png' ></a>")

    def sme_form(self, obj):
        if obj.pdf:
            return mark_safe("<a target='_blank' href='{}'>Download <img width='20px' src='/static/img/logos/pdf-icon.png' ></a>".format(obj.pdf.url))
        else:
            return mark_safe("<a target='_blank' disabled href='#'>Error <img width='20px' src='/static/img/logos/close-icon.png' ></a>")

    def make_invitation(self, request, queryset):
        sme_score = SMEScore.objects.get(pk=1)
        obj = [x for x in queryset if x.sme_scores() >= int(
            sme_score.pass_mark) and x.invite in [False, None]]
        email_address = [x.email for x in obj]
        phone_number = [x.phone_number for x in obj]
        ids = [x.id for x in obj]
        if ids:
            try:
                invitation = Invitation.objects.get(pk=1)
                utils.send_out_invitation(
                    invitation.subject, invitation.message, email_address)
                queryset.filter(pk__in=ids).update(invite=True)
                self.message_user(request, "Invitation sent",
                                  level=messages.SUCCESS)
            except Exception as e:
                print(e)
                self.message_user(
                    request, "Error! Invitation not sent", level=messages.ERROR)
        else:
            self.message_user(
                request, "No valid options selected", level=messages.INFO)

    make_invitation.short_description = "Send invitation"


admin.site.register(SMERegistration, SMEAdmin)
admin.site.register(SMEScore)
admin.site.register(Invitation)
