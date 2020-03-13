from django.urls import path
from . import views

urlpatterns = [
    # 127.0.0.1:8000/ 로 들어왔을 때 views.post_list를 보여주기.
    # name= 부분은 url에 이름을 붙인 것.
    path('', views.post_list, name='post_list'),
]