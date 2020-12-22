from allauth.account.models import EmailConfirmationHMAC
from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse_lazy
from rest_framework import mixins, viewsets, permissions, decorators, generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


from profiles.models import Product, User
from profiles.serializer import UserSerializer, ProductSerializer


class UserListView(APIView):

    @api_view(['GET', 'POST'])
    def get(self, request, search_string=None):
        """
        Returns profiles which contain searching string
        :param request:
        :param search_string:
        :return:
        """
        query = SearchQuery(search_string)

        username_vector = SearchVector('username', weight='A')
        first_name_vector = SearchVector('first_name', weight='B')
        last_name_vector = SearchVector('last_name', weight='B')
        email_vector = SearchVector('email', weight='B')
        vectors = username_vector + first_name_vector + last_name_vector + email_vector
        qs = User.objects
        qs = qs.annotate(search=vectors).filter(search=query)
        qs = qs.annotate(rank=SearchRank(vectors, query)).order_by('-rank')
        print(qs)
        return Response(UserSerializer(qs, many=True).data)


class ProductListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, search_string=None):
        """
        Returns profiles which contain searching string
        :param request:
        :param search_string:
        :return:
        """
        query = SearchQuery(search_string)

        name_vector = SearchVector('name', weight='A')
        description_vector = SearchVector('description', weight='B')
        vectors = name_vector + description_vector
        qs = Product.objects
        qs = qs.annotate(search=vectors).filter(search=query)
        qs = qs.annotate(rank=SearchRank(vectors, query)).order_by('-rank')
        print(qs)
        return Response(ProductSerializer(qs, many=True).data)

'''class UsersViewSet(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
'''

'''class ProductsDetail(APIView):

    @api_view(['GET'])
    @permission_classes([AllowAny])
    def get_object(self, id):
        try:
            return Product.objects.get(id=id)
        except Product.DoesNotExist:
            raise Http404

    @api_view(['DELETE'])
    @permission_classes([IsAuthenticated])
    def delete(self, request, id):
        product = self.get_object(id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @api_view(['PUT'])
    @permission_classes([IsAuthenticated])
    def put(self, request, id):
        product = self.get_object(id)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductList(APIView):
    @api_view(['GET'])
    @permission_classes([AllowAny])
    def get(self, request):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    @api_view(['POST'])
    @permission_classes([IsAuthenticated])
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)'''


class UserCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserList(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDelete(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProductCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductList(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdate(generics.RetrieveUpdateAPIView):
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDelete(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


def confirm_email(request, key):
    email_confirmation = EmailConfirmationHMAC.from_key(key)
    if email_confirmation:
        email_confirmation.confirm(request)
    return HttpResponseRedirect(reverse_lazy('api'))


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def is_authenticated(request):
    if request.user.is_authenticated():
        data = User.objects.filter(id=request.user.id)
        return Response(data=data)
    else:
        return HttpResponse(status=401)
