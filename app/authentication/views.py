from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import FinappUserSerializer, User


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = FinappUserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    #def get_permissions(self):
    #    if self.action in ['create']:
    #        return [AllowAny()]
    #    return [IsAuthenticated()]

    #def get_object(self):
    #    return self.request.user

    def create(self, request):
        data = request.data.copy()
        data['email'] = data.get('email', '').lower()

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.validated_data,
            status=status.HTTP_201_CREATED
        )

    #def partial_update(self, request):
    #    data = request.data.copy()
    #    data['email'] = data.get('email', '').lower()

    #    serializer = self.get_serializer(
    #        self.get_object(),
    #        data=data,
    #        partial=True
    #    )
    #    serializer.is_valid(raise_exception=True)
    #    serializer.save()
    #    return Response(
    #        serializer.data,
    #        status=status.HTTP_200_OK
    #    )
