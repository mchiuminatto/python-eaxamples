from datetime import datetime
from dotenv import load_dotenv

load_dotenv()



# This creates a class to serielize
class Comment:
    def __init__(self, email: str, content: str, created: datetime | None =None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()

    def __str__(self):
        return f"{self.email} \n{self.content}"

comment = Comment("test@test.com", "this is a comment")
print(comment)


# This creates a basic serializer

from rest_framework import serializers

class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

# No we serialize the object

# the object to serialize is passed in the constructor

serializer = CommentSerializer(comment)


print("The serializer ", serializer)
print("The serializer data ", serializer.data)

# Now we serialize into JSON 

from rest_framework.renderers import JSONRenderer

json = JSONRenderer().render(serializer.data)
print("This is JSON serialization ", json)



# Deserializing data

import io
from rest_framework.parsers import JSONParser

stream = io.BytesIO(json)
data = JSONParser().parse(stream)

print(f"This is the deserialized data {data}, the type is {type(data)}")

serializer = CommentSerializer(data=data)  # directly specifies data

print(f"Is valid the data? {serializer.is_valid()}")
print(f"The serializer validated data {serializer.validated_data}")



