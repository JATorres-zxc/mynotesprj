from rest_framework.serializers import ModelSerializer
from .models import Note


# serialize note model
class NoteSerializer(ModelSerializer):
    """
    Serializers in Django REST Framework are used to convert complex data types
    into native Python datatypes that can then be easily rendered into JSON, XML,
    or other content types and vice versa.
    """
    class Meta:
        model = Note # specify the model to be serialized which is Note in model
        fields = '__all__' # all meaning body, updated, created