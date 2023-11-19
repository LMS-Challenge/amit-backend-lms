from django.contrib import admin

from .models import offer, course


@admin.register(offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('course', 'original_price', 'discounted_price', 'new_price', 'start_date', 'end_date', 'status')
    readonly_fields = ('original_price', 'discounted_price',)

    def original_price(self, obj):
        # Assuming there is a foreign key from Offer to Course named 'course'
        return f"${obj.course.course_price}"

    def discounted_price(self, obj):
        # Assuming there is a foreign key from Offer to Course named 'course'
        return f"${obj.course.course_price - obj.discount}" if obj.new_price else "N/A"

    def save_model(self, request, obj, form, change):
        obj.full_clean()  # This will call the clean method
        super().save_model(request, obj, form, change)