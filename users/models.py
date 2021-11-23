from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.db.models.deletion import CASCADE

# from multiselectfield import MultiSelectField


class Category(models.Model):
    cat_name = models.CharField(max_length=155)
    
    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.cat_name
    # cat_name = models.OneToOneField(
    #     Headline., on_delete=models.CASCADE, default=True)
    # slug = models.SlugField(unique=True)
    # category_choices = (
    #     ('sports', 'sports'),
    #     ('business', 'business'),
    #     ('health', 'health'),
    #     ('entertainment', 'entertainment'),
    #     ('technology', 'technology')
    # )
    # cat_name = MultiSelectField(choices=category_choices)



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(
        Category, blank=True)  # through='UserCategory')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def selectedby(self):
        return ",".join([str(p) for p in self.name.all()])


# class UserCategory(models.Model):
#     user = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)

#     class Meta:
#         verbose_name_plural = "UserSelectedCategories"
#         unique_together = [['user', 'category']]
