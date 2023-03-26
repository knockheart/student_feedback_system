from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api_service.serializers import StudentSerializer, ProfessorSerializer
from feedback_to_professors.models import FeedbackToProfessors
from users.models import Professor, Student


@api_view(['POST'])
def post_feedback(request, *args, **kwargs):
    print(type(request.data), request.data)
    data = request.data
    FeedbackToProfessors(
        semester=data["semester"],
        subject=data["subject"],
        rating=data["rating"],
        message=data["message"],
        professor=Professor.objects.get(professor_id=data["professor_id"]),
        student=Student.objects.get(student_id=data["student_id"])
    ).save()
    return Response([], status=status.HTTP_200_OK)


@api_view(['GET'])
def get_list_of_feedbacks_for_professor(request, professor_id):
    professor = Professor.objects.get(professor_id=professor_id)
    fps = FeedbackToProfessors.objects.filter(professor=professor).values()
    return Response(fps, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_list_of_feedbacks_from_student(request, student_id):
    student = Student.objects.get(student_id=student_id)
    fps = FeedbackToProfessors.objects.filter(student=student).values()
    return Response(fps, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_user_profile(request, user_type, user_id):
    if user_type.lower() == "professor":
        professor = Professor.objects.get(professor_id=user_id)
        return Response(ProfessorSerializer(professor).data, status=status.HTTP_200_OK)
    elif user_type.lower() == "student":
        student = Student.objects.get(student_id=user_id)
        return Response(StudentSerializer(student).data, status=status.HTTP_200_OK)
    else:
        return Response([], status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_user_profile_by_email(request, user_type, email_id):
    if user_type.lower() == "professor":
        professor = Professor.objects.get(email=email_id)
        return Response(ProfessorSerializer(professor).data, status=status.HTTP_200_OK)
    elif user_type.lower() == "student":
        student = Student.objects.get(email=email_id)
        return Response(StudentSerializer(student).data, status=status.HTTP_200_OK)
    else:
        return Response([], status=status.HTTP_404_NOT_FOUND)


def validate_user(request, *args, **kwargs):
    pass


@api_view(['GET'])
def get_all_professors(request):
    professor = Professor.objects.all()
    return Response(ProfessorSerializer(professor, many=True).data, status=status.HTTP_200_OK)
