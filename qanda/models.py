from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify


class Question(models.Model):
  question = models.CharField(_("question"), max_length=250)
  slug = models.SlugField(_("slug"), unique=True)

  def __str__(self):
    return f'{self.id} - {self.question}'
    
  def save(self, *args, **kwargs):
    if not self.slug:
      self.slug = slugify(self.question)
    super(Question, self).save(*args, **kwargs)


class Answer(models.Model):
  answer = models.TextField(_("answer"), blank=True, null=True)
  question = models.ForeignKey(Question, related_name='answers', on_delete=models.PROTECT)

  def __str__(self):
    return f'{self.answer}'