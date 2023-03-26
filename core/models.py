from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100)
    products = models.ManyToManyField(Product)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Provider(models.Model):
    name = models.CharField(max_length=100)
    city = models.OneToOneField(City, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
