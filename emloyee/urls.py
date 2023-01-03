from django.urls import path
from .views import empList, empDetails

urlpatterns=[
     path('empList/',empList.as_view()),
     path('empDetails/<int:pk>',empDetails.as_view())
]