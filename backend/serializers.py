from rest_framework import serializers
from .models import productModel


class productSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = productModel
        fields = ('id','title','description','image')

