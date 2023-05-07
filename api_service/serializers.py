from rest_framework import serializers

from class_room.models import Subject
from feedback_to_professors.models import FeedbackToProfessors
from metadata.models import Branch, College, Semester
from users.models import Student, Professor


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'


class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):
    professor_id = ProfessorSerializer(many=False, read_only=True)

    # professor_id = serializers.StringRelatedField(many=False)

    class Meta:
        model = Subject
        # fields = [
        #     'subject_id', 'subject_name', 'description', 'branch_id', 'semester_id', 'college_id',
        #     'professor_id',
        # ]
        fields = "__all__"


class SubjectSerializerWithoutNest(serializers.ModelSerializer):
    class Meta:
        model = Subject

        fields = "__all__"


class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = '__all__'


class FeedbackToProfessorsSerializer(serializers.ModelSerializer):
    # professor = ProfessorSerializer(many=False, read_only=True)
    subject = SubjectSerializer(many=False, read_only=True)

    class Meta:
        model = FeedbackToProfessors
        fields = '__all__'


class FeedbackToProfessorsSerializerWithoutNest(serializers.ModelSerializer):
    subject = SubjectSerializerWithoutNest(many=False, read_only=True)

    class Meta:
        model = FeedbackToProfessors
        fields = '__all__'
