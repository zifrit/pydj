from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

zodiac_signs = {
    'Aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'Taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'Gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'Cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'Leo': 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'Virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'Libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'Scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'Sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'Capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'Aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'Pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
}

elements_zodiac = {
    'Fire': ['Aries', 'Leo', 'Sagittarius'],
    'Earth': ['Taurus', 'Virgo', 'Capricorn'],
    'Air': ['Gemini', 'Libra', 'Aquarius'],
    'Water': ['Cancer', 'Scorpio', 'Pisces'],
}


def zodiac(request, name_zodiac):
    namezodiac = list(zodiac_signs)
    if str(name_zodiac).capitalize() in namezodiac:
        return render(request, 'test_video_code/zodiacs.html', {'zodiac': zodiac_signs[str(name_zodiac).capitalize()]})
    else:
        return render(request, 'test_video_code/zodiacs.html', {'zodiac': 'знака нету'})


def main(request):
    return render(request, 'test_video_code/href_zodiac.html', {'zodiac_signs': zodiac_signs})


def element_zodiac(request):
    return render(request, 'test_video_code/element_zodiac.html', {'elements_zodiac': elements_zodiac})


def element_to_zodiac(request, element_to_zodiac):
    return render(request, 'test_video_code/element_to_zodiac.html',
                  {'elements_zodiac': elements_zodiac[element_to_zodiac]})


def month_to_zodiac(request, month, day):
    return render(request, 'test_video_code/element_to_zodiac.html',
                  {'elements_zodiac': elements_zodiac[element_to_zodiac]})
