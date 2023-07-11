from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user    = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar  = models.ImageField(default='profile_images/default.png', upload_to='profile_images/')
    bio     = models.TextField()
    phone   = models.CharField(default='+9890000000000', max_length=15)

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)
    def __str__(self):
        return self.user.username