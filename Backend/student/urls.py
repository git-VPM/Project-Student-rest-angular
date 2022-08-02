from django.urls import path
from .views import getdist, getprofile, getprofile_by_id, get_by_id


urlpatterns = [
    path('', getprofile.as_view()),
    path('dist', getdist.as_view(), name='dist'),
    path('<str:key>', getprofile_by_id.as_view(), name="student"),
    path('dist/<str:key>', get_by_id.as_view(), name="id"),
]


# from django.urls import re_path
# from student import views

# urlpatterns = [
#     re_path(r'^api/student$', getprofile.as_view()),
#     re_path(r'^api/student/(?P<pk>[0-9]+)$',
#             getprofile_by_id.as_view(), name="student")
# ]
