from django.contrib import admin
from .models import SlideImg
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin



@admin.register(SlideImg)
class SpaceAdmin( SortableInlineAdminMixin,  admin.ModelAdmin):
    model = SlideImg
    list_display = ('admin_photo',)
    def admin_photo(self, obj):
        return mark_safe(f'<img src={obj.img.url} width="100" height="100">')
    admin_photo.short_description = 'Изображение'




admin.site.index_title = 'Космическое агенство'
admin.site.site_header = 'Личный кабинет для добавления фотографий'
admin.site.site_title = 'Личный кабинет'
