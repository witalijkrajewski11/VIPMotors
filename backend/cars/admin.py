from django.contrib import admin
from cars import models


@admin.register(models.CarBrand)
class CarBrandAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CarBrandOverview)
class CarBrandOverview(admin.ModelAdmin):
    pass


@admin.register(models.CarModel)
class CarModelAdmin(admin.ModelAdmin):
    pass
