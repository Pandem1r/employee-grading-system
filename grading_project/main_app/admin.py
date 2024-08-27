from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.utils.html import format_html
from django import forms
from django.urls import reverse
from main_app.models import *

from django.contrib.auth.models import User


def user_str(self):
    full_name = self.get_full_name()
    return full_name if full_name else self.username


User.add_to_class("__str__", user_str)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'position', 'ratings', 'get_report_button']
    search_fields = ['user__first_name', 'user__last_name', 'position__position_name', 'ratings']

    def full_name(self, obj):
        full_name = obj.user.get_full_name()
        return full_name if full_name else obj.user.username
    full_name.short_description = 'Юзер'

    def get_report_button(self, obj):
        return format_html('<a class="button" href="{}">Сформировать отчет</a>', reverse('admin:user_grading_report', args=[obj.pk]))
    get_report_button.short_description = 'Отчет'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('report/<int:profile_id>/', self.admin_site.admin_view(self.user_grading_report), name='user_grading_report'),
        ]
        return custom_urls + urls

    def user_grading_report(self, request, profile_id):
        profile = self.get_object(request, profile_id)
        grading_records = Grading.objects.filter(user=profile.user)

        return render(request, 'admin/user_grading_report.html', {
            'profile': profile,
            'grading_records': grading_records,
        })


class CriteriaAdmin(admin.ModelAdmin):
    list_display = ['title', 'standard_in_points', 'table_name']
    search_fields = ['title', 'standard_in_points', 'table_title__table']

    def table_name(self, obj):
        return obj.table_title.table

    table_name.short_description = 'Название таблицы'


# class GradingAdminForm(forms.ModelForm):
#     user = forms.ModelChoiceField(
#         queryset=User.objects.all(),
#         label='Юзер',
#         widget=forms.Select,
#         to_field_name='id',
#         empty_label=None,
#     )
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['user'].label_from_instance = lambda obj: f"{obj.get_full_name()}"
#
#     class Meta:
#         model = Grading
#         fields = '__all__'


class GradingAdmin(admin.ModelAdmin):
    #form = GradingAdminForm
    list_display = ['full_name', 'criteria_title', 'work_done', 'rating']
    search_fields = ['user__first_name', 'user__last_name', 'used_standard__title', 'work_done', 'rating']

    def criteria_title(self, obj):
        return obj.used_standard.title

    def full_name(self, obj):
        return obj.user.get_full_name()

    full_name.short_description = 'Юзер'

    criteria_title.short_description = 'Наименование работ'


class TableAdmin(admin.ModelAdmin):
    list_display = ['table']
    search_fields = ['table']


class PositionsAdmin(admin.ModelAdmin):
    list_display = ['position_name']
    search_fields = ['position_name']


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Criteria, CriteriaAdmin)
admin.site.register(Grading, GradingAdmin)
admin.site.register(Table, TableAdmin)
admin.site.register(Positions, PositionsAdmin)
