from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api_service.serializers import StudentSerializer, ProfessorSerializer, BranchSerializer, CollegeSerializer, \
    SubjectSerializer, SemesterSerializer, FeedbackToProfessorsSerializer, FeedbackToProfessorsSerializerWithoutNest
from class_room.models import Subject
from feedback_to_professors.models import FeedbackToProfessors
from metadata.models import Branch, College, Semester
from users.models import Professor, Student


@api_view(['POST'])
def post_feedback(request, *args, **kwargs):
    print(type(request.data), request.data)
    data = request.data
    FeedbackToProfessors(
        semester=Semester.objects.get(semester_id=data["semester"]),
        subject=Subject.objects.get(subject_id=data["subject"]),
        rating=data["rating"],
        message=data["message"],
        professor=Professor.objects.get(professor_id=data["professor_id"]),
        student=Student.objects.get(student_id=data["student_id"])
    ).save()
    return Response([], status=status.HTTP_200_OK)


@api_view(['POST'])
def add_student(request, *args, **kwargs):
    try:
        print(type(request.data), request.data)
        data = request.data

        Student(
            email=data["email"],
            student_id=data["student_id"],
            student_name=data["student_name"],
            phone_number=data["phone_number"],
            password=data["password"],
            branch_id=Branch.objects.get(branch_id=data["branch_id"]),
            college_id=College.objects.get(college_id=data["college_id"])
        ).save()
        return Response([], status=status.HTTP_200_OK)
    except KeyError as key_error:
        return Response({"error_message": str(key_error)}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as exception:
        return Response({"error_message": str(exception)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT'])
def update_student(request, *args, **kwargs):
    """

    Payload 1:

    {
        "email_id": "s@gmail.com",
        "is_fingerprint_enrolled": true
    }

    Payload 2:

    {
        "user_id": "s@gmail.com",
        "is_fingerprint_deleted": true
    }

    Payload 3:

    {
        "user_id": "s@gmail.com",
        "is_fingerprint_need_re_enrolled": true
    }

    """
    try:
        print(type(request.data), request.data)
        data = request.data

        user_id = data.get("user_id")
        email = data.get("email_id")
        if user_id:
            student = Student.objects.get(student_id=user_id)
        elif email:
            student = Student.objects.get(email=email)
        else:
            return Response([], status=status.HTTP_400_BAD_REQUEST)

        is_fingerprint_enrolled = data.get("is_fingerprint_enrolled")
        is_fingerprint_deleted = data.get("is_fingerprint_deleted")
        is_fingerprint_need_re_enrolled = data.get("is_fingerprint_need_re_enrolled")
        if is_fingerprint_enrolled is not None and is_fingerprint_enrolled:
            student.is_fingerprint_enrolled = True
            student.is_fingerprint_deleted = False
            student.is_fingerprint_need_re_enrolled = False
        elif is_fingerprint_deleted is not None and is_fingerprint_deleted:
            student.is_fingerprint_enrolled = True
            student.is_fingerprint_deleted = True
            student.is_fingerprint_need_re_enrolled = False
        elif is_fingerprint_need_re_enrolled is not None and is_fingerprint_need_re_enrolled:
            student.is_fingerprint_enrolled = False
            student.is_fingerprint_deleted = True
            student.is_fingerprint_need_re_enrolled = True

        student.save()

        return Response([], status=status.HTTP_200_OK)
    except KeyError as key_error:
        print(key_error)
        return Response({"error_message": str(key_error)}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as exception:
        print(exception)
        return Response({"error_message": str(exception)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def get_list_of_feedbacks_for_professor(request, professor_id):
    professor = Professor.objects.get(professor_id=professor_id)
    fps = FeedbackToProfessors.objects.filter(professor=professor)
    return Response(FeedbackToProfessorsSerializerWithoutNest(fps, many=True).data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_list_of_feedbacks_from_student(request, student_id):
    student = Student.objects.get(student_id=student_id)
    fps = FeedbackToProfessors.objects.filter(student=student)
    return Response(FeedbackToProfessorsSerializer(fps, many=True).data, status=status.HTTP_200_OK)


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
    try:
        if user_type.lower() == "professor":
            professor = Professor.objects.get(email=email_id)
            return Response(ProfessorSerializer(professor).data, status=status.HTTP_200_OK)
        elif user_type.lower() == "student":
            student = Student.objects.get(email=email_id)
            return Response(StudentSerializer(student).data, status=status.HTTP_200_OK)
        else:
            return Response({}, status=status.HTTP_404_NOT_FOUND)
    except ObjectDoesNotExist as does_not_exist:
        return Response({}, status=status.HTTP_404_NOT_FOUND)


def validate_user(request, *args, **kwargs):
    pass


@api_view(['GET'])
def get_all_professors(request):
    professor = Professor.objects.all()
    return Response(ProfessorSerializer(professor, many=True).data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_all_branch(request):
    professor = Branch.objects.all()
    return Response(BranchSerializer(professor, many=True).data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_all_college(request):
    professor = College.objects.all()
    return Response(CollegeSerializer(professor, many=True).data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_all_subjects(request):
    semester_id = request.GET.get('semester_id')
    subject_id = request.GET.get('subject_id')

    if semester_id or subject_id:
        filter_data = {}
        if semester_id:
            filter_data["semester_id"] = semester_id
        if subject_id:
            filter_data["subject_id"] = subject_id
        subject = Subject.objects.filter(**filter_data)
    else:
        subject = Subject.objects.all()
    return Response(SubjectSerializer(subject, many=True).data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_all_semester(request):
    print(request.GET.get('x'))
    semester = Semester.objects.all()
    return Response(SemesterSerializer(semester, many=True).data, status=status.HTTP_200_OK)
