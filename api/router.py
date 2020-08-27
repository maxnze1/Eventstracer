from api.viewsets import (
    EventsViewSet,
    EventCategoryViewSet,
    UserViewSet,
    ProfileViewSet,
    NewsCategoryViewSet,
    NewsViewSet,
    DirectoryCategoryViewSet,
    DirectoryViewSet,
    SmeRegistrationViewSet
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register('events/4f0e28e525736e2582f23a4828a197df856b0582', EventsViewSet)
router.register('events-category/4f0e28e525736e2582f23a4828a197df856b0582', EventCategoryViewSet)
router.register('user', UserViewSet)
router.register('profile/4f0e28e525736e2582f23a4828a197df856b0582', ProfileViewSet)
router.register('news/4f0e28e525736e2582f23a4828a197df856b0582', NewsViewSet)
router.register('news-cateogry/4f0e28e525736e2582f23a4828a197df856b0582', NewsCategoryViewSet)
router.register('directory/4f0e28e525736e2582f23a4828a197df856b0582', DirectoryViewSet)
router.register('directory-category/4f0e28e525736e2582f23a4828a197df856b0582', DirectoryCategoryViewSet)
router.register('sme-registration/4f0e28e525736e2582f23a4828a197df856b0582', SmeRegistrationViewSet)
