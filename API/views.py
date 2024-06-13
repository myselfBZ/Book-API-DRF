from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from .models import Book, Comment
from .serializers import BookSerialzer, CommentSerializer
from .models import Star
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
def get_books(request):
    books = Book.objects.all()
    if books.exists():
        
        serialized_data = BookSerialzer(books, many=True)
        

        return Response(serialized_data.data)
    
    else:
        return Response({"message":"Books were not found."})


@api_view(["PUT", "GET"])
def borrow_book(request, pk):
    book = Book.objects.get(id=pk)

    if request.method == "PUT":
            
        
        serialized = BookSerialzer(book, data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response({"message":"You are borrowing the book now."})
        return Response({"message":"You messed up"})
    else:
        serialized = BookSerialzer(book)
        return Response(serialized.data)    


@api_view(["GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response({"message":"Authenticated", "user":request.user.username})



@api_view(["POST", "GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def stars(request, pk):
    book = Book.objects.get(id=pk)
    if not book.star:
        star = Star.objects.create()
        book.star = star 
    if request.method == 'POST':

        user = request.user 
        

        if user.customuser in book.star.customuser_set.all():

            return Response({"m":"You already starred the book", "star rating":book.star.avarage})
        
        user.customuser.star.add(book.star) 
        book.star.save()
        
        stars = book.star
        print(stars.number) 
        stars.number += request.data["numbers"]
        stars.save()
        
        return Response({"message":"Starring complete!",})
    
    serialized = BookSerialzer(book)
    return Response({"message":serialized.data})

@api_view(["POST", "GET"])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def comment(request, pk):
    user = request.user.customuser
    
    book = Book.objects.get(id=pk)
    
    if request.method == "POST":
        data = request.data['content']
        
        
        commnt = Comment(book=book, user=user, content=data)
        commnt.save()
        return Response({"message":"Success"})
    commnt = Comment.objects.filter(book=book)
    if not commnt:
        return Response({"message":"there is no comments"})

    serialized = CommentSerializer(commnt, many=True)
    return Response({"message":serialized.data})



        