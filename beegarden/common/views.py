from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes([])
def health_check(request):
    return Response('Service is available')
