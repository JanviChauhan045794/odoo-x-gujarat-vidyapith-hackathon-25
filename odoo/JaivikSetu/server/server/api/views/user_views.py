from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from ..models import User
from ..serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        users = self.get_queryset()
        serializer = self.get_serializer(users, many=True)
        return Response({
            "status": "success",
            "data": serializer.data
        })

    def retrieve(self, request, pk=None):
        user = self.get_queryset().filter(pk=pk).first()
        if user:
            serializer = self.get_serializer(user)
            return Response({
                "status": "success",
                "data": serializer.data
            })
        return Response({
            "status": "error",
            "data": {"error": "user not found"}
        }, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            "status": "error",
            "data": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        return Response({
            "status": "error",
            "data": {"error": "PUT method not allowed"}
        }, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, *args, **kwargs):
        return Response({
            "status": "error",
            "data": {"error": "DELETE method not allowed"}
        }, status=status.HTTP_405_METHOD_NOT_ALLOWED)
