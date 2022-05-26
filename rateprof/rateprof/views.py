from django.shortcuts import redirect


def redirect_root_view(request):
    return redirect('rateinfo_index_list_urlpattern')