from django import template


register = template.Library()


@register.simple_tag()
def list_menu(authen=True):
    menu = [{'name': "Главная", 'url_name': "home"},
            {'name': "Пройти тестирование", 'url_name': "to_test"},
            {'name': "Посмотреть результаты", 'url_name': "watch_results"},
            ]
    if not authen:
        menu.pop(2)
        menu.pop(1)
    return menu


