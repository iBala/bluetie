from django.urls import path, include


from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.auth import views as auth_views



urlpatterns = [
    # path('', views.index, name='index'),
    # path('question/', views.QuestionList.as_view()),
    # path('exam/', login_required(views.ExamList.as_view())),
    # path('answer/', views.AnswerList.as_view()),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('', include(router.urls, namespace='users'))
    # path('myexam/', login_required(exams.GetMyExamList.as_view()), name='My Exams'),
]

urlpatterns = format_suffix_patterns(urlpatterns)