from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^questions', views.get_all_questions),
    url(r'^user/(?P<username>[+\w]+)$', views.get_user)
]
