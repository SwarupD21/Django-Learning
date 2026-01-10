from django.contrib import admin
from .models import Content,review,Store, Certificate

class ChaiReviewInline(admin.TabularInline):
  model = review
  extra = 1

class ChaiVarietyAdmin(admin.ModelAdmin):
  list_display = ('name', 'type', 'date_added')
  inlines = [ChaiReviewInline]

class StoreAdmin(admin.ModelAdmin):
  list_display = ('name', 'location')
  filter_horizontal = ('chai_varity',)

class ChaiCertificateAdmin(admin.ModelAdmin):
  list_display = ('chai', 'certificate', 'issued_date', 'valid_date')

admin.site.register(Content, ChaiVarietyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Certificate, ChaiCertificateAdmin)