from rest_framework.response import Response
from rest_framework.decorators import api_view
from blog.models import Post 
from .serializers import PostSerializer

@api_view(['GET'])
def getData(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addItem(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)