from django.urls import path
from rateinfo.views import (
    IndexList,
    CourseList,
    CourseDetail,
    CourseCreate,

)

urlpatterns = [
    path('index/',
         IndexList.as_view(),
         name='rateinfo_index_list_urlpattern'
         ),
    # path('comment/',
    #      CommentList.as_view(),
    #      name='rateinfo_comment_list_urlpattern'
    #      ),
    # path('comment/<int:pk>',
    #      CommentDetail.as_view(),
    #      name='rateinfo_comment_detail_urlpattern'
    #      ),
    # path('comment/create/',
    #      CommentCreate.as_view(),
    #      name='rateinfo_comment_create_urlpattern'
    #      ),
    path('course/',
         CourseList.as_view(),
         name='rateinfo_course_list_urlpattern'
         ),
    # path('course/search/',
    #      CourseSearch,
    #      name='rateinfo_course_search_urlpattern'
    # #      ),
    path('course/<int:pk>',
         CourseDetail.as_view(),
         name='rateinfo_course_detail_urlpattern'
         ),
    path('course/create/',
         CourseCreate.as_view(),
         name='rateinfo_course_create_urlpattern'
         ),
    # path('course/update/<int:pk>',
    #      CourseUpdate.as_view(),
    #      name='rateinfo_course_update_urlpattern'
    #      ),
    # path('course/delete/<int:pk>',
    #      CourseDelete.as_view(),
    #      name='rateinfo_course_delete_urlpattern'
    #      ),
    # path('group/',
    #      GroupList.as_view(),
    #      name='rateinfo_group_list_urlpattern'
    #      ),
    # path('instructor/',
    #      InstructorList.as_view(),
    #      name='rateinfo_instructor_list_urlpattern'
    #      ),
    # path('instructor/<int:pk>',
    #      InstructorDetail.as_view(),
    #      name='rateinfo_instructor_detail_urlpattern'
    #      ),
    # path('instructor/create/',
    #      InstructorCreate.as_view(),
    #      name='rateinfo_instructor_create_urlpattern'
    #      ),
    # path('instructor/update/<int:pk>',
    #      InstructorUpdate.as_view(),
    #      name='rateinfo_instructor_update_urlpattern'
    #      ),
    # path('instructor/delete/<int:pk>',
    #      InstructorDelete.as_view(),
    #      name='rateinfo_instructor_delete_urlpattern'
    #      ),
    # path('user/',
    #      UserList.as_view(),
    #      name='rateinfo_user_list_urlpattern'
    #      ),
    # path('user/<int:pk>',
    #      UserDetail.as_view(),
    #      name='rateinfo_user_detail_urlpattern'
    #      ),
    # path('user/create/',
    #      UserCreate.as_view(),
    #      name='rateinfo_user_create_urlpattern'
    #      ),
    # path('user/update/<int:pk>',
    #      UserUpdate.as_view(),
    #      name='rateinfo_user_update_urlpattern'
    #      ),
    # path('user/delete/<int:pk>',
    #      UserDelete.as_view(),
    #      name='rateinfo_user_delete_urlpattern'
    #      ),
]
