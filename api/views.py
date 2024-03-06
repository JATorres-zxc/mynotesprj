from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note
from .serializers import NoteSerializer

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)

# to GET all notes or to POST(CREATE) new note
@api_view(['GET', 'POST'])
def getNotes(request):
    
    if request.method == 'GET':
        # for all notes
        notes = Note.objects.all().order_by('-updated') # order by desc of time updated
        serializer = NoteSerializer(notes, many=True) #serialize
        
        return Response(serializer.data)

    # for creating a note
    if request.method == 'POST':
        data = request.data
        note = Note.objects.create(body=data['body']) # this is where you type the body.data
        serializer = NoteSerializer(note, many = False) #serialize
        return Response(serializer.data)


# to GET the single note, PUT(update) the body of a note and DELETE a note
@api_view(['GET', 'PUT', 'DELETE'])
def getNote(request, pk):
    
    if request.method == 'GET':
        # for single note so may pk
        notes = Note.objects.get(id=pk)
        serializer = NoteSerializer(notes, many=False) #serialize
        
        return Response(serializer.data)
    
    # for updating a note
    if request.method == 'PUT':
        data = request.data
        note = Note.objects.get(id=pk)
        # create a serializer instance for note updated version
        serializer = NoteSerializer(instance=note, data=data)
        
        if serializer.is_valid():
            serializer.save()
        
        return Response(serializer.data)
    
    
    #for deleting a note
    if request.method == 'DELETE':
        note = Note.objects.get(id=pk)
        note.delete()
        return Response('Note deleted')
    
    
    
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user): # custom tokenserializer to include additional info(username) in token
        token = super().get_token(user)

        token['username'] = user.username

        return token
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer #to use the custome otekn serializer

