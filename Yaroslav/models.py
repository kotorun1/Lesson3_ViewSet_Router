from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class StatusPet(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name



class Pet(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='images/')
    status = models.ForeignKey(StatusPet, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)


    def __str__(self):
       return self.name
    

class StatusOrder(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Order(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    ship_date = models.DateTimeField()
    status = models.ForeignKey(StatusOrder, on_delete=models.CASCADE)
    complete = models.BooleanField()

    def __str__(self):
        return self.pet.name

