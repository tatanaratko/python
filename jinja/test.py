from jinja2 import Template


class Letter:
    def __init__(self, meetings, adresat):
        self.meetings = meetings
        self.adresat = adresat


class Meeting:
    def __init__(self, meet_name, meet_time, is_importent):
        self.meet_name = meet_name
        self.meet_time = meet_time
        self.is_importent = is_importent


class Adresat:
    def __init__(self, name, position, department, is_busy):
        self.name = name
        self.position = position
        self.department = department
        self.is_busy = is_busy


meet1 = Meeting('RTDM meeting', '13:45', True)
meet2 = Meeting('stendup', '12:30', False)
meet3 = Meeting('Techno', '11:30', False)
meet4 = Meeting('Retro', '19:45', True)

adresat1 = Adresat('Ира', 'начальник отдела', 'отдел трансформации', False)
letter1 = Letter([meet1, meet2, meet3, meet4], adresat1)


adresat2 = Adresat('Васян', 'программист', 'хуячечная', True)
letter2 = Letter([meet1, meet2, meet3, meet4], adresat2)

# Вывести отдельно важные встречи, неважные и в конце самую раннюю по времени

template_str = """ 
Здравствуйте, {{ zhopa.adresat.name }}!
Прошу прийти на встречи:
{% for meet in zhopa.meetings|selectattr("is_importent")|sort(attribute="meet_time") %}
    {{meet.meet_name}} : {{meet.meet_time}} 
{% endfor %}

{% for meet in zhopa.meetings|selectattr("is_importent", "false")|sort(attribute="meet_time") %}
    {{meet.meet_name}} : {{meet.meet_time}} 
{% endfor %}

Всего доброго!
"""

print(Template(template_str).render(zhopa=letter1))
