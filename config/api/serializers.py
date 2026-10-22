from rest_framework import serializers
from .models import Author, Book

class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    full_name = serializers.CharField(max_length=255)
    birth_date = serializers.CharField(required=False, allow_null=True, allow_blank=True)

    def validate_full_name(self, value):
        author = Author.objects.filter(full_name=value)
        if self.instance:
            author = author.exclude(pk=self.instance.pk)
        if author.exists():
            raise serializers.ValidationError("Bu nomli author allaqachon mavjud")
        return value

    def create(self, validated_data):
        return Author.objects.create(**validated_data)

    def update(self, instance: Author, validated_data):
        instance.full_name = validated_data.get("full_name", instance.full_name)
        instance.birth_date = validated_data.get("birth_date", instance.birth_date)
        instance.save()
        return instance


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=10, decimal_places=2, default=0)
    pages = serializers.IntegerField(min_value=1, default=1)
    published_year = serializers.IntegerField(default=2020)
    author_id = serializers.IntegerField()  

    def validate_author_id(self, value):
        if not Author.objects.filter(pk=value).exists():
            raise serializers.ValidationError("Bunday Author topilmadi")
        return value

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance: Book, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.price = validated_data.get("price", instance.price)
        instance.pages = validated_data.get("pages", instance.pages)
        instance.published_year = validated_data.get("published_year", instance.published_year)
        instance.author_id = validated_data.get("author_id", instance.author_id)
        instance.save()
        return instance