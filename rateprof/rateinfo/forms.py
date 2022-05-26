from django import forms
from rateinfo.models import (
    Instructor,
    Course,
    Comment,
    User,
    GP,
)


class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = '__all__'

    def clean_Instructor_Name(self):
        return self.cleaned_data['Instructor_Name'].strip()

    def clean_Instructor_Department(self):
        return self.cleaned_data['Instructor_Department'].strip()


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

    def clean_Course_Name(self):
        return self.cleaned_data['Course_Name'].strip()

    def clean_Course_Department(self):
        return self.cleaned_data['Course_Department'].strip()


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

    def clean_Comment_Text(self):
        return self.cleaned_data['Comment_Text'].strip()

    def clean_Comment_Score(self):
        return self.cleaned_data['Comment_Score']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

    def clean_User_Name(self):
        return self.cleaned_data['User_Name'].strip()

    def clean_User_Gender(self):
        return self.cleaned_data['User_Gender'].strip()
