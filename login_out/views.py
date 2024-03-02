#### 로그인/회원가입/로그아웃페이지입니다 ####


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
import pymysql




# Create your views here.
def login_view(request):
    if request.method == 'POST':
        userid = request.POST['username']
        userpw = request.POST['password']

        #### DB name ####
        with pymysql.connect(host='localhost', user='root', password='wlsdud1004', db='project', charset='utf8') as connection:
            cursor = connection.cursor(pymysql.cursors.DictCursor)

            SQL = '''SELECT * FROM project.user WHERE userid=%s AND userpw=%s'''
            cursor.execute(SQL, (userid, userpw))

            user = cursor.fetchone()

            if user is not None:
                print("인증성공")
                # login(request, user)
                return redirect('/main')  # 로그인 성공 시 이동할 페이지

    return render(request, "page_login.html")

def logout_view(request):
    logout(request)
    return redirect("user:login")

def signup_view(request):

    if request.method == "POST":
        print(request.POST)
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["id"]
        password = request.POST["password"]
        email = request.POST["email"]
        phone_number = request.POST["phone_number"]
        other_number = request.POST["other_number"]
        home_address = request.POST["home_address"]


        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.phone_number = phone_number
        user.other_number = other_number
        user.home_address = home_address
        user.save()

        return redirect("user:login")

    return render(request,"signup.html")
    # return render(request,"users/signup.html")
