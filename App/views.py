from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.serializers import Serializer
from .serializers import UserSerializer
from .models import User
from rest_framework import permissions

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return super().perform_create(serializer)
        #serializer.save(user=self.request.user)