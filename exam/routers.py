from exam.views import QuestionList
from rest_framework import routers

# router = routers.SimpleRouter(trailing_slash=False)
router = routers.DefaultRouter()
router.register('',QuestionList, base_name='api')