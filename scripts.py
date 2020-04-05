from functools import wraps
from random import choice
from datacenter.models import Chastisement, Commendation, Lesson, Mark, Schoolkid
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist

COMMENDATIONS = ["Молодец!",
                 "Отлично!",
                 "Хорошо!",
                 "Гораздо лучше, чем я ожидал!",
                 "Ты меня приятно удивил!",
                 "Великолепно!",
                 "Прекрасно!",
                 "Ты меня очень обрадовал!",
                 "Именно этого я давно ждал от тебя!",
                 "Сказано здорово – просто и ясно!",
                 "Ты, как всегда, точен!",
                 "Очень хороший ответ!",
                 "Талантливо!",
                 "Ты сегодня прыгнул выше головы!",
                 "Я поражен!",
                 "Уже существенно лучше!",
                 "Потрясающе!",
                 "Замечательно!",
                 "Прекрасное начало!",
                 "Так держать!",
                 "Ты на верном пути!",
                 "Здорово!",
                 "Это как раз то, что нужно!",
                 "Я тобой горжусь!",
                 "С каждым разом у тебя получается всё лучше!",
                 "Мы с тобой не зря поработали!",
                 "Я вижу, как ты стараешься!",
                 "Ты растешь над собой!",
                 "Ты многое сделал, я это вижу!",
                 "Теперь у тебя точно все получится!"]


def get_schoolkid(decorated_function):
    @wraps(decorated_function)
    def wrapper(child_name, *args, **kwargs):
        try:
            schoolkid = Schoolkid.objects.get(full_name__contains=child_name)
        except MultipleObjectsReturned:
            print(f"Ошибка! С именем {child_name} найдено больше одного ученика. Уточните запрос.")
        except ObjectDoesNotExist:
            print(f"Ошибка! Ученик {child_name} не найден. Проверьте запрос.")
        else:
            decorated_function(schoolkid, *args, **kwargs)

    return wrapper


@get_schoolkid
def fix_marks(schoolkid):
    Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3]).update(points=5)


@get_schoolkid
def remove_chastisements(schoolkid):
    Chastisement.objects.filter(schoolkid=schoolkid).delete()


@get_schoolkid
def create_commendation(schoolkid, subject_title):
    commendation = choice(COMMENDATIONS)
    lesson = Lesson.objects.filter(year_of_study=schoolkid.year_of_study,
                                   group_letter=schoolkid.group_letter,
                                   subject__title=subject_title).order_by("-date")[0]
    Commendation.objects.create(text=commendation,
                                created=lesson.date,
                                schoolkid=schoolkid,
                                subject=lesson.subject,
                                teacher=lesson.teacher)
