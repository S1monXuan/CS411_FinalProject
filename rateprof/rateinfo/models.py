from django.db import models
from django.urls import reverse


class Instructor(models.Model):
    Instructor_ID = models.AutoField(primary_key=True)
    Instructor_Name = models.CharField(max_length=255)
    Instructor_Department = models.CharField(max_length=255)

    def __str__(self):
        return '%s - %s' % (self.Instructor_Name, self.Instructor_Department)

    # def get_absolute_url(self):
    #     return reverse('rateinfo_instructor_detail_urlpattern',
    #                    kwargs={'pk': self.pk},
    #                    )
    #
    # def get_update_url(self):
    #     return reverse('rateinfo_instructor_update_urlpattern',
    #                    kwargs={'pk': self.pk}
    #                    )
    #
    # def get_delete_url(self):
    #     return reverse('rateinfo_instructor_delete_urlpattern',
    #                    kwargs={'pk': self.pk}
    #                    )

    class Meta:
        ordering = ['Instructor_Name']


class Course(models.Model):
    Course_ID = models.AutoField(primary_key=True)
    Course_Name = models.CharField(max_length=255)
    Course_Department = models.CharField(max_length=255)
    Course_Instructor_ID = models.ForeignKey(Instructor, related_name='courses', on_delete=models.PROTECT)

    def __str__(self):
        return '%s - %s' % (self.Course_Name, self.Course_Department)

    def get_absolute_url(self):
        return reverse('rateinfo_course_detail_urlpattern',
                       kwargs={'pk': self.pk},
                       )
    #
    # def get_update_url(self):
    #     return reverse('rateinfo_course_update_urlpattern',
    #                    kwargs={'pk': self.pk},
    #                    )
    #
    # def get_delete_url(self):
    #     return reverse('rateinfo_course_delete_urlpattern',
    #                    kwargs={'pk': self.pk})

    class Meta:
        ordering = ['Course_Department', 'Course_Name']


class User(models.Model):
    User_ID = models.AutoField(primary_key=True)
    User_Name = models.CharField(max_length=255)
    User_Gender = models.CharField(max_length=2)

    def __str__(self):
        return '%s - %s' % (self.User_Name, self.User_Gender)

    # def get_absolute_url(self):
    #     return reverse('rateinfo_user_detail_urlpattern',
    #                    kwargs={'pk': self.pk}
    #                    )
    #
    # def get_update_url(self):
    #     return reverse('rateinfo_user_update_urlpattern',
    #                    kwargs={'pk': self.pk},
    #                    )
    #
    # def get_delete_url(self):
    #     return reverse('rateinfo_user_delete_urlpattern',
    #                    kwargs={'pk': self.pk},
    #                    )

    class Meta:
        ordering = ['User_ID']


class Comment(models.Model):
    Comment_ID = models.AutoField(primary_key=True)
    Comment_Text = models.CharField(max_length=255)
    Comment_Score = models.IntegerField()
    Comment_Course_ID = models.ForeignKey(Course, related_name='comments', on_delete=models.PROTECT)
    Comment_User_ID = models.ForeignKey(User, related_name='comments', on_delete=models.PROTECT)

    def __str__(self):
        return '%s - %s - %s' % (self.Comment_Course_ID, self.Comment_Course_ID.Course_Name, self.Comment_Text)

    # def get_absolute_url(self):
    #     return reverse('rateinfo_comment_detail_urlpattern',
    #                    kwargs={'pk': self.pk}
    #                    )

    class Meta:
        ordering = ['Comment_Course_ID', 'Comment_Score']


class Response(models.Model):
    Response_ID = models.AutoField(primary_key=True)
    Response_Text = models.CharField(max_length=255)
    Response_Comment_ID = models.ForeignKey(Comment, related_name='responses', on_delete=models.PROTECT)

    def __str__(self):
        return '%s - %s' % (self.Response_ID, self.Response_Text)

    class Meta:
        ordering = ['Response_ID']


class GP(models.Model):
    User_ID = models.ForeignKey(User, related_name='gps', on_delete=models.PROTECT)
    Group_ID = models.IntegerField()

    def __str__(self):
        return '%s - %s' % (self.Group_ID, self.User_ID.User_Name)


class Teach(models.Model):
    Course_ID = models.ForeignKey(Course, related_name='teaches', on_delete=models.PROTECT)
    Instructor_ID = models.ForeignKey(Instructor, related_name='teaches', on_delete=models.PROTECT)

    def __str__(self):
        return '%s - %s' % (self.Instructor_ID.Instructor_Name, self.Course_ID.Course_Name)

    # class Meta:
    #     ordering = ['Instructor_ID.Instructor_Name', 'Course_ID.Course_Name']


class GroupChat(models.Model):
    Group_Chat_ID = models.AutoField(primary_key=True)
    Message_Info = models.CharField(max_length=255)
    Receive_From_ID = models.ForeignKey(User, related_name='groupchatrecieve', on_delete=models.PROTECT)
    Send_To_ID = models.ForeignKey(User, related_name='groupchatsent', on_delete=models.PROTECT)

    def __str__(self):
        return '%s - %s' % (self.Group_Chat_ID, self.Message_Info)

    # def get_absolute_url(self):
    #     return reverse('rateinfo_groupchat_detail_urlpattern',
    #                    kwargs={'pk': self.pk}
    #                    )

    class Meta:
        ordering = ['Group_Chat_ID']
