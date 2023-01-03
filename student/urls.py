from django.urls import path
from .views import StudList, StudDetails

urlpatterns=[
     path('studList/',StudList.as_view()),
     path('studDetails/<int:pk>',StudDetails.as_view())
]