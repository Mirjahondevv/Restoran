from django.db import models

class AuthorBook(models.Model):
    ism = models.CharField(max_length=12)
    familiya = models.CharField(max_length=23)
    yosh = models.IntegerField()


class Category(models.Model):
    name = models.CharField(max_length=23)

    def __str__(self):
        return self.name

class Foods(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=23)
    price = models.IntegerField()
    img = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.name

class Chefs(models.Model):
    ism = models.CharField(max_length=23)
    img = models.ImageField(upload_to='media/')
    instagram = models.CharField(max_length=23)
    facebook = models.CharField(max_length=23)
    twitter = models.CharField(max_length=23)

    def __str__(self):
        return self.ism

class Contact(models.Model):
    name = models.CharField(max_length=23)
    email = models.EmailField()
    subject = models.CharField(max_length=23)
    message = models.TextField()

    def __str__(self):
        return self.name