from django.db import models
from event.models import EventPage
from django.conf import settings
from ticketing import utils
import os
from django.core.files.base import ContentFile
from datetime import datetime

# Create your models here.


class EventTicket(models.Model):
    PAYMENT_STATUS = (
        ('S', 'Success'),
        ('F', 'Failed'),
    )
    title = models.ForeignKey(EventPage, on_delete=models.SET_NULL, null=True)
    ticket_id = models.CharField(max_length=50)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    amount = models.IntegerField()
    payment_status = models.CharField(max_length=50, choices=PAYMENT_STATUS)
    ticket = models.FileField(upload_to="documents", blank=True, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)

    def save(self, *args, **kwargs):
        data = {'title': self.title.title, 'date': datetime.strftime(self.title.start_date, "%d/%m/%Y"),
                'time': datetime.strftime(self.title.start_date, "%I:%M%p"), 'address': self.title.address,
                'organizer': self.title.organizer, 'type': self.title.category.name, 'order_no': self. ticket_id, 'photo': self.title.image}
        get_temp_file = utils.save_pdf_ticket(data)
        form_content = ContentFile(get_temp_file.getvalue())
        if self._state.adding:
            self.ticket.save("Ticket_{}.pdf".format(
                self.pk), form_content, save=False)
        else:
            try:
                os.remove(self.ticket.path)
                self.ticket.save("Ticket_{}.pdf".format(
                    self.pk), form_content, save=False)
            except:
                self.ticket.save("Ticket_{}.pdf".format(
                    self.pk), form_content, save=False)
        super(EventTicket, self).save(*args, **kwargs)

    def __str__(self):
        return self.title.title
