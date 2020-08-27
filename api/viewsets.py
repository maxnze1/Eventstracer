from rest_framework import viewsets
from .serializers import(
    EventsSerializer,
    EventCategorySerializer,
    UserSerializer,
    ProfileSerializer,
    NewsCategorySerializer,
    NewsSerializer,
    DirectoryCategorySerializer,
    DirectorySerializer,
    SMESerializer
)

from event.models import EventPage, Category as EventCategory
from news.models import News, Category as NewsCategory
from directory.models import Directory, Category as DirectoryCategory
from registrations.models import SMERegistration
from sme.models import SmeCircuit, Category as SMECategory
from users.models import Profile, CustomUser
from rest_framework.permissions import IsAuthenticated


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    #permission_classes = (IsAuthenticated,)


class EventCategoryViewSet(viewsets.ModelViewSet):
    queryset = EventCategory.objects.all()
    serializer_class = EventCategorySerializer
    #permission_classes = (IsAuthenticated,)


class EventsViewSet(viewsets.ModelViewSet):
    queryset = EventPage.published.all()
    serializer_class = EventsSerializer
    #permission_classes = (IsAuthenticated,)


class NewsCategoryViewSet(viewsets.ModelViewSet):
    queryset = NewsCategory.objects.all()
    serializer_class = NewsCategorySerializer
    #permission_classes = (IsAuthenticated,)


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    #permission_classes = (IsAuthenticated,)


class DirectoryCategoryViewSet(viewsets.ModelViewSet):
    queryset = DirectoryCategory.objects.all()
    serializer_class = DirectoryCategorySerializer
    #permission_classes = (IsAuthenticated,)


class DirectoryViewSet(viewsets.ModelViewSet):
    queryset = Directory.objects.all()
    serializer_class = DirectorySerializer
    #permission_classes = (IsAuthenticated,)


class SmeRegistrationViewSet(viewsets.ModelViewSet):
    queryset = SMERegistration.objects.all()
    serializer_class = SMESerializer
    #permission_classes = (IsAuthenticated,)
