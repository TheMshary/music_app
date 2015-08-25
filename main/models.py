from django.db import models

# Create your models here.

class Genre(models.Model):
    genre_id = models.IntegerField(null=True)
    genre_parent_id = models.ForeignKey('main.Genre', null=True)
    genre_title = models.CharField(max_length=255, null=True)
    genre_slug = models.SlugField(max_length=255, null=True)

class Artist(models.Model):
    artist_id = models.IntegerField(null=True)
    artist_website = models.CharField(max_length=255, null=True)
    artist_name = models.CharField(max_length=255, null=True)
    artist_bio = models.TextField(null=True)
    artist_location = models.CharField(max_length=255, null=True)

class Album(models.Model):
    album_id = models.IntegerField(null=True)
    artist = models.ForeignKey('main.Artist', null=True)
    album_title = models.CharField(max_length=255, null=True)
    album_image = models.ImageField(upload_to="album_images")

class Track(models.Model):
    track_id = models.IntegerField(null=True)
    album = models.ForeignKey('main.Album', null=True)
    genre = models.ForeignKey('main.Genre', null=True)
    track_title = models.CharField(max_length=255, null=True)
