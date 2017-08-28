from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField #does not contain upload option for us in Images
from ckeditor_uploader.fields import  RichTextUploadingField #for adding upload from our own server in CKEDITOR

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    slug = models.SlugField(max_length=255, null=True, blank=True)
    details = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
#    class Meta:
#        db_table = "questions"
#        verbose_name = ("Question")
#        verbose_name_plural = ("Questions")
#        ordering = ("created_date",)
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text
    def save(self, *args, **kwargs):
        if not self.pk:
            super(Question, self).save(*args, **kwargs)
        else:
            self.update_date = datetime.now()
        super(Question, self).save(*args, **kwargs)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = RichTextUploadingField()
#    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

#    class Meta:
#        db_table = "answers"
#        verbose_name = ("Answer")
#        verbose_name_plural = ("Answers")
#        ordering = ("date",)

#    def __unicode__(self):
#        return u'{0} - {1}'.format(self.user.username, self.question.title)

#    def get_comment_as_markdown(self):
#        return markdown.markdown(self.comment, safe_mode='escape')

#    def get_up_voters(self):
#        upvotes = UserUpvote.objects.filter(comment=self)
#        upvote_users = [upvote.user.id for upvote in upvotes]
#        return upvote_users
class Comment(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
