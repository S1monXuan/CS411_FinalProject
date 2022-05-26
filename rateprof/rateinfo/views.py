from django.core import serializers
from django.db import connection
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from rateinfo import models
from rateinfo.forms import CourseForm
from rateinfo.models import Course

# Create your views here.
from rateinfo.utils import ObjectCreateMixin


class IndexList(View):

    def get(self, request):
        cursor = connection.cursor()
        cursor.execute(
            "SELECT DISTINCT Course_Name,rateinfo_Instructor.Instructor_Name FROM rateinfo_Instructor JOIN rateinfo_Course ON rateinfo_Instructor.Instructor_ID = rateinfo_Course.Course_Instructor_ID_id WHERE rateinfo_Course.Course_ID IN (SELECT Course_ID FROM Course WHERE Course_Department = 'Computer Science' ) limit 15")
        selectCourseId = dict(cursor.fetchall())
        courseIdKey = selectCourseId.keys()
        courseIdVal = selectCourseId.values()

        cursor.execute(
            "SELECT Course_Name, t.averageRate FROM rateinfo_course r JOIN (SELECT Comment_Course_ID_id, AVG(c.Comment_Score) as averageRate FROM rateinfo_Comment c NATURAL JOIN rateinfo_Course co WHERE co.Course_Department = 'Computer Science' GROUP BY Comment_Course_ID_id HAVING AVG(c.Comment_Score) > 4 limit 15) t ON r.Course_ID = t.Comment_Course_ID_id")
        courseAbove4 = dict(cursor.fetchall())
        courseAbove4Key = courseAbove4.keys()
        courseAbove4Val = courseAbove4.values()
        return render(
            request,
            'rateinfo/index_list.html',
            {'selectCourseId': selectCourseId,
             'courseAbove4': courseAbove4,
             }
        )


# class InstructorList(View):
#
#     def get(self, request):
#         value = request.GET.get('q')
#         if value:
#             instructorList = models.Instructor.objects.filter(Instructor_Name__contains=value)
#             return render(
#                 request,
#                 'rateinfo/instructor_list.html',
#                 {'instructor_list': models.Instructor.objects.filter(Instructor_Name__contains=value)}
#             )
#
#         return render(
#             request,
#             'rateinfo/instructor_list.html',
#             {'instructor_list': Instructor.objects.all()}
#         )

class CourseList(View):

    def get(self, request):
        value = request.GET.get('q')
        if value:
            sql = "select * from rateinfo_Course WHERE Course_Name LIKE '%%%s%%';" % value
            courseList = models.Course.objects.raw(sql)
            return render(
                request,
                'rateinfo/course_list.html',
                {'course_list': models.Course.objects.filter(Course_Name__contains=value)}
                # models.Course.objects.filter(Course_Name__contains=value)
            )

        return render(
            request,
            'rateinfo/course_list.html',
            {'course_list': models.Course.objects.raw("select * from rateinfo_Course")}
        )


class CourseDetail(View):

    def get(self, request, pk):
        course = get_object_or_404(
            Course,
            pk=pk
        )
        # commentlist = models.Course.objects.raw("select * from rateinfo_comment WHERE Comment_Course_ID = { }".format(course.Course_ID))
        # commentlist = course.comments.all(),
        return render(
            request,
            'rateinfo/course_detail.html',
            {'course': course, 'comment_list': course.comments.all()}  # , 'instructor': instructor }
        )

# class InstructorList(View):
#
#     def get(self, request):
#         value = request.GET.get('q')
#         if value:
#             instructorList = models.Instructor.objects.filter(Instructor_Name__contains=value)
#             return render(
#                 request,
#                 'rateinfo/instructor_list.html',
#                 {'instructor_list': models.Instructor.objects.filter(Instructor_Name__contains=value)}
#             )
#
#         return render(
#             request,
#             'rateinfo/instructor_list.html',
#             {'instructor_list': Instructor.objects.all()}
#         )

class CourseCreate(View):
    form_class = CourseForm
    template_name = 'rateinfo/course_form.html'

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'form': self.form_class}
        )

    def post(self, request):
        # bound_form = self.form_class(request.POST)
        courseName = self.form_class.Course_Name
        courseDepart = self.form_class.Course_Department
        courseInstID = self.form_class.Course_Instructor_ID
    # if bound_form.is_valid():
        cursor = connection.cursor()
        cursor.execute(
            "SELECT Course_ID FROM rateinfo_Course ORDER BY Course_ID DESC LIMIT 1")
        CourseId = dict(cursor)[0] + 1
        query = 'INSERT INTO rateinfo_Course (Course_ID, Course_Name, Course_Department, Course_Instructor_ID_id) VALUES (%s, %s, %s, %s)', [CourseId, courseName, courseDepart, courseInstID];
        cursor.execute(query)
        # new_object = bound_form.save()
        # return redirect(new_object)
        # else:
        #     return render(
        #         request,
        #         self.template_name,
        #         {'form': bound_form}
        #     )

