from django.urls import path
from .views import directory_detail, CreateDirectoryView, DirectoryView, DirectoryCategoryView, UpdateViewDirectory

app_name = 'directory'


urlpatterns = [
    path('', DirectoryView.as_view(), name='directory'),
    path('<int:pk>/', DirectoryCategoryView.as_view(),
         name='directory_list_by_cat'),
    path('<id>/<slug>/', directory_detail, name='directory-detail'),
    path('directory', CreateDirectoryView.as_view(), name='create'),
    path('<id>/<slug>/update',
         UpdateViewDirectory.as_view(), name='update'),
]
