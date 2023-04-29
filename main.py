st1 = "Задаючи завдання додому, вчителі мітять у учнів, а потрапляють у батьків."
st2 = "Ніколи! Ніколи не нюхайте як кипить чайник."
st3 = "Математичні завдання - це єдине місце, де хтось може купити 60 кавунів і ніхто його не запитає навіщо?"
st4 = "Як тільки зібрався взятися за розум, закінчився навчальний рік."
st5 = "Зник собака, дуже розумна. Кулька, якщо ти зараз це читаєш, подзвони додому!"


def first_last(string, *args):
    string = string.lower()
    for letter in args:
        if letter.lower() in string:
            print(f'"{letter}" : {string.find(letter.lower()), string.rfind(letter.lower())}')
        else:
            print(f'"{letter}" : {None, None}')

first_last(st1, "з", "щ", "а")


def camel(string):
    new_string = ''
    count = 0
    for symbol in string:
        if symbol.isalpha():
            if count % 2 ==0:
                new_string += symbol.upper()
                count += 1
            else:
                new_string += symbol.lower()
                count += 1
        else:
            new_string += symbol
    return new_string

print(camel(st2))