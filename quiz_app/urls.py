from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.api_route),
    url(r'^login_user', views.login_user),
    url(r'^updates_since/(?P<epoch_time>[+\d]+)', views.get_updates_since),
    url(r'^all_questions', views.get_all_questions),
    url(r'^question/(?P<question_id>[+\d]+)$', views.get_question),
    url(r'^add_question_with_answers', views.post_question),
    url(r'^delete_question', views.delete_question),
    url(r'^answer/(?P<answer_id>[+\d]+)$', views.get_answer),
    url(r'^user/(?P<username>[+\w]+)$', views.get_user),
    url(r'^save_high_score', views.save_high_score),
]
