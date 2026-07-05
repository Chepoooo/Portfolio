from django.contrib import admin
from .models import Project, Social, Technology


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title",)
    filter_horizontal = ("technologies",)


admin.site.register(Social)
