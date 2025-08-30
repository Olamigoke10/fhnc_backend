from django.urls import path
from .views import CourseListview, RegistrationCreateView

urlpatterns = [
    path("courses/", CourseListview.as_view(), name="Course-list"),
    path("register/", RegistrationCreateView.as_view(), name="course-register")
    
]