from rest_framework import serializers
from .models import Registration, Course

class CourseSeraializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"
        
class RegistrationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = "__all__"