from rest_framework import serializers
from add_tags.models import Tags

class Tags_Serializers(serializers.ModelSerializer):
    class Meta:
        model=Tags
        #fields=['tag_name']
        fields=('__all__')