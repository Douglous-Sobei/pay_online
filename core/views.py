from django.shortcuts import render, redirect


def index(request):
    if request.user.is_authenticated:
        return redirect("core:index")
    return render(request, "core/index.html")
