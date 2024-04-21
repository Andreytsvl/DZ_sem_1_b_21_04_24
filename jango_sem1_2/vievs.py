import logging

from django.http import HttpResponse

# Получаем экземпляр логгера
logger = logging.getLogger(__name__)


def index(request):
    logger.info('''f"Посетитель зашёл на главную страницу: {request.user}")
    return HttpResponse(<h1>Добро пожаловать на страницу Иванова Ивана Иваныча</h1>
                        <p>Описание главной страницы...</p>''')


def about(request):
    logger.info(f"Посетитель посетил страницу 'О себе': {request.user}")
    return HttpResponse('''<h1>О сайте</h1>
                        <p>Информация о сайте Иванова Ивана Иваныча...</p>''')