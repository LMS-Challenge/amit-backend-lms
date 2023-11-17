# from django.test import TestCase
# from django.utils import timezone
# from django.urls import reverse

# from rest_framework.test import APIClient
# from rest_framework import status

# from .models import course, Content, Assignment, Quiz, Feedback
# from users.models import Student, Instructor, CustomUser

# # Create your tests here.
# class PublicCourseApiTests(TestCase):
#     """Test unauthenticated course API access"""
    
#     def setUp(self):
#         self.client = APIClient()
    
#     def test_login_required(self):
#         """Test that login is required for retrieving course"""
#         res = self.client.get(reverse('course_list'))
#         self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


# class PrivateCourseApiTests(TestCase):
#     """Test authenticated course API access"""
    
#     def setUp(self):
#         self.client = APIClient()

#         self.admin = CustomUser.objects.create_superuser(
#             email='admin@admin.com',
#             password='admin'
#         )
#         self.instructor = Instructor.objects.create(
#             email='instructor@example.com',
#             name='Instructor Name',
#             title='Dr.',
#             gender='M',
#             specialization='Computer Science',
#             password='testpassword123',  
#             is_instructor=True,
#             is_staff=True
#         )

#         self.student = Student.objects.create(
#             email='student@example.com',
#             first_name='Student',
#             last_name='User',
#             date_of_birth='2000-01-01',
#             gender='F',
#             password='studentpassword123',  
#         )

#         self.course = course.objects.create(
#             course_name='Test course',
#             course_description='Test Description',
#             category='development',
#             course_credit_hours=10,
#             course_price=100,
#             certificate='none',
#             course_image='none',
#             rating=5
#         )

#     def test_course_list_view(self):
#         url = reverse('course_list')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertContains(response, 'Test course')

#     def test_course_detail_view(self):
#         url = reverse('course_detail', args=[course.id])
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertContains(response, 'Test course')

#     def test_course_creation(self):
#         """Test that instructors or admins can create courses."""
        
#         # Admin user creates a course
#         self.client.force_authenticate(user=self.admin)
#         payload = {
#             'course_name': 'New Course',
#             'course_description': 'New Description',
#             'category': 'development',
#             'course_credit_hours': 3,
#             'course_price': 100,
#             'certificate': 'none',
#             'course_image': 'none',
#             'rating': 5
#         }
#         res = self.client.post(reverse('course_add'), payload)
#         self.assertEqual(res.status_code, status.HTTP_302_FOUND)

#         # Test for instructor user
#         self.client.force_authenticate(self.instructor)
#         res = self.client.post(reverse('course_add'), payload)
#         self.assertEqual(res.status_code, status.HTTP_302_FOUND)

#         # Test for student user (should not be allowed)
#         self.client.force_authenticate(self.student)
#         res = self.client.post(reverse('course_add'), payload)
#         self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

#     def test_course_update_view(self):
#         # Admin user updates the course
#         self.client.force_authenticate(user=self.admin)
#         updated_payload = {
#             'course_name': 'Updated Course',
#             'course_description': 'Updated Description',
#             'category': 'development',
#             'course_credit_hours': 3,
#             'course_price': 100,
#             'certificate': 'none',
#             'course_image': 'none',
#             'rating': 5
#         }
#         url = reverse('course_update', args=[self.course.id])
#         res = self.client.post(url, updated_payload)
#         self.assertEqual(res.status_code, status.HTTP_302_FOUND)

#         # Test for instructor user
#         self.client.force_authenticate(self.instructor)
#         res = self.client.post(url, updated_payload)
#         self.assertEqual(res.status_code, status.HTTP_302_FOUND)

#         # Test for student user (should not be allowed)
#         self.client.force_authenticate(self.student)
#         res = self.client.post(url, updated_payload)
#         self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

#     def test_course_delete_view(self):
#         # Admin user deletes the course
#         self.client.force_authenticate(user=self.admin)
#         url = reverse('course_delete', args=[self.course.id])
#         res = self.client.post(url)
#         self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertFalse(course.objects.filter(id=self.course.id).exists())

#         # Re-create the course
#         self.course = course.objects.create(
#             course_name='Test course',
#             course_description='Test Description',
#             category='development',
#             course_credit_hours=10,
#             course_price=100,
#             certificate='none',
#             course_image='none',
#             rating=5
#         )

#         # Test for instructor user
#         self.client.force_authenticate(user=self.instructor)
#         res = self.client.post(url)
#         self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertFalse(course.objects.filter(id=self.course.id).exists())

#         # Re-create the course
#         self.course = course.objects.create(
#             course_name='Test course',
#             course_description='Test Description',
#             category='development',
#             course_credit_hours=10,
#             course_price=100,
#             certificate='none',
#             course_image='none',
#             rating=5
#         )

#         # Test for student user (should not be allowed)
#         self.client.force_authenticate(user=self.student)
#         res = self.client.post(url)
#         self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)
#         self.assertTrue(course.objects.filter(id=self.course.id).exists())
        
#     def test_content_creation(self):
#         # Test that only instructors or admins can create content
#         self.client.force_authenticate(user=self.instructor)
#         content_payload = {
#             'course': self.course.id,
#             'content_description': 'Test Content'
#         }
#         res = self.client.post(reverse('content_add'), content_payload)
#         self.assertEqual(res.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Content.objects.count(), 1)

#     def test_assignment_creation(self):
#         # Test that only instructors or admins can create assignments
#         self.client.force_authenticate(user=self.instructor)
#         assignment_payload = {
#             'course': self.course.id,
#             'title': 'Test Assignment',
#             'explain_assignments': 'Test Explanation',
#             'due_date': timezone.now()
#         }
#         url = reverse('assignment_add', kwargs={'pk': self.course.id})
#         res = self.client.post(url, assignment_payload)
#         self.assertEqual(res.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Assignment.objects.count(), 1)

#     def test_quiz_creation(self):
#         # Test that only instructors or admins can create quizzes
#         self.client.force_authenticate(user=self.instructor)
#         quiz_payload = {
#             'course': self.course.id,
#             'quiz_title': 'Test Quiz',
#             'quiz_deadline': timezone.now()
#         }
#         url = reverse('quiz_add', kwargs={'pk': self.course.id})
#         res = self.client.post(url, quiz_payload)
#         self.assertEqual(res.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Quiz.objects.count(), 1)

#     def test_feedback_creation(self):
#         # Create a Feedback instance to make sure it can be created
#         course = course.objects.get(course_name='Test course')
#         student = Student.objects.get(name='Student1')
#         feedback = Feedback.objects.create(
#             course=course,
#             student=student,
#             rating=5,
#             comment='Great course!'
#         )
#         expected_str = f"Feedback for {course.course_name} by {student.name}"
#         self.assertEqual(feedback.__str__(), expected_str)

#     # def tearDown(self):
#     #     self.client.logout()