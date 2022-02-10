from django import template

register = template.Library()


censor_list = ['гниль', 'гнида', 'гандон', 'блядь', 'гуманитарий', 'пес']


@register.filter(name='censor')
def censor(value):
    value1 = (str(value).split())
    for i in censor_list:
        for j in value1:
            if j == i:
                value1.remove(i)
    value = ' '.join(value1)

    return str(value)