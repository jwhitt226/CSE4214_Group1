from django.db import models
import uuid


# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    userid = models.UUIDField(default=uuid.uuid4, editable=False)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=20)

    @classmethod
    def create_user(cls, **kwargs):
        # Create and return a new user instance
        return cls.objects.create(**kwargs)

class Cart(models.Model):
    def __init__ (self):
        self.items = {}

    def add_book(self, book):
        if book.id in self.items:
            self.items[book.id]['quantity'] += 1
        else:
            self.items[book.id] = {'book_id': book.id, 'quantity': 1}