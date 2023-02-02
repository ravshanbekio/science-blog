from django.db import models
from ckeditor.fields import RichTextField
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=25)

    class Meta:
        verbose_name_plural = "Category"

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=120)
    subtitle = models.CharField(max_length=70)
    slug = models.SlugField(blank=True, null=True)
    body = RichTextField()
    preview_image = models.FileField()
    category = models.ManyToManyField(Category, related_name='blogs')
    views = models.IntegerField(default=0)
    added_date = models.DateField(auto_now_add=True)
    estimated_read_time = models.IntegerField(default=2)

    class Meta:
        verbose_name_plural = "Blog"

    def __str__(self):
        return self.title
    
class PinnedBlog(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.PROTECT)

    def __str__(self):
        return self.blog.title
    
@receiver(post_save, sender=Blog)
def pre_save_blog(instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
        instance.save()