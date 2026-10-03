from django.contrib import admin
from site_setup.models import MenuLinks, SiteSetup

@admin.register(MenuLinks)
class MenuLinksAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'url_or_path')
    list_display_links = ('id', 'text')
    seartch_fields = ('text', 'id', 'url_or_path')

@admin.register(SiteSetup)
class SiteSetupAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
