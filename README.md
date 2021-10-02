# Z49-TMS

# Django-steam web application
## This is a django-based steam application

### Django-steam включает в себя:
* Регистрация, вход и выход из системы.
* Профиль пользователя:
  * Возможность изменния и сохранения всех личных данных.
  * Возможность просмотра чужого профиля и его библиотеки игр
* Товары (игры):
  * Модель товара
  * Виш-лист игр
  * Покупка игр

* Корзина и заказы:
  * Добавление товара в корзину без перегагрузки страницы
  * Оформление заказа
  * Оплата заказа (Подключение API какой-нибудь платежки)
  * Удаление заказа
  * Статусы заказа

* Работа с админкой джанго, графики помесячных продаж


## Как запустить проект у себя?

1. git clone https://github.com/EternalTDt/steam-clone-2.0
2. pip install -r requirements.txt
3. cd steam
4. sudo docker-compose build
5. sudo docker compose up
