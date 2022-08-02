from rest_framework.validators import ValidationError

def phone_number(number):
    if len(str(number)) == 12 and str(number)[0:3] == "998":
        return number
    else:
        raise ValidationError("Telefon raqam noto'g'ri kiritildi!")

def full_name(name):
    if len(name.split(' ')) > 1:
        return name
    else:
        raise ValidationError("Ism-sharifingiz to'liq emas!")
