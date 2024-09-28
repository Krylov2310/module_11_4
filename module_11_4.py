import sys

print('\033[30m\033[47mДомашнее задание по теме "Интроспекция".\033[0m')
print('\033[30m\033[47mЦель: Закрепить знания об интроспекции в Python.\033[0m')
print('\033[30m\033[47mСтудент Крылов Эдуард Васильевич\033[0m')
print('\033[30m\033[47mДата: 28.09.2024г.\033[0m')
thanks = '\033[30m\033[47mБлагодарю за внимание :-)\033[0m'
print()


def introspection_info(obj):
    type_obj = type(obj).__name__
    attributes_obj = dir(obj)
    methods_obj = [method_obj for method_obj in attributes_obj if callable(getattr(obj, method_obj))]
    color = ''
    if type(obj) is str:
        color = '[32m'
    elif type(obj) is int:
        color = '[34m'
        # obj += 15
    elif type(obj) is list:
        color = '[31m'
    elif type(obj) is dict:
        color = '[35m'
    elif type(obj) is float:
        color = '[36m'
    print(f'Тип объекта "type": \033{color}{obj} = {type_obj}\033[0m')
    module_obj = obj.__class__.__module__
    other_obj = sys.platform
    info_obj = [f'Атрибуты объекта "attributes": {attributes_obj}, '
                f'Методы объекта "methods": {methods_obj}, '
                f'Модуль, к которому объект принадлежит "module": {module_obj}, '
                f'Другие интересные свойства объекта "other: {other_obj}']

    return info_obj


# Пример работы:
list_set = ['Привет, я Эд :-)', 23, 3.143, {1: 'a'}, [1, 'Hello!', 5.45], 42]

for i in list_set:
    number_info = introspection_info(i)
    print(number_info)
print()
print(thanks)
