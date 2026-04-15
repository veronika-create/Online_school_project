from django.contrib import admin


from testing.models import Test

@admin.register (Test)

class TestAdmin(admin.ModelAdmin):
	list_display = ('question',)



