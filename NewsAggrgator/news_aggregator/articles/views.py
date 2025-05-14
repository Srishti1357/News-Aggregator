from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status, generics, filters
from django.contrib.auth.models import User
from .models import Article
from .serializers import ArticleSerializer
from django.contrib.auth import authenticate
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ArticleFilter
from rest_framework_simplejwt.exceptions import TokenError

class RegisterView(APIView):
    def post(self, request):
        """
        Handles user registration. Expects JSON payload:
        {
            "username": "user1",
            "password": "password123"
        }
        """
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({"error": "User with this username already exists"}, status=status.HTTP_400_BAD_REQUEST)

        # Create the user
        User.objects.create_user(username=username, password=password)
        return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request):
        """
        Handles user login. Expects JSON payload:
        {
            "username": "user1",
            "password": "password123"
        }
        Returns JWT tokens on success.
        """
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Generate JWT tokens
            refresh = RefreshToken.for_user(user)
            return Response({
                "message": "Login successful",
                "access": str(refresh.access_token),
                "refresh": str(refresh),
                "username": username
            }, status=status.HTTP_200_OK)

        return Response({"error": "Invalid username or password"}, status=status.HTTP_401_UNAUTHORIZED)



# class ArticleListView(generics.ListAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
#     filterset_class = ArticleFilter
#     search_fields = ['title']
#     ordering_fields = ['created_at', 'category']
#     permission_classes = [IsAuthenticated]


from .pagination import CustomPagination  # Import your custom pagination class
class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_class = ArticleFilter
    search_fields = ['title']
    ordering_fields = ['created_at', 'category']
    permission_classes = [IsAuthenticated]

    # Add pagination
    pagination_class = CustomPagination  # Use page number pagination
    

class ArticleFilteredNoPaginationView(generics.ListAPIView):
    serializer_class = ArticleSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = ArticleFilter
    search_fields = ['title']
    permission_classes = [IsAuthenticated]
    pagination_class = None  # 👈 disables pagination

    queryset = Article.objects.all()  # ✅ FIXED


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        Logs out the user by blacklisting their refresh token.
        Expects JSON payload:
        {
            "refresh": "refresh_token"
        }
        """
        refresh_token = request.data.get("refresh")
        if not refresh_token:
            return Response({"error": "Refresh token is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()  # Blacklist the refresh token
            return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)
        except TokenError:
            return Response({"error": "Invalid or expired token"}, status=status.HTTP_400_BAD_REQUEST)
        



from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Article, SavedArticle

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def save_article(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
        saved_article, created = SavedArticle.objects.get_or_create(user=request.user, article=article)
        if created:
            return Response({'message': 'Article saved successfully!'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Article already saved.'}, status=status.HTTP_200_OK)
    except Article.DoesNotExist:
        return Response({'error': 'Article not found.'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_saved_articles(request):
    saved_articles = SavedArticle.objects.filter(user=request.user).select_related('article')
    data = [
        {
            'id': saved.article.id,
            'title': saved.article.title,
            'link': saved.article.link,
            'category': saved.article.category,
            'date': saved.article.date,
            'publisher_logo': saved.article.publisher_logo,
            'image': saved.article.image,
            'video': saved.article.video,
        }
        for saved in saved_articles
    ]
    return Response(data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_saved_article(request, article_id):
    try:
        saved_article = SavedArticle.objects.get(user=request.user, article__id=article_id)
        saved_article.delete()
        return Response({'message': 'Article removed from saved list.'}, status=status.HTTP_200_OK)
    except SavedArticle.DoesNotExist:
        return Response({'error': 'Saved article not found.'}, status=status.HTTP_404_NOT_FOUND)
