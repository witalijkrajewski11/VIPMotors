from djchoices import DjangoChoices, ChoiceItem


class NotificationsWhen(DjangoChoices):
    right_now = ChoiceItem('right_now', 'Right Now')
    end_of_the_day = ChoiceItem('end_of_the_day', 'End of the Day')
    never = ChoiceItem('never', 'Never')


class MemberType(DjangoChoices):
    member = ChoiceItem('member', 'Member')
    admin = ChoiceItem('admin', 'Admin')