# def course_list_view(request):
#     course_list = Course.objects.all();
#     #course_list = Course.objects.none();
#     return render(request, 'rateinfo/course_list.html', {'course_list': course_list})
#
#
# class CourseUpdate(ObjectCreateMixin, View):
#     form_class = CourseForm
#     model = Course
#     template_name = 'rateinfo/course_form_update.html'
#
#     def get_object(self, pk):
#         return get_object_or_404(
#             self.model,
#             pk=pk
#         )
#
#     def get(self, request, pk):
#         course = self.get_object(pk)
#         context = {
#             'form': self.form_class(
#                 instance=course),
#             'course': course,
#         }
#         return render(
#             request, self.template_name, context
#         )
#
#     def post(self, request, pk):
#         course = self.get_object(pk)
#         bound_form = self.form_class(
#             request.POST, instance=course
#         )
#         if bound_form.is_valid():
#             new_course = bound_form.save()
#             return redirect(new_course)
#         else:
#             context = {
#                 'form': bound_form,
#                 'course': course,
#             }
#             return render(
#                 request,
#                 self.template_name,
#                 context
#             )
#
#
# class CourseDelete(ObjectCreateMixin, View):
#     def get(self, request, pk):
#         course = self.get_object(pk)
#         comment = course.comments.all()
#         if comment.count() > 0:
#             return render(
#                 request,
#                 'rateinfo/course_refuse_delete.html',
#                 {'course': course,
#                  'comments': comment,
#                  }
#             )
#         else:
#             return render(
#                 request,
#                 'rateinfo/course_confirm_delete.html',
#                 {'course': course}
#             )
#
#     def get_object(self, pk):
#         return get_object_or_404(
#             Course,
#             pk=pk)
#
#     def post(self, request, pk):
#         course = self.get_object(pk)
#         course.delete()
#         return redirect('rateinfo_course_list_urlpattern')


# class InstructorList(View):
#
#     def get(self, request):
#         value = request.GET.get('q')
#         if value:
#             instructorList = models.Instructor.objects.filter(Instructor_Name__contains=value)
#             return render(
#                 request,
#                 'rateinfo/instructor_list.html',
#                 {'instructor_list': models.Instructor.objects.filter(Instructor_Name__contains=value)}
#             )
#
#         return render(
#             request,
#             'rateinfo/instructor_list.html',
#             {'instructor_list': Instructor.objects.all()}
#         )
#
#
# class InstructorDetail(View):
#
#     def get(self, request, pk):
#         instructor = get_object_or_404(
#             Instructor,
#             pk=pk
#         )
#         instructorlist = instructor.courses.all(),
#         return render(
#             request,
#             'rateinfo/instructor_detail.html',
#             {'instructor': instructor, 'course_list': instructor.courses.all()}
#         )
#
#
# class InstructorCreate(ObjectCreateMixin, View):
#     form_class = InstructorForm
#     template_name = 'rateinfo/instructor_form.html'
#
#
# class InstructorUpdate(View):
#     form_class = InstructorForm
#     model = Instructor
#     template_name = 'rateinfo/instructor_form_update.html'
#
#     def get_object(self, pk):
#         return get_object_or_404(
#             self.model,
#             pk=pk
#         )
#
#     def get(self, request, pk):
#         instructor = self.get_object(pk)
#         context = {
#             'form': self.form_class(
#                 instance=instructor),
#             'instructor': instructor,
#         }
#         return render(
#             request, self.template_name, context
#         )
#
#     def post(self, request, pk):
#         instructor = self.get_object(pk)
#         bound_form = self.form_class(
#             request.POST, instance=instructor
#         )
#         if bound_form.is_valid():
#             new_instructor = bound_form.save()
#             return redirect(new_instructor)
#         else:
#             context = {
#                 'form': bound_form,
#                 'instrcutor': instructor,
#             }
#             return render(
#                 request,
#                 self.template_name,
#                 context
#             )
#
#
# class InstructorDelete(View):
#
#     def get(self, request, pk):
#         instructor = self.get_object(pk)
#         courses = instructor.courses.all()
#         if courses.count() > 0:
#             return render(
#                 request,
#                 'rateinfo/instructor_refuse_delete.html',
#                 {'instructor': instructor,
#                  'courses': courses,
#                  }
#             )
#         else:
#             return render(
#                 request,
#                 'rateinfo/instructor_confirm_delete.html',
#                 {'instructor': instructor}
#             )
#
#     def get_object(self, pk):
#         return get_object_or_404(
#             Instructor,
#             pk=pk)
#
#     def post(self, request, pk):
#         instructor = self.get_object(pk)
#         instructor.delete()
#         return redirect('rateinfo_instructor_list_urlpattern')


