# blog/serializers.py
# convert our django data models to a text-representation
# suitable to transmit over HTTP.

from rest_framework import serializers
from .models import *


class ArticleSerializer(serializers.ModelSerializer):
    """A serializer for the Article model. Specify whick model/fields to send in the API."""

    class Meta:
        model = Article
        fields = ["id", "title", "author", "text"]

    # add methods to customize the Create/Read/update/Delete operations
    def create(self, validated_data):
        """override the superclass method that handles object creation."""
        print(f"AritcleSerializer.create, validated_data={validated_data}.")
        # # create an Article object
        # article = Article(**validated_data)
        # # attach a FK for the User
        # article.user = User.objects.first()
        # # save the object to the database
        # article.save()
        # # return an object instance
        # return article

        # a simplified way:
        # attach a FK for the User
        validated_data["user"] = User.objects.first()

        # do the create and save all at once
        return Article.objects.create(**validated_data)
