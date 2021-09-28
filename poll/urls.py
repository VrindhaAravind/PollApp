from django.urls import path
from .views import index,create_poll,list_questions,vote,poll_result


urlpatterns=[
    path("home",index,name='home'),
    path("create_poll",create_poll,name="create"),
    path("polls",list_questions,name="listQuestions"),
    path("vote/<int:id>",vote,name="vote"),
    path("poll_result/<int:id>",poll_result,name="results")
]