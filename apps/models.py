from django.db.models import Model, CharField, ForeignKey, CASCADE, IntegerField


# from django_resized import ResizedImageField


class Category(Model):
    name = CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Product(Model):
    name = CharField(max_length=255)
    price = IntegerField()
    description = CharField(max_length=255)
    category = ForeignKey('apps.Category', on_delete=CASCADE)

    def __str__(self):
        return self.name
