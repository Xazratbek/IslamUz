from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from hitcount.models import HitCountMixin

class Iymon(models.Model, HitCountMixin):
    title = models.CharField(max_length=300)
    slug = models.SlugField(null=False, unique=True)
    body = RichTextField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("iymon", kwargs={'slug':self.slug, 'pk':self.pk})

class Zakot(models.Model, HitCountMixin):
    title = models.CharField(max_length=300)
    slug = models.SlugField(null=False, unique=True)
    body = RichTextField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("zakot", kwargs={'slug':self.slug, 'pk':self.pk})

class Namoz(models.Model, HitCountMixin):
    title = models.CharField(max_length=300)
    slug = models.SlugField(null=False, unique=True)
    body = RichTextField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("namoz", kwargs={'slug':self.slug, 'pk':self.pk})

class Ruza(models.Model, HitCountMixin):
    title = models.CharField(max_length=300)
    slug = models.SlugField(null=False, unique=True)
    body = RichTextField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("ruza", kwargs={'slug':self.slug, 'pk':self.pk})

class Haj(models.Model, HitCountMixin):
    title = models.CharField(max_length=300)
    slug = models.SlugField(null=False, unique=True)
    body = RichTextField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("haj", kwargs={'slug':self.slug, 'pk':self.pk})
