from rest_framework import serializers
from .models import Article, SavedArticle
from django.contrib.auth.models import User



class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
    def validate(self, attrs):
        user = User.objects.filter(username=data['username']).first()
        if user and user.check_password(data['password'].first()):
            return user
        raise serializers.ValidationError("Unable to log in with provided credentials.")
    
class SavedArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedArticle
        fields = ['id', 'title', 'link', 'category', 'image', 'video', 'publisher_logo', 'lastmod']

    lastmod = serializers.DateTimeField(source='article.lastmod', default=None)
