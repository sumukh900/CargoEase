from django.db import models


class User(models.Model):
    username = models.CharField(primary_key=True,max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.username + ' ' + self.password + ' ' + self.first_name + ' ' + self.last_name

class Carrier(models.Model):
    carrier_id = models.CharField(primary_key=True,max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)
    email_address = models.EmailField()
    address = models.CharField(max_length=512, blank=True, null=True)
    password = models.CharField(max_length=100)
    price =  models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.carrier_id 

class Route(models.Model):
    route_id = models.CharField(primary_key=True,max_length=100)
    source = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    carrier_id = models.ForeignKey(Carrier, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.route_id) 


class Container(models.Model):
    container_id = models.CharField(primary_key=True,max_length=100)
    length = models.DecimalField(max_digits=10, decimal_places=2)
    breadth = models.DecimalField(max_digits=10, decimal_places=2)
    height = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.container_id 

class Carrier_details(models.Model):
    container_id = models.ForeignKey(Container, on_delete=models.CASCADE)
    carrier_id = models.ForeignKey(Carrier, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    route_id = models.ForeignKey(Route, on_delete=models.CASCADE)
    length = models.DecimalField(max_digits=10, decimal_places=2)
    breadth = models.DecimalField(max_digits=10, decimal_places=2)
    height = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.container_id+' '+self.route_id+' '+self.username +' '+self.carrier_id