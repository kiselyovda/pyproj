def fizz_buzz(start, stop):
    rez = 0
    for i in range(start, stop + 1):
        if i % 3 == 0 and i % 5 == 0:
            rez += i
    return rez

print('0-3:', fizz_buzz(0, 3))
print('0-5:', fizz_buzz(0, 5))
print('15-15:', fizz_buzz(15, 15))
print('1000-20000:', fizz_buzz(1000, 20000))

def plural_form(value, *args):
    output = ''
    if value % 10 == 1:
        output = args[0]
    if 1 < value % 10 < 5:
        output = args[1]
    if 10 < value < 21:
        output = args[2]
    if 5 <= value % 10 < 10 or value % 10 == 0:
        output = args[2]
    return output

print(1, plural_form(1, 'яблоко', 'яблока', 'яблок'))
print(3, plural_form(3, 'яблоко', 'яблока', 'яблок'))
print(5, plural_form(5, 'яблоко', 'яблока', 'яблок'))
print(11, plural_form(11, 'яблоко', 'яблока', 'яблок'))
print(121, plural_form(121, 'яблоко', 'яблока', 'яблок'))
print(125, plural_form(125, 'яблоко', 'яблока', 'яблок'))

def html(*args, **kwargs):
    def decorator(decorated_function):
        def wrapper(input_value):
            text = decorated_function(input_value)
            if kwargs:
                text = f'>{text}'
                for k, v in kwargs.items():
                    text = f' {k}="{v}"{text}'
                for tag in args:
                    text = f'<{tag}{text}</{tag}>'
            else:
                for tag in args:
                    text = f'<{tag}>{text}</{tag}>'
            return text
        return wrapper
    return decorator


@html('body')
@html('div', width=200, height=100)
@html('a', href='https://yandex.ru/')
def to_string(input_value):
    return str(input_value)


print(to_string('ссылка на яндекс'))