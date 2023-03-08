from django.db import models
from hitcount.models import HitCountMixin

class Sura(models.Model,HitCountMixin):
    name = models.CharField(max_length=300)
    # slug = models.SlugField(null=False, unique=True)

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.name)
    #     return super().save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse("suralar", kwargs={'slug':self.slug, 'pk':self.pk})

    def __str__(self):
        return self.name

class Oyat(models.Model):
    sura = models.ForeignKey(Sura, on_delete=models.CASCADE)
    arabic_text = models.TextField()
    uzbek_text = models.TextField()
    audio_file = models.FileField(upload_to='oyat_audio',null=True)

    def __str__(self):
        return str(self.id)