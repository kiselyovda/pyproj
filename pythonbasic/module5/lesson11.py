def wrapper_over_decorator(decorator_parameter_1='', decorator_parameter_2=''):

    print(f"""1. Я обертка над декоратором. Называй меня Главная обертка. Я буду создавать декоратор. У меня есть параметры:
     - decorator_parameter_1: {decorator_parameter_1}
     - decorator_parameter_2: {decorator_parameter_2}""")

    def decorator(decorated_function):

        print(f"""2. Я сам декоратор. Я подчиняюсь Главной обертке. Я вижу все, что есть у Главной обертки. Я тоже вижу параметры:
        - decorator_parameter_1: {decorator_parameter_1}
        - decorator_parameter_2: {decorator_parameter_2}
        Еще я вижу декорируемую функцию decorated_function: {decorated_function}""")

        def wrapper_over_decorated_function(*args, **kwargs):
            print(f"""3. Я обертка над декорируемой функцией. Я подчиняюсь декоратору и Главной обертке, поэтому я вижу все, что есть у них:
                  - параметр decorator_parameter_1: {decorator_parameter_1}
                  - параметр decorator_parameter_2: {decorator_parameter_2}
                  - функцию, которая есть у декоратора decorated_function: {decorated_function};
                  - все аргументы, которые переданы при вызове декорируемой функции *args, **kwargs: {args}, {kwargs}."""
                  )
            result = decorated_function(*args, **kwargs)
            return result

        return wrapper_over_decorated_function

    return decorator


@wrapper_over_decorator('Hello', 'World')
def div(a, b=1):
    return a / b


result_div = div(4, b=2)

print(result_div)