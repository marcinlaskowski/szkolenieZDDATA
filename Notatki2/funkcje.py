"""
ARGS
"""

# def my_sum(param1, param2, *args): # param1 =1, param2=2, args = (3,4)
#     print(args)
#
#     for arg in args:
#         print(arg)
#
#     print(sum(args))
#
# my_sum(1,2)

#
# def my_sum(*args):
#     print(args)
#
#     for arg in args:
#         print(arg)
#
#     print(sum(args))
#
# my_sum()

"""
KWARGS
"""

#
# def my_sum(**kwargs):
#     print(kwargs)
#
#
# my_sum(param1=1,param2=2)

#
# def my_sum(param1, **kwargs):
#
#     print(param1)
#     print(kwargs)
#     # print(kwargs['param2'])
#     print(kwargs.get('param2', None))
#
#
# my_sum(param1=1,param2=20, param3=10)

#
# def my_sum(*args, **kwargs):
#     print("Args:", args)
#     print("Kwargs:", kwargs)
#
#
# my_sum(1, 2, 3, 4, param1=1, param2=20, param3=10)


"""
Funkcje domyślnie zwracają None
"""

#
# def say_hello():
#     print("Hello")
#
# print(say_hello())
#
#
# def say_hello():
#     return "Hello"
#
# print(say_hello())


"""
Adnotacje typów
"""


def get_fullname(name: str, surname: str) -> str:
    return f'{name} {surname}'


print(get_fullname("Jan", "Kowalski"))
print(get_fullname(True, 5))
