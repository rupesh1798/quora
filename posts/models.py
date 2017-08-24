from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    text = models.TextField()
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
        return self.title
    def save(self, *args, **kwargs):
        if not self.pk:
            super(Post, self).save(*args, **kwargs)
        else:
            self.update_date = datetime.now()
        if not self.slug:
            slug_str = "%s" % (self.title.lower())
            self.slug = slugify(slug_str)
        super(Post, self).save(*args, **kwargs)


class Answer(models.Model):
    question = models.ForeignKey(Post)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    upvotes = models.IntegerField(default=0)

#    class Meta:
#        db_table = "answers"
#        verbose_name = ("Answer")
#        verbose_name_plural = ("Answers")
#        ordering = ("date",)

    def __unicode__(self):
        return u'{0} - {1}'.format(self.user.username, self.question.title)

#    def get_comment_as_markdown(self):
#        return markdown.markdown(self.comment, safe_mode='escape')

#    def get_up_voters(self):
#        upvotes = UserUpvote.objects.filter(comment=self)
#        upvote_users = [upvote.user.id for upvote in upvotes]
#        return upvote_users
