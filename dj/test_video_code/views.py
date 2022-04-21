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
    if (day >= 22 and month == 12) or (day <= 20 and month == 1):
        zodiac = zodiac_signs['Capricorn']
    elif (day >= 21 and month == 1) or (day <= 19 and month == 2):
        zodiac = zodiac_signs['Aquarius']
    elif (20 <= day < 28 and month == 2) or (day <= 20 and month == 3):
        zodiac = zodiac_signs['Pisces']
    elif (day >= 21 and month == 3) or (day <= 20 and month == 4):
        zodiac = zodiac_signs['Aries']
    elif (day >= 21 and month == 4) or (day <= 21 and month == 5):
        zodiac = zodiac_signs['Taurus']
    elif (day >= 22 and month == 5) or (day <= 21 and month == 6):
        zodiac = zodiac_signs['Gemini']
    elif (day >= 22 and month == 6) or (day <= 23 and month == 7):
        zodiac = zodiac_signs['Cancer']
    elif (day >= 24 and month == 7) or (day <= 23 and month == 8):
        zodiac = zodiac_signs['Leo']
    elif (day >= 24 and month == 8) or (day <= 23 and month == 9):
        zodiac = zodiac_signs['Virgo']
    elif (day >= 24 and month == 9) or (day <= 23 and month == 10):
        zodiac = zodiac_signs['Libra']
    elif (day >= 24 and month == 10) or (day <= 23 and month == 11):
        zodiac = zodiac_signs['Scorpio']
    elif (day >= 23 and month == 11) or (day <= 21 and month == 12):
        zodiac = zodiac_signs['Sagittarius']
    else:
        zodiac = 'нету такого знака зодиака'
    return render(request, 'test_video_code/zodiacs.html', {'zodiac': zodiac})
