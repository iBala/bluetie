from exam.views import GetQuestionAPI, GetExamAPI, GetAnswerAPI
from rest_framework import routers
from users.views import ProfileAPI

# router = routers.SimpleRouter(trailing_slash=False)
router = routers.DefaultRouter()
router.register('',GetQuestionAPI, base_name='api')
router.register('',GetExamAPI, base_name='api')
router.register('',GetAnswerAPI, base_name='api')
router.register('',ProfileAPI, base_name='api')