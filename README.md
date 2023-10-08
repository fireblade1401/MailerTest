# MailerTest
MailerTest Запуск Docker контейнера с приложением

1.Клонировать репозиторий: __git clone git@github.com:fireblade1401/MailerTest.git__

2.Перейти в директорию проекта: __cd MailerTest__

3.Построить Docker образ: __docker build -t mailer-service .__

4.Запустить контейнер: **docker run -p 8000:8000 mailer-service**

После запуска приложение будет доступно по адресу __http://localhost:8000__
