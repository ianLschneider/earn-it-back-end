"""
URL configuration for earnitproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from earnit.views import EarnerViewSet, TaskViewSet, EarnerTasks, RewardViewSet
#, EarnerRewards

router = routers.DefaultRouter()
router.register(r'earners', EarnerViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'rewards', RewardViewSet)


urlpatterns = [
    path('<int:pk>/tasks/', EarnerTasks.as_view()),
    # path('<int:pk>/rewards/', EarnerRewards.as_view()),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
