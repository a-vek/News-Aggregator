# from users.userapi.serializers import UserSerializer
# from users.models import Profile
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = Profile.objects.all()
#     serializer_class = UserSerializer
#     authentication_classes = [SessionAuthentication]
#     permission_classes = [IsAuthenticated]
