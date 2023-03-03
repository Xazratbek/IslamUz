from django.db import models
from hitcount.models import HitCountMixin

class NamozVaqtlari(models.Model,HitCountMixin):
    mintaqa = models.CharField(max_length=300)
    bomdod  = models.TimeField(null=True)
    quyosh  = models.TimeField(null=True)
    peshin = models.TimeField(null=True)
    asr  = models.TimeField(null=True)
    shom  = models.TimeField(null=True)
    xufton  = models.TimeField(null=True)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
    	return self.mintaqa

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.mintaqa)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("namoz_vaqtlari", kwargs={'slug':self.slug, 'pk':self.pk})