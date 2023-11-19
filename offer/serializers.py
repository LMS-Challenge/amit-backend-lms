from rest_framework import serializers

from .models import offer


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = offer
        fields = ['id', 'course', 'description', 'enrolled_students',
                'max_capacity', 'current_enrollment', 'waiting_list',
                'start_date', 'end_date', 'new_price', 'discount', 'duration', 'status'
        ]
