from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.core.exceptions import ValidationError
from .models import CustomUser  # Your custom user model
from django.contrib import messages

from .models import Student  # Import your Student model


# Create your views here.
# def register(request):
#     if request.user.is_authenticated and request.user.is_instructor:
#         return redirect('home')
        
#     if request.POST:
#         user_name=request.POST.get('username')
#         email=request.POST.get('email')
#         password=request.POST.get('password')
#         confirm_password=request.POST.get('confirm_password')

#         try:
#             validate_email(email)
#         except ValidationError:
#             messages.error(request, "Please enter a correct email address!")
#             return redirect('register')
        
#         try:
#             validator=ASCIIUsernameValidator()
#             validator(user_name)
#         except:
#             messages.error(request, ASCIIUsernameValidator.message)
#             return redirect('register')
        
#         if User.get_object_or_none(username=user_name):
#             messages.error(request, 'Username already exists')
#             return redirect('register')

#         if User.get_object_or_none(email=email):
#             messages.error(request, 'Email already exists!')
#             return redirect('register')

#         if password!=confirm_password:
#             messages.error(request, "Passwords don't match!")
#             return redirect('register')

#         user=User.objects.create(username=user_name, email=email)
#         user.set_password(password)
#         user.save()
#         messages.success(request, 'Account Created successfully!')
#         return redirect('login')
    
    # else:
    #     return render(request, 'user_interface/registeration.html')

from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import redirect, render

def custom_login(request):
    if request.user.is_authenticated:
        if request.user.is_instructor:
            return redirect('instructor/dashboard')
        elif not request.user.is_staff:
            return redirect('student/dashboard')
        elif request.user.is_superuser:
            return redirect('/admin')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email)
        print(password)
        

        # Authenticate the user based on email and password
        User = get_user_model()
        user = authenticate(request, email=email, password=password)

        if user is not None:
            print(user.is_instructor)
            # User exists and credentials are valid
            login(request, user)
            if user.is_instructor:
                print('login Done successfully')
                return redirect('instructor/dashboard')  # Redirect to instructor dashboard
            elif user.is_superuser and user.is_staff:
                return redirect('/admin')  # Redirect to student dashboard
        else:
            # User does not exist or invalid credentials
            # You can handle this case (e.g., show an error message)
            # For now, let's redirect to the signup page
            return redirect('student/signup')  # Replace 'signup' with your actual signup URL

    return render(request, 'users/login.html')






def student_signup(request):
    if request.method == 'POST':
        # Other student-specific fields as needed
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        date_of_birth = request.POST.get('date_of_birth')
        gender =  request.POST.get('gender')
        profile_image =  request.POST.get('profile_image')
        confirm_password = request.POST.get('confirm_password')
        
        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "Please enter a correct email address!")
            return redirect('signup')
        
       

        if Student.get_object_or_none(email=email):
            messages.error(request, 'Email already exists!')
            return redirect('signup')

        if password!=confirm_password:
            messages.error(request, "Passwords don't match!")
            return redirect('signup')
       

        # Create a new student user
        student = Student.objects.create_user(
            # Set other student-specific fields here
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            gender=gender,
            profile_image=profile_image,
           
        )

        # Log the student user in
        login(request, student)

        return redirect('')  # Redirect to student dashboard

    return render(request, 'users/signup.html')



def student_dashboard(request):
    return render(request, 'users/student_dashboard.html')



def instructor_dashboard(request):
    return render(request, 'users/instructor_dashboard.html')



def logoutUser(request):
    logout(request)
    return redirect('')