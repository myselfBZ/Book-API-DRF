from rest_framework.serializers import ModelSerializer
from .models import Author, Book, Star, Comment
from rest_framework import serializers
class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = [
            'id'
            'name'
        ]


class BookSerialzer(ModelSerializer):
    #author = serializers.SerializerMethodField(read_only=True)
    avarage = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Book 
        fields = [
            'id',
            'title',
            'author',
            'is_available',
            'avarage'
        ]

    #def get_author(self, obj):
    #    return obj.author.name
    def get_avarage(self, obj):
        return obj.star.avarage

class StarSerializer(ModelSerializer):
    class Meta:
        model = Star
        fields=[
            'book',
            'number',
            'avarage'
        ]

class CommentSerializer(ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)
    book = serializers.SerializerMethodField(read_only=True)
    
    
    class Meta:
        model = Comment
        fields = [
            'content',
            'user',
            'book',
        ]
    
    def get_user(self, obj):
        return obj.user.user.username


    def get_book(self, obj):
        return obj.book.title  