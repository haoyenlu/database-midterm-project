from django.db import models

# Create your models here.
class Type(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.TextField()


class Spot(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.TextField()
    lon = models.FloatField()
    lat = models.FloatField()
    town_id = models.CharField(max_length = 3)
    type = models.ForeignKey(Type,on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.id}:{self.name}"

class Surfshop(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.TextField()
    address = models.TextField()
    spot = models.ForeignKey(Spot,on_delete = models.CASCADE)
    rating = models.FloatField()
    operating_now = models.BooleanField()

    def __str__(self):
        return f"{self.id}:{self.name}"

class News(models.Model):
    news_id = models.IntegerField(primary_key = True)
    date = models.TextField()
    url = models.TextField()
    title = models.TextField()
    spot = models.ForeignKey(Spot,on_delete = models.CASCADE)

    def __str__(self):
        return self.news_id

class Information(models.Model):
    spot = models.ForeignKey(Spot,primary_key = True,on_delete = models.CASCADE)
    date = models.DateField()
    wave_height = models.FloatField()
    wave_period = models.FloatField()
    wave_direction = models.FloatField()
    wind_speed = models.FloatField()
    wind_direction = models.FloatField()
    temperature = models.FloatField()
    sea_temperature = models.FloatField()
    score = models.IntegerField()


class Reviewer(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.TextField()
    email = models.EmailField() 

class Recommendation(models.Model):
    reviewer = models.ForeignKey(Reviewer,on_delete = models.CASCADE)
    spot = models.ForeignKey(Spot,on_delete = models.CASCADE)
    score = models.IntegerField()
    content = models.TextField()
    date = models.DateField()

class Town(models.Model):
    id = models.CharField(max_length = 3,primary_key = True)
    name = models.TextField()
    city = models.TextField()

    