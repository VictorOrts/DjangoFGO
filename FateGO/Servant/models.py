from django.db import models

# Create your models here.
# "https://api.atlasacademy.io/basic/NA/servant/search?lang=en&name=Kama&className=assassin"
class Servantch(models.Model):
    unique_id  =  models.CharField(max_length=8, primary_key=True)
    collectionNo = models.CharField(max_length=5)
    name = models.CharField(max_length=30)
    typeS = models.CharField(max_length=30)
    flag = models.CharField(max_length=30)
    className = models.CharField(max_length=30)
    attribute = models.CharField(max_length=30)
    rarity = models.CharField(max_length=1)
    atkMax = models.CharField(max_length=5)
    hpMax = models.CharField(max_length=5)
    face = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    def get_collectionNo(self):
        return self.collectionNo

class infoCharacter(models.Model):
    unique_id = models.CharField(max_length=8,primary_key=True)
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
