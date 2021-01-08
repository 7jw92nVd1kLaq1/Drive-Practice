"""driveit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact', views.foot, name="contact"),
    path('test', views.ready_for_test, name="first_test_ready"),
    path('test/ovrtest', views.gen_test, name="first_test"),
    path('subtest', views.ready_for_visual_test, name="visual_test_ready"),
    path('subtest/ovrtest', views.gen_visual_test, name="visual_test"),
    path('result', views.result, name="result"),
    path('result/review', views.display_rights_wrongs, name="review_answers")
]


