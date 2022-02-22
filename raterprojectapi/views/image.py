from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.forms import ValidationError
from django.http import HttpResponseServerError
from django.core.files.base import ContentFile
import uuid
import base64
from raterprojectapi.models import GamePicture

class ImageView(ViewSet):
    def list(self, request):
        image = GamePicture.objects.all()
        gameid = request.query_params.get("game", None)
        if gameid is not None:
            reviews = reviews.filter(game=gameid)
        serializer = ImageSerializer(image, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        try:
            format, imgstr = request.data["game_image"].split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name=f'{request.data["game"]}-{uuid.uuid4()}.{ext}')
            serializer = CreateImageSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(action_pic=data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GamePicture
        fields = ("id","game", "action_pic")
        
        
class CreateImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GamePicture
        fields = ("game", "action_pic")
        