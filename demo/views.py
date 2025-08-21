from rest_framework import viewsets,status
from rest_framework.response import Response

from .serializers import PaperSerializer, UserSerializer
from .models import Paper
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    @action(detail=False, methods=['POST'], permission_classes=[IsAuthenticated])
    def signout(self,request):
        user = request.user
        user.delete()
        return Response({"message": "Logged out successfully"})

class PaperViewSet(viewsets.ModelViewSet):
    queryset = Paper.objects.all()
    serializer_class = PaperSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('subject', 'examination', 'course')

   

    @action(detail=False, methods=['get'])
    def filter(self, request):
        subjects = Paper.objects.values_list('subject', flat=True).distinct()
        examinations = Paper.objects.values_list('examination', flat=True).distinct()
        courses = Paper.objects.values_list('course', flat=True).distinct()
        return Response({'subjects': list(subjects), 'examinations': list(examinations), 'course': list(courses)})









