from random import choice
from cars.constants import VIN_NUMBER_CHARS
from cars import models


def generate_unique_vin_code():
    while True:
        vin_code = ''.join(choice(VIN_NUMBER_CHARS) for char in range(17))

        if not models.Car.objects.filter(vin=vin_code).exists() \
                and not models.Car.objects.filter(vin=vin_code).exists():
            return vin_code
