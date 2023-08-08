from djchoices import DjangoChoices, ChoiceItem


class FuelType(DjangoChoices):
    gasoline = ChoiceItem('gasoline', 'Gasoline')
    diesel = ChoiceItem('diesel', 'Diesel')
    hybrid = ChoiceItem('hybrid', 'Hybrid')
    electric = ChoiceItem('electric', 'Electric')


class TransmissionType(DjangoChoices):
    manual = ChoiceItem('manual', 'Manual')
    automatic = ChoiceItem('automatic', 'Automatic')
    robotic = ChoiceItem('robotic', 'Robotic')
    variable = ChoiceItem('variable', 'Variable')


class DrivetrainType(DjangoChoices):
    fwd = ChoiceItem('fwd', 'FWD')
    rwd = ChoiceItem('rwd', 'R  WD')
    _4wd = ChoiceItem('4wd', '4WD')


VIN_NUMBER_CHARS = 'QWERTYPASDFGHJKLZXCVBNM123456789'

DEFAULT_CREDIT_MONTH = 60
TAX_PERCENTS = 5
VIP_MOTORS_PAYMENT_FEE = 4