# def instructor_list_view(request):
#     instructor_list = Instructor.objects.all();
#     #course_list = Course.objects.none();
#     return render(request, 'rateinfo/instructor_list.html', {'instructor_list': instructor_list})

#
# class CommentList(View):
#
#     def get(self, request):
#         return render(
#             request,
#             'rateinfo/comment_list.html',
#             {'comment_list': Comment.objects.all()}
#         )
#
#
# class CommentDetail(View):
#
#     def get(self, request, pk):
#         comment = get_object_or_404(
#             Comment,
#             pk=pk
#         )
#         return render(
#             request,
#             'rateinfo/comment_detail.html',
#             {'comment': comment}
#         )
#
#
# class CommentCreate(ObjectCreateMixin, View):
#     form_class = CommentForm
#     template_name = 'rateinfo/comment_form.html'
#
#
# # def comment_list_view(request):
# #     comment_list = Comment.objects.all();
# #     #course_list = Course.objects.none();
# #     return render(request, 'rateinfo/comment_list.html', {'comment_list': comment_list})
#
#
# class UserList(View):
#
#     def get(self, request):
#         value = request.GET.get('q')
#         if value:
#             userList = models.User.objects.filter(User_Name__contains=value)
#             return render(
#                 request,
#                 'rateinfo/user_list.html',
#                 {'user_list': userList}
#             )
#
#         return render(
#             request,
#             'rateinfo/user_list.html',
#             {'user_list': User.objects.all()}
#         )
#
#
# class UserDetail(View):
#
#     def get(self, request, pk):
#         user = get_object_or_404(
#             User,
#             pk=pk
#         )
#         # instructor = course.courses.all(),
#         # commentlist = user.comments.all(),
#         groupchatReceive = user.groupchatrecieve.all(),
#         groupchatSent = user.groupchatsent.all(),
#         return render(
#             request,
#             'rateinfo/user_detail.html',
#             {'user': user, 'groupchat_receive': user.groupchatrecieve.all(), 'groupchat_sent': user.groupchatsent.all()}
#         )
#
#
# class UserCreate(ObjectCreateMixin, View):
#     form_class = UserForm
#     template_name = 'rateinfo/user_form.html'
#
#
# class UserUpdate(ObjectCreateMixin, View):
#     form_class = UserForm
#     model = User
#     template_name = 'rateinfo/user_form_update.html'
#
#     def get_object(self, pk):
#         return get_object_or_404(
#             self.model,
#             pk=pk
#         )
#
#     def get(self, request, pk):
#         user = self.get_object(pk)
#         context = {
#             'form': self.form_class(
#                 instance=user),
#             'user': user,
#         }
#         return render(
#             request, self.template_name, context
#         )
#
#     def post(self, request, pk):
#         user = self.get_object(pk)
#         bound_form = self.form_class(
#             request.POST, instance=user
#         )
#         if bound_form.is_valid():
#             new_user = bound_form.save()
#             return redirect(new_user)
#         else:
#             context = {
#                 'form': bound_form,
#                 'user': user,
#             }
#             return render(
#                 request,
#                 self.template_name,
#                 context
#             )
#
#
# class UserDelete(ObjectCreateMixin, View):
#     def get(self, request, pk):
#         user = self.get_object(pk)
#         groups = user.gps.all()
#         if groups.count() > 0:
#             return render(
#                 request,
#                 'rateinfo/user_refuse_delete.html',
#                 {'user': user,
#                  'groups': groups,
#                  }
#             )
#         else:
#             return render(
#                 request,
#                 'rateinfo/user_confirm_delete.html',
#                 {'user': user}
#             )
#
#     def get_object(self, pk):
#         return get_object_or_404(
#             User,
#             pk=pk)
#
#     def post(self, request, pk):
#         user = self.get_object(pk)
#         user.delete()
#         return redirect('rateinfo_user_list_urlpattern')


# def user_list_view(request):
#     user_list = User.objects.all();
#     #course_list = Course.objects.none();
#     return render(request, 'rateinfo/user_list.html', {'user_list': user_list})


# class GroupList(View):
#
#     def get(self, request):
#         return render(
#             request,
#             'rateinfo/group_list.html',
#             {'group_list': GP.objects.all()}
#         )

# def group_list_view(request):
#     group_list = GP.objects.all();
#     #course_list = Course.objects.none();
#     return render(request, 'rateinfo/group_list.html', {'group_list': group_list})
