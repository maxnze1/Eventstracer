from elasticsearch_dsl import Index
from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import EventPage


events = Index('events')
events.settings(
    number_of_shards=1,
    number_of_replicas=0
)


@registry.register_document
@events.document
class EventDocument(Document):
    class Django:
        model = EventPage
        fields = ['image', 'title', 'location', 'address']
