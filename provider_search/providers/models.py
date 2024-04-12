from django.db import models

# Create your models here.
class Provider(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    sex = models.CharField(max_length=10)
    birth_date = models.CharField(max_length=20)
    rating = models.FloatField()
    primary_skills = models.JSONField()
    secondary_skill = models.JSONField()
    company = models.CharField(max_length=100)
    active = models.BooleanField()
    country = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    views = models.IntegerField(default=0)

    class Meta:
        ordering = ['-rating', 'views']

    def __str__(self):
        model_name = self.__class__.__name__
        fields_str = ", ".join((f"{field.name}={getattr(self, field.name)}" for field in self._meta.fields))
        return f"{model_name}({fields_str})"
