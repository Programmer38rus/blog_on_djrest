from django.contrib import admin
import app.models


# Register your models here.
@admin.register(app.models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(app.models.Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(app.models.User)
class UserAdmin(admin.ModelAdmin):
    pass