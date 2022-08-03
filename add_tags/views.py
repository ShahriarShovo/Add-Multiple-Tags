from rest_framework.decorators import api_view
from add_tags.serializers import Tags_Serializers
from rest_framework.response import Response
from add_tags.models import Tags

# Create your views here.

@api_view(['GET'])
def retrive_tags(request):
    tags=Tags.objects.all()
    tag_serializers=Tags_Serializers(tags, many=True)
    return Response(tag_serializers.data)




@api_view(['POST'])
def add_tags(request):
    if request.method=='POST':
        tags=Tags_Serializers(data=request.data)
        if tags.is_valid():
            tags.save()
            return Response(tags.data)
        else:
            return Response(tags.errors)
    else:
        return None 
