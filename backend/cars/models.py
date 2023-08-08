from django.db import models
from decimal import Decimal
from ckeditor.fields import RichTextField

from cars import constants, utils

SPECIAL_OFFER_HELP_TEXT = "Vehicle incentives and rebates are programs made available by car manufacturers to " \
                          "encourage vehicle sales by providing consumers with cash allowances or favorable " \
                          "financing/lease rates. Incentives can vary by location, vehicle configuration, as well " \
                          "as the buyer's method of payment (cash purchase, financing, lease). Some incentives can " \
                          "be stacked with other incentive programs, and some have eligibility conditions that" \
                          " must be met to qualify. Additional incentives are sometimes targeted to customer " \
                          "segment groups like college graduates, military members, etc. Incentives are normally " \
                          "subject to change and governed by specific eligibility rules. Please see your local dealer " \
                          "for details on incentives that might be available to you."


class AbstractReference(models.Model):
    name = models.CharField(max_length=255)
    image = models.FileField(upload_to='images/common_images/%Y/%m/%d')

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class CarBrand(AbstractReference):
    special_offer_discount = models.IntegerField(blank=True, null=True, default=0, help_text=SPECIAL_OFFER_HELP_TEXT)


class CarModel(AbstractReference):
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.brand.name} {self.name}'


class CarType(AbstractReference):
    pass


class CarBrandOverview(models.Model):
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    html_text = RichTextField()

    def __str__(self):
        return f'{self.brand.name} Overview'


class Car(models.Model):
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    car_type = models.ForeignKey(CarType, on_delete=models.SET_NULL, null=True, blank=True)
    engine = models.CharField(max_length=255)
    year = models.PositiveIntegerField(default=2023)
    transmission = models.CharField(
        max_length=255,
        choices=constants.TransmissionType.choices)
    drivetrain = models.CharField(
        max_length=255,
        choices=constants.DrivetrainType.choices)
    fuel = models.CharField(
        max_length=255,
        choices=constants.FuelType.choices)
    vin = models.CharField(max_length=255, unique=True, blank=True, null=True)
    date_created = models.DateField(auto_now_add=True)
    location = models.CharField(max_length=255)
    exterior = models.CharField(max_length=255)
    mileage = models.PositiveIntegerField()
    interior = models.CharField(max_length=255)
    consumption = models.CharField(max_length=255, blank=True, null=True)
    power_reserve = models.CharField(max_length=255, blank=True, null=True)
    stock_number = models.PositiveBigIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    thumbnail = models.FileField(upload_to='new_car_images/%Y/%m/%d')

    def __str__(self):
        return self.car_full_name

    def save(self, *args, **kwargs):
        if not self.vin:
            self.vin = utils.generate_unique_vin_code()
        super().save(*args, **kwargs)

    @property
    def tax_amount(self):
        if self.car_model.brand.special_offer_discount:
            return (self.price - self.car_model.brand.special_offer_discount) * (Decimal(constants.TAX_PERCENTS) / 100)
        return self.price * (Decimal(constants.TAX_PERCENTS) / 100)

    @property
    def payment_fee(self):
        if self.car_model.brand.special_offer_discount:
            return (self.price - self.car_model.brand.special_offer_discount) * \
                (Decimal(constants.VIP_MOTORS_PAYMENT_FEE) / 100)
        return self.price * (Decimal(constants.VIP_MOTORS_PAYMENT_FEE) / 100)

    @property
    def credit_price(self):
        return self.total_price / Decimal(constants.DEFAULT_CREDIT_MONTH)

    @property
    def total_price(self):
        if self.car_model.brand.special_offer_discount:
            return self.price - self.car_model.brand.special_offer_discount + self.tax_amount + self.payment_fee
        return self.price + self.tax_amount + self.payment_fee

    @property
    def car_full_name(self):
        return f'{self.car_model.brand.name} {self.car_model.name}'

    @property
    def is_new_car(self):
        return not bool(self.mileage)
