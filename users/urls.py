from django.urls import path


from . import views
from . import exams
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # path('', views.index, name='index'),
    # path('author/', login_required(views.AuthorList.as_view())),
    # path('candidate/', login_required(views.CandidateList.as_view())),
    # path('question/', login_required(views.QuestionList.as_view())),
    # path('exam/', login_required(exams.GetAllExamList.as_view())),
    # path('answer/', login_required(views.AnswerList.as_view())),
    path('signup/', views.signup, name='signup'),
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('myexam/', login_required(exams.GetMyExamList.as_view()), name='My Exams'),

]

urlpatterns = format_suffix_patterns(urlpatterns)