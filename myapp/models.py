from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    # Add a method to generate the absolute URL for the product detail page
    #This helps in creating SEO-friendly URLs for each product, which can improve search engine rankings and user experience.
    def get_absolute_url(self):
        return reverse("detail", args=[self.slug])
    

    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(unique=True,blank=True) # Add a slug field for SEO-friendly URLs SEO stands for 
    # Search Engine Optimization, which is the practice of improving the visibility and ranking of a 
    # website or web page in search engine results. A slug is a URL-friendly version of a string, typically 
    # used to create clean and readable URLs for products, categories, or other content on a website. 
    # By adding a slug field to the Product model, you can generate SEO-friendly URLs for 
    # each product, making it easier for search engines to index and rank your product pages.
    stock = models.IntegerField()
    active = models.BooleanField()

    def save(self,*args,**kwargs):
        if not self.slug:
            # self.slug = slugify(self.name)
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Product.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name 