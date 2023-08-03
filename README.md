## Функционал  
Этот бот парсит ```https://kaspi.kz/shop/```  
В выбранной категории он отбирает те товары, у которых количество отзывов за 2023 год больше или равно заданному в .ini файле значению.  
После чего все товары, прошедшие через фильтр выдаются ссылками в output.txt  
**БОТ ПАРСИТ ТОЛЬКО КАТЕГОРИИ ТОВАРОВ (бытовая техника, телефоны, итд).**  

Пример рабочей ссылки:  
```https://kaspi.kz/shop/c/smartphones%20and%20gadgets/?sort=rating```  

Кнопки сортировки товаров отражаются параметром в URL, то есть можно сначала отсортировать товары на сайте так, как вам хочется, а потом скормить эту ссылку боту.  

**ПЭЙ АТТЕНШОН:** зачастую при сортировке на сайте люди кликают туда-сюда по номерам страниц, чтобы проверить как отсортировались товары итд, при возврате на 1(первую) страницу **НЕ ВСЕГДА** правильно выставляется параметр в URL, поэтому, убедитесь в том, что в конце текущего URL(адресная строка) параметр page равен 1:  
ПРАВИЛЬНО (page=1):  
```https://kaspi.kz/shop/c/smartphones%20and%20gadgets/?sort=rating&page=1```  

НЕПРАВИЛЬНО (page=2):  
```https://kaspi.kz/shop/c/smartphones%20and%20gadgets/?sort=rating&page=2```  

Страшного при этом ничего не случится, просто бот изначально будет парсить со второй (или какая там будет) страницы, а это значит, что вы потеряете все самые "вкусные" товары с первой.  
  
## config.ini  
**feedback_threshold** - количество отзывов, необходимое для того, чтобы товар прошел через фильтр.  
> прим. если указать 10, то все товары, у которых 10 или больше отзывов за 2023 год попадут в итоговый файл в виде ссылок.  

**number_of_pages_to_parse** - количество страниц товаров, которые будет проходить бот.  

**driver_name** - имя файла драйвера с учетом расширения (прим. geckodriver.exe)  
  
## Скорость работы  
Бот работает довольно медленно, но отражает свой статус в консоли.  

  
## Запуск
1) Убедиться, что установлен/установить интерпретатор Python 3;
2) Склонировать этот репозиторий себе:  
```git clone https://github.com/Alryum/kaspi_bot.git```  
3) Создать виртуальное окружение, после чего установить туда все зависимости:  
```pip install -r requirements.txt```  
4) Необходимо скачать драйвер браузера Firefox (да, именно его, так как я его использую в коде) и засунуть его в папку collectors:  
```https://github.com/mozilla/geckodriver/releases```  
Версия драйвера должна совпадать с версией Firefox у вас на компутере.  
5) Запустить файл manage.py и всё должно работать, НО!  
  
Есть вероятность получить следующие ошибки:  
- Проблемы с драйвером(geckodriver). Скорее всего, он сообщит, что версия драйвера и браузера не совпадают, при этом там довольно понятная ошибка, так что тут просто смотрим в числа, которые он выкинул в консоли и идём качать именно эту версию geckodriver, после этого удаляем старый драйвер, закидываем новый, должно работать!  
- Проблемы с Python. Этих проблем может быть миллион, так что самые очевидные - это:  
  1) Вы установили старый интерпретатор, на данный момент таковыми можно считать все версии младше 3.10. В таком случае просто зайдите на ```https://www.python.org/``` и скачайте самый новый.  
  2) Проблема с виртуальным окружением, а именно: Вы можете пытаться запустить бота вне виртуального окружения, тогда, скорее всего, вам будут лететь ошибки о том, что он не может найти нужные библиотеки для работы. Просто активируйте виртуальное окружение перед тем, как запускать manage.py (прим. для активации нужно запустить этот файл ```.venv/Scripts/activate```).  

- Kaspi изменили разметку или стили своего сайта и бот просто стал неактуален, в этом случае, вероятнее всего, вы будете получать сообщение об ошибке в консоль и некорректный результат работы (например, пустой файл). Можно подождать пока я его исправлю (если я буду это делать) или полезть самому.  
