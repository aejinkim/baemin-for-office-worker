from django.contrib.auth import (
    authenticate,
    login as auth_login,
    logout as auth_logout,
)
# login 이 위에도 있고 아래도 있어서 두개가 넘어간것으로 생각하여 에러가남. 따라서 위의 로그인을 더 명확하게 지정함
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    ctx = {}
    return render(request, "index.html", ctx)

def login(request):
    ctx = {}
    return render(request, "login.html", ctx)

    if request.method == "GET":
        pass
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/partner/")
            # partner의 메인 페이지로 넘겨줌
        else:
            ctx.update({"error":"사용자가 없습니다."})


def logout(request):
    auth_logout(request)
    return redirect("/partner/")


def signup(request):
    if request.method == "GET":
        pass
    elif request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        # print(username,email, password)

        user = User.objects.create_user(username, email, password)
        # Article.objects.creat(title="", content="")


    ctx = {}
    return render(request, "signup.html", ctx)
# signup.html 안에 input과 id가 있음
