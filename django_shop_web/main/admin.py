from django.contrib import admin
from .models import ActivationEmail, AuthGroup, AuthGroupPermissions, AuthPermission, AuthUser, AuthUserGroups, AuthUserUserPermissions, Business, ConfirmString, \
                    DjangoAdminLog, DjangoContentType, DjangoMigrations, DjangoSession, Limitedtime, MainConfirmstring, MainImg, Record, SnippetsSnippet, \
                    SystemConfig, Udn, Users, Product

admin.site.register(ActivationEmail)
admin.site.register(AuthGroup)
admin.site.register(AuthGroupPermissions)
admin.site.register(AuthPermission)
admin.site.register(AuthUser)
admin.site.register(AuthUserGroups)
admin.site.register(AuthUserUserPermissions)
admin.site.register(Business)
admin.site.register(ConfirmString)
admin.site.register(DjangoAdminLog)
admin.site.register(DjangoContentType)
admin.site.register(DjangoMigrations)
admin.site.register(DjangoSession)
admin.site.register(Limitedtime)
admin.site.register(MainConfirmstring)
admin.site.register(MainImg)
admin.site.register(Record)
admin.site.register(SnippetsSnippet)
admin.site.register(SystemConfig)
admin.site.register(Udn)
admin.site.register(Users)
admin.site.register(Product)