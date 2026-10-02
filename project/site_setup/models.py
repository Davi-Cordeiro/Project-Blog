from django.db import models

class MenuLinks(models.Model):
    class Meta:
        verbose_name = "Menu Link"
        verbose_name_plural = "Menu Links"

    text = models.CharField(max_length=100)
    url_or_path = models.CharField(max_length=2048)
    new_tab = models.BooleanField(default=False)

    def __str__(self):
        return self.text
