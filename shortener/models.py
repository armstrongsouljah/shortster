from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import pre_save

from .utils import shortcode_gen

# Generic user
User = get_user_model()

# Create your models here.
class Shortener(models.Model):
    """
    Store data related to links and returned shortened urls
    """
    website = models.CharField(max_length=255, unique=True)
    short_code = models.CharField(max_length=6, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    last_visited = models.DateTimeField(blank=True, null=True)
    visit_count = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.author.username}, {self.website}'


@receiver(pre_save, sender=Shortener)
def shortener_receiver(instance, sender, *args, **kwargs):
    if instance.short_code:
        code_exists = Shortener.objects.filter(
            short_code=instance.short_code).exists()
        if code_exists:
            instance.short_code = shortcode_gen(6)
            return instance
    if not instance.short_code:
        instance.short_code = shortcode_gen(6)
    return instance
        

