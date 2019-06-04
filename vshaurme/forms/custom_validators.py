from wtforms import ValidationError
import re

def weak_checker(form, field):
    lowercase_letters = re.findall(r"[a-z]", field.data)
    uppercase_letters = re.findall(r"[A-Z]", field.data)
    numbers = re.findall(r"\d", field.data)
    letters = lowercase_letters + uppercase_letters
    all_symbols = letters + numbers
    if len(all_symbols) < 10:
        raise ValidationError("Пароль короче 10 символов")
    if len(numbers) == 0:
        raise ValidationError("Пароль состоит только из букв")
    if len(letters) == 0:
        raise ValidationError("Пароль состоит только из цифр")
    if len(uppercase_letters) == 0 or len(lowercase_letters) == 0:
        raise ValidationError("Пароль содержит буквы одного регистра")
