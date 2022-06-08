from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=40,null=True)
    email = models.EmailField()
    description = models.TextField()

    def __str__(self):
        return self.name


STATUS_CHOICES = (
   ('draft', 'Draft'),
   ('published', 'Published'),
)
class Blog(models.Model):
    title = models.CharField(max_length = 250,default=True)
    slug = models.SlugField(max_length = 250,default=True)
    text = models.TextField()
    published_at = models.DateField(auto_now_add = True)
    status = models.CharField(
        max_length = 10, 
        choices = STATUS_CHOICES,
        default ='draft')
 
 
    class Meta:
       ordering = ('-published_at', )
 
    def __str__(self):
        return self.title