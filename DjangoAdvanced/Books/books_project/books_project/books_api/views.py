from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer


# Create your views here.
class ListBooksView(APIView):
    
    def get(self, request):
        books = Book.objects.all()
        seriaizer = BookSerializer(books, many=True)

        return Response({'books': seriaizer.data})

    
    def post(self, request):
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class DetailBookView(APIView):


    def get(self, request, id):

        book = Book.objects.get(pk=id)
        serializer = BookSerializer(book)
        return Response({'book': serializer.data})
    
    def post(self, request, id):
        book = Book.objects.get(pk=id)
        serializer = BookSerializer(book, data=request.data)

        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        book = Book.objects.all(pk=id)
        book.delete()

        return Response(status=status.HTTP_200_OK)


