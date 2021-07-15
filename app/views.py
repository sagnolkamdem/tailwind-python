from rest_framework import generics, mixins
# Create your views here.
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# from common.authentication import JWTAuthentication
from core.models import Announce, Comment, Logement
from .serializers import AnnounceSerializer, CommentSerializer,  LogementSerializer, VisitSerializer


class AnnounceGenericAPIView(
    generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin,
    mixins.UpdateModelMixin, mixins.DestroyModelMixin
):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = Announce.objects.filter(available=True, validated=True).order_by('-id')
    serializer_class = AnnounceSerializer

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request, pk)

        return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, pk=None):
        return self.partial_update(request, pk)

    def delete(self, request, pk=None):
        return self.destroy(request, pk)


class CommentGenericAPIView(generics.GenericAPIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        comments = Comment.objects.filter(announce_id=pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        return self.create(request)


class LogementGenericAPIView(
    generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin,
    mixins.UpdateModelMixin, mixins.DestroyModelMixin
):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    serializer_class = LogementSerializer

    def get(self, request, pk=None):
        logement = Logement.objects.filter(announce_id=pk)
        serializer = LogementSerializer(logement, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        return self.create(request)

    def put(self, request, pk):
        return self.partial_update(request, pk)


class VisitGenericAPIView(
    generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin,
    mixins.UpdateModelMixin, mixins.DestroyModelMixin
):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    serializer_class = VisitSerializer

    def post(self, request):
        return self.create(request)

    def put(self, request, pk):
        return self.partial_update(request, pk)
