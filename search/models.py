from django.db import models


class RandomText(models.Model):
    text = models.TextField()
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.text


class ShowLog(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    shown = models.ForeignKey(RandomText, null=True, related_name='search_queries', on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = "Show log"

    def __str__(self):
        return self.shown.text if self.shown else "None"
