from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy

from .models import offer
from users.models import Student


# Create your views here.
class OfferListView(View):
    def get(self, request):
        offers = offer.objects.all()
        # Serialize and return the list of offers
        context = {
            'offers': offers
        }
        return render(request, 'offer/offer_list.html', context)


class OfferDetailView(View):
    def get(self, request, offer_id):
        offer_detail = get_object_or_404(offer, pk=offer_id)
        # Serialize and return the offer detail
        context = {
            'offer_detail': offer_detail
        }
        return render(request, 'offer/offer_detail.html', context)


class OfferCreateView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def post(self, request):
        # Create a new offer using request data
        try:
            new_offer = offer(
                course = request.POST.get('course'),
                description = request.POST.get('description'),
                max_capacity = request.POST.get('max_capacity'),
                start_date = request.POST.get('start_date'),
                end_date = request.POST.get('end_date'),
                new_price = request.POST.get('new_price'),
                discount = request.POST.get('discount'),
                duration = request.POST.get('duration'),
            )
            new_offer.save()
            return JsonResponse({'message': 'Offer created successfully!'}, status=201)
        except:
            return JsonResponse({'message': 'Offer creation failed!'}, status=400)

    success_url = reverse_lazy('offer_list')


class OfferUpdateView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def put(self, request, offer_id):
        offer_obj = get_object_or_404(offer, pk=offer_id)
        try:
            # Update fields from request
            offer_obj.description = request.POST.get('description')
            offer_obj.max_capacity = request.POST.get('max_capacity')
            offer_obj.start_date = request.POST.get('start_date')
            offer_obj.end_date = request.POST.get('end_date')
            offer_obj.new_price = request.POST.get('new_price')
            offer_obj.discount = request.POST.get('discount')
            offer_obj.duration = request.POST.get('duration')
            offer_obj.save()
            return JsonResponse({'message': 'Offer updated successfully!'})
        except:
            return JsonResponse({'message': 'Offer update failed!'}, status=400)

    success_url = reverse_lazy('offer_detail')


class OfferDeleteView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def delete(self, request, offer_id):
        offer_obj = get_object_or_404(offer, pk=offer_id)
        try:
            offer_obj.delete()
            return JsonResponse({'message': 'Offer deleted successfully!'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    success_url = reverse_lazy('offer_list')



class StudentEnrollmentView(View):
    def post(self, request, offer_id):
        student_id = request.POST.get('student_id')
        student = get_object_or_404(Student, id=student_id)
        offer_obj = get_object_or_404(offer, id=offer_id)

        if student in offer_obj.enrolled_students.all():
            return JsonResponse({'message': 'Student already enrolled'}, status=400)

        if offer_obj.enrolled_students.count() < offer_obj.max_capacity:
            offer_obj.enrolled_students.add(student)
            offer_obj.current_enrollment += 1
            offer_obj.save()
            return JsonResponse({'message': 'Student enrolled successfully'})
        else:
            if student not in offer_obj.waiting_list.all():
                offer_obj.waiting_list.add(student)
                return JsonResponse({'message': 'Added to waiting list as the course is at full capacity'}, status=200)
            else:
                return JsonResponse({'message': 'Student is already on the waiting list'}, status=400)


class EnrolledStudentsListView(View):
    def get(self, request, offer_id):
        offer_obj = get_object_or_404(offer, id=offer_id)
        enrolled_students = list(offer_obj.enrolled_students.all().values('id', 'first_name', 'last_name'))
        return JsonResponse({'enrolled_students': enrolled_students})


class WaitingListView(View):
    def get(self, request, offer_id):
        offer_obj = get_object_or_404(offer, id=offer_id)
        waiting_list_students = offer_obj.waiting_list.all().values('first_name', 'last_name')
        return JsonResponse({'waiting_list_students': list(waiting_list_students)})
