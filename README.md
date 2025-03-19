# PS05_Scrapy
 PS05 Scrapy

Устанавливаем нужную библиотеку через терминал:
    pip install scrapy

Вручную создаём шаблон проекта или использовать команду.
    scrapy startproject divanpars


Создаём файл внутри пакета spiders:
Пишем команду:
    cd 
Нажимаем правой кнопкой мыши на пакет и выбираем Copy Path/Reference — Absolute Path. Так мы скопируем абсолютный путь к пакету.
Вставляем путь в терминал, после команды cd.
Продолжаем команду:
    cd [путь] scrapy genspider divannewpars divan.ru


Визуально упрощаем работу с терминалом (необязательно):
    pip install ipython

Заходим в файл scrapy.cfg
Дописываем код:
!Это было, это не прописываем
    [settings]
    default = divanpars.settings

!Это новое, это прописываем
    shell == ipython

!То есть мы "заменяем" стандартный терминал только что установленным

Отправляем в терминале команду:
    scrapy shell


Команды в терминале:
    fetch(’ссылка’) — используется, чтобы загрузить веб-страницу. После использования покажется статус-код;
    response.css(’h2’) — поиск всех элементов с тегом h2;
    response.css(’h2.vFBoK’) — поиск элементов по названию класса. Указываем тег, ставим точку, указываем название класса;
    response.css(’div.LlPhw’) — поиск по тегу. Будет создан целый список;
    response.css(’div.LlPhw’).get() — выбор только первого элемента из списка;
    divan = response.css(’div.LlPhw’) — создаём переменную, в которую сохранится список из поиска по тегу;
    len(divan) — считаем, сколько диванов было найдено по тегу;
    divan1 = divan[0] — выбираем элемент из списка по его индексу (индексы начинаются с 0);
    divan1.css(’div’) — получаем все теги div от этого элемента.


Мы соберём информацию обо всех диванах с сайта. Мы возьмём названия, цены и ссылки.
Заходим на сайт и изучаем, какие у карточек одинаковые блоки.
Открываем файл divannewpars.py.
Удаляем pass.


Переходим в новый терминал Local(2).
Нажимаем правой кнопкой мыши на пакет spiders и выбираем Copy Path/Reference — Absolute Path.
Пишем команду:
    cd [путь] scrapy crawl divannewpars
___
Дополнительные материалы

1. Веб-скрапинг

https://tproger.ru/translations/skraping-sajta-s-pomoshhju-python-gajd-dlja-novichkov

https://priceva.ru/blog/article/v-chem-raznitsa-mezhdu-parsingom-i-skrejpingom

2. Scrapy

https://habr.com/ru/companies/otus/articles/812035/

https://habr.com/ru/companies/sberbank/articles/748406/

https://digitology.tech/docs/scrapy/index.html

3. Итераторы и генераторы

https://sky.pro/media/ispolzovanie-klyuchevogo-slova-yield-v-python/

https://proglib.io/p/chto-takoe-yield-v-python-samyy-populyarnyy-vopros-na-stakoverflou-po-pitonu-2022-03-21

https://habr.com/ru/articles/337314/

https://sky.pro/media/raznicza-mezhdu-generatorami-i-iteratorami-v-python/