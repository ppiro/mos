from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from .models import Payment, PaymentInfo, MembershipPeriod, ContactInfo, KindOfMembership, MembershipFee, BankCollectionMode


class ContactInfoInline(admin.StackedInline):
    model = ContactInfo
    max_num = 1


class PaymentInfoInline(admin.StackedInline):
    model = PaymentInfo
    max_num = 1


class MembershipPeriodInline(admin.TabularInline):
    model = MembershipPeriod


class PaymentInline(admin.TabularInline):
    model = Payment
    fields = ('date', 'amount', 'method')
    ordering = ('date',)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
    list_filter = ['user']
    list_display = ['date', 'method', 'user', 'amount', 'original_file', 'original_line']
    list_display_links = None

class MembershipFeeInline(admin.TabularInline):
    model = MembershipFee
    ordering = ('start',)

@admin.register(KindOfMembership)
class KindOfMembershipAdmin(admin.ModelAdmin):
    inlines = [MembershipFeeInline]

@admin.register(BankCollectionMode)
class BankCollectionModeAdmin(admin.ModelAdmin):
    pass

admin.site.unregister(User)


@admin.register(User)
class MemberAdmin(UserAdmin):
    inlines = [ContactInfoInline, PaymentInfoInline, MembershipPeriodInline,
               PaymentInline]
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff',
                    'is_active')
    list_filter = ('is_staff', 'is_superuser', 'paymentinfo__bank_collection_mode')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)
