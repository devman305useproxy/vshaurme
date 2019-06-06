from wtforms import ValidationError
import re

badwords = [
    "anal", "anus","jopa","arse","ass", "ochko","ass fuck","ass hole",
    "assfucker","joposhnik","glinomes","asshole","assshole","bastard","merzavets",
    "bitch", "suka","cuka","bliad",
    "black cock","bloody hell","boong","cock","huy","xyu","cockfucker",
    "cocksuck","cocksucker","coon","coonnass","crap",
    "cunt","pizda","cyberfuck","damn","darn","dick","dirty",
    "douche","gondon","dummy","erect","erection","erotic","escort",
    "fag","faggot","fuck","Fuck off","fuck you","fuckass",
    "fuckhole","god damn","gook","hard core","hardcore",
    "homoerotic","hore","lesbian","lesbians","mother fucker",
    "motherfuck","motherfucker","negro","nigger","nigga", "orgasim",
    "orgasm","penis","penisfucker","piss","piss off",
    "porn","porno","pornography","pussy","retard","dolboeb",
    "sadist","sex","sexy","shit","govno","slut","shmara","son of a bitch","such",
    "suck","tits","viagra","whore","xxx",
]

def bad_words_checker(form, field):
    for word in badwords:
        if re.search(r'{}'.format(word), field.data.lower()):
            raise ValidationError("Имя пользователя содержит нецензурное сочетание букв")

def weak_pass_checker(form, field):
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
