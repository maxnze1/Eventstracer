from rest_framework import serializers
from event.models import EventPage, Category as EventCategory
from news.models import News, Category as NewsCategory
from directory.models import Directory, Category as DirectoryCategory
from registrations.models import SMERegistration
from sme.models import SmeCircuit, Category as SMECategory
from users.models import Profile, CustomUser


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email')


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'profile_image')


class EventCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventCategory
        fields = ('name',)


class EventsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventPage
        fields = ('category', 'title', 'slug', 'location',
                  'description', 'image', 'address', 'start_date', 'end_date', 'organizer', 'contact_person',
                  'has_ticket', 'created', 'author', 'status',)


class NewsCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NewsCategory
        fields = ('name',)


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = News
        fields = ('category', 'title', 'slug', 'body',
                  'author', 'image', 'created', 'status',)


class DirectoryCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DirectoryCategory
        fields = ('name',)


class DirectorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Directory
        fields = ('category', 'business_name', 'slug', 'track_record',
                  'email', 'phone_number', 'business_address', 'state', 'city', 'company_logo', 'product_image', 'created')


class SMESerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = SMERegistration
        fields = ('company_name', 'type_of_business', 'company_address', 'company_sector',
                  'years_business', 'contact_person', 'company_person_designation',
                  'phone_number', 'description', 'email', 'website', 'date_incorporation',
                  'contact_person2', 'employed_person', 'annual_revenue', 'business_projection',
                  'challenges', 'outlets', 'improve_business', 'payment', 'payment_reference',
                  'invite', 'photo', 'supporting_document', 'user')
