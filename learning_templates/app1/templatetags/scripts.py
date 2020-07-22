from django import template 

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
        Remplace arg dans le value par un caractere de notre choix
    """
    return value.replace(arg,'TEKAM BRANDON LEE')

#register.filter('cut',cut)