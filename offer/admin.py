from django.contrib import admin
from .models import offer, course

@admin.register(offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('course', 'original_price', 'discount', 'new_price', 'start_date', 'end_date', 'status')
    readonly_fields = ('original_price',)

    def original_price(self, obj):
        # Assuming there is a foreign key from Offer to Course named 'course'
        return f"${obj.course.course_price}"
    original_price.short_description = "Original Price"  # Optional: To set a header column name

