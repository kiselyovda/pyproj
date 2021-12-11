# def wrapper_over_decorator(decorator_parameter_1='', decorator_parameter_2=''):

#     print(f"""1. Я обертка над декоратором. Называй меня Главная обертка. Я буду создавать декоратор. У меня есть параметры:
#      - decorator_parameter_1: {decorator_parameter_1}
#      - decorator_parameter_2: {decorator_parameter_2}""")

#     def decorator(decorated_function):

#         print(f"""2. Я сам декоратор. Я подчиняюсь Главной обертке. Я вижу все, что есть у Главной обертки. Я тоже вижу параметры:
#         - decorator_parameter_1: {decorator_parameter_1}
#         - decorator_parameter_2: {decorator_parameter_2}
#         Еще я вижу декорируемую функцию decorated_function: {decorated_function}""")

#         def wrapper_over_decorated_function(*args, **kwargs):
#             print(f"""3. Я обертка над декорируемой функцией. Я подчиняюсь декоратору и Главной обертке, поэтому я вижу все, что есть у них:
#                   - параметр decorator_parameter_1: {decorator_parameter_1}
#                   - параметр decorator_parameter_2: {decorator_parameter_2}
#                   - функцию, которая есть у декоратора decorated_function: {decorated_function};
#                   - все аргументы, которые переданы при вызове декорируемой функции *args, **kwargs: {args}, {kwargs}."""
#                   )
#             result = decorated_function(*args, **kwargs)
#             return result

#         return wrapper_over_decorated_function

#     return decorator


# @wrapper_over_decorator('Hello', 'World')
# def div(a, b=1):
#     return a / b


# result_div = div(4, b=2)

# print(result_div)

# def fizz_buzz(start, stop):
#     rez = 0
#     for i in range(start, stop + 1):
#         if i % 3 == 0 and i % 5 == 0:
#             rez += i
#     return rez

# print('0-3:', fizz_buzz(0, 3))
# print('0-5:', fizz_buzz(0, 5))
# print('15-15:', fizz_buzz(15, 15))
# print('1000-20000:', fizz_buzz(1000, 20000))

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