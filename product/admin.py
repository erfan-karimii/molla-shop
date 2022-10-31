from django.contrib import admin
from .models import Category, Product,Color,GalleryImage, Size,Tags,ZirCategory , Comment
#-------------------STARTBAG------------


class SizeInlineBag(admin.TabularInline):
    model = Size
    extra = 0

class ColorInlineBag(admin.TabularInline):
    model = Color
    extra = 0

class GalleryInlineBag(admin.TabularInline):
    model = GalleryImage
    extra = 0

class CustomBag(admin.ModelAdmin):
    inlines = [
        SizeInlineBag,
        ColorInlineBag,
        GalleryInlineBag,
    ]
    # formfield_overrides = {
    #     models.CharField: {'widget': TextInput(attrs={'size':'50'})},
    # }

admin.site.register(Product,CustomBag)
admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(GalleryImage)
admin.site.register(Tags)
admin.site.register(ZirCategory)
admin.site.register(Comment)

#-----------------ENDBAG--------------
