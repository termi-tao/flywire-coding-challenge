from rest_framework.views import APIView
from .serializers import CourseSerializer
from ..admission.models import Course
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.request import Request


class ListCourses(APIView):
    # TODO: May use a custom authenticator to enable authentication throttling and such
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request: Request) -> Response:
        # TODO: Integrate pagination when model expands
        queryset = Course.objects.all()
        serializer = CourseSerializer(queryset, many=True)
        return Response(serializer.data)
