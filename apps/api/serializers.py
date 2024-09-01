from rest_framework import serializers
from apps.admission.models import Course
from apps.admission.models import Intake


class IntakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intake
        fields = ['id', 'start_date', 'end_date']  


class CourseSerializer(serializers.ModelSerializer):
    # Include respective intakes
    intakes = IntakeSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ["name", "intakes"]
