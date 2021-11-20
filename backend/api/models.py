# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Information(models.Model):
    spot = models.OneToOneField('Spot', models.DO_NOTHING, db_column='Spot_id', primary_key=True)  # Field name made lowercase.
    date = models.TextField(db_column='Date')  # Field name made lowercase.
    wave_height = models.FloatField(db_column='Wave_height', blank=True, null=True)  # Field name made lowercase.
    wave_period = models.FloatField(db_column='Wave_period', blank=True, null=True)  # Field name made lowercase.
    wave_direction = models.FloatField(db_column='Wave_direction', blank=True, null=True)  # Field name made lowercase.
    wind_speed = models.FloatField(db_column='Wind_speed', blank=True, null=True)  # Field name made lowercase.
    wind_direction = models.FloatField(db_column='Wind_direction', blank=True, null=True)  # Field name made lowercase.
    temperature = models.FloatField(db_column='Temperature', blank=True, null=True)  # Field name made lowercase.
    sea_temperature = models.FloatField(db_column='Sea_temperature', blank=True, null=True)  # Field name made lowercase.
    score = models.IntegerField(db_column='Score', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INFORMATION'
        unique_together = (('spot', 'date'),)


class News(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    url = models.TextField(db_column='Url', blank=True, null=True)  # Field name made lowercase.
    title = models.TextField(db_column='Title', blank=True, null=True)  # Field name made lowercase.
    spot = models.ForeignKey('Spot', models.DO_NOTHING, db_column='Spot_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NEWS'


class Recommend(models.Model):
    reviewer = models.OneToOneField('Reviewer', models.DO_NOTHING, db_column='Reviewer_id', primary_key=True)  # Field name made lowercase.
    spot = models.ForeignKey('Spot', models.DO_NOTHING, db_column='Spot_id')  # Field name made lowercase.
    score = models.IntegerField(db_column='Score', blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RECOMMEND'
        unique_together = (('reviewer', 'spot'),)


class Reviewer(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    email = models.TextField(db_column='Email', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'REVIEWER'


class Spot(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    lon = models.FloatField(db_column='Lon', blank=True, null=True)  # Field name made lowercase.
    lat = models.FloatField(db_column='Lat', blank=True, null=True)  # Field name made lowercase.
    town = models.ForeignKey('Town', models.DO_NOTHING, db_column='Town_id', blank=True, null=True)  # Field name made lowercase.
    type = models.ForeignKey('Type', models.DO_NOTHING, db_column='Type_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SPOT'


class Surfshop(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase.
    spot = models.ForeignKey(Spot, models.DO_NOTHING, db_column='Spot_id', blank=True, null=True)  # Field name made lowercase.
    rating = models.FloatField(db_column='Rating', blank=True, null=True)  # Field name made lowercase.
    operating_now = models.BooleanField(db_column='Operating_now', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SURFSHOP'


class Town(models.Model):
    id = models.CharField(db_column='Id', primary_key=True, max_length=3)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    city = models.TextField(db_column='City', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TOWN'


class Type(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TYPE'
