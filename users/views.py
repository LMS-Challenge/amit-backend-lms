from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import CustomUser  # Your custom user model
from .models import Student  # Import your Student model


# Create your views here.

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Authenticate the user based on email and password
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            # User exists and credentials are valid
            login(request, user)
            if user.is_instructor:
                return redirect('instructor/dashboard')  # Redirect to instructor dashboard
            else:
                return redirect('student/dashboard')  # Redirect to student dashboard
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
        profile_image =  request.POST.get(profile_image)
       

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

        return redirect('student_dashboard')  # Redirect to student dashboard

    return render(request, 'users/student_signup.html')



def student_dashboard(request):
    return render(request, 'users/student_dashboard.html')



def instructor_dashboard(request):
    return render(request, 'users/instructor_dashboard.html')