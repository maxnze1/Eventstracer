from django.contrib import admin, messages
from django.utils.safestring import mark_safe
from ticketing.models import EventTicket
from admin_csv import CSVMixin
# Register your models here.


class EventTicketAdmin(CSVMixin, admin.ModelAdmin):
    list_display = ('title', 'user', 'ticket_id', 'ticket_form')
    """
    csv_fields = ('company_name', 'type_of_business', 'company_sector', 'years_business', 'contact_person',
                  'company_person_designation', 'phone_number', 'email', 'website', 'description',
                  'date_incorporation', 'contact_person2', 'employed_person', 'annual_revenue',
                  'business_projection', 'challenges', 'outlets', 'improve_business', 'sme_scores',)
    """

    def ticket_form(self, obj):
        if obj.ticket:
            return mark_safe("<a target='_blank' href='{}'>Download <img width='20px' src='/static/img/logos/pdf-icon.png' ></a>".format(obj.ticket.url))
        else:
            return mark_safe("<a target='_blank' disabled href='#'>Error <img width='20px' src='/static/img/logos/close-icon.png' ></a>")


admin.site.register(EventTicket, EventTicketAdmin)
