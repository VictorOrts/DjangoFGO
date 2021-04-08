from django.db import models

# Create your models here.
class Character_class(models.Model):
    """A typical class defining a model, derived from the Model class."""
    # Fields
    name = models.CharField(max_length=20, help_text='Enter field documentation')
    class Meta:
        ordering = ['-name']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.name

class Character(models.Model):
    """A typical class defining a model, derived from the Model class."""
    # Fields
    name = models.CharField(max_length=20, help_text='Enter field documentation')
    character_c = models.ForeignKey(Character_class,on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=255, help_text='Enter field documentation')
    genre = models.CharField(max_length=10, help_text='Enter field documentation')
    class Meta:
        ordering = ['-name','-character_c','-description']
    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('model-detail-view', args=[str(self.id)])

class Skill(models.Model):
    """A typical class defining a model, derived from the Model class."""
    # Fields
    name = models.CharField(max_length=20, help_text='Enter field documentation')
    character_id = models.ForeignKey(Character, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, help_text='Enter field documentation')
    class Meta:
        ordering = ['-name','-character_id','-description']
    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('model-detail-view', args=[str(self.id)])
