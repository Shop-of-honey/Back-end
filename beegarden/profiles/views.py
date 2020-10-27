from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank
from rest_framework import mixins, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from profiles.models import Product, User
from profiles.serializer import ProductSerializer, UserSerializer


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


class ProductsViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    """
    ViewSet to manage sections
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)