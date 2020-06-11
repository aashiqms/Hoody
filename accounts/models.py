from django.contrib.auth.models import User
from django.db import models
from PIL import Image


########################################################################################################################
# ** Profile Model ** for storing profile information has OneToOne relationship with default User model
########################################################################################################################


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='media/profile_pics/default.jpg', upload_to='profile_pics')
    cover_pic = models.ImageField(default='media/cover_pics/cover.jpg', upload_to='cover_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, **kwargs):
        super().save()
        #
        # img = Image.open(self.image.path)
        # if img.height > 300 or img.width > 300:
        #     output_size = (300, 300)
        #     img.thumbnail(output_size)
        #     img.save(self.image.path)


# class Products(models.Model):
#     product_name = models.CharField