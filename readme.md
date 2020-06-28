pylint-7.5/10  
[Русский](#Русский)  
[English](#English)  
  
 #English
  
 ##Note:  
I KNOW that in working program, `.env` file must be in `.gitignore`  
  
=====  
  
 ##PRE INSTALL:  
it works with direnv and venv. You need installed python3 venv to use this easy.  
`pip3 install venv`  
  
=====  
  
 ##INSTALL:
then git clone with:
`git clone https://github.com/arseniiyamnii/flaskEmptyServer_TestTask.git`
then `cd` to the dirrectory.  
`cd flaskEmptyServer_TestTask`  
create new venv  
`python3 -m venv .`  
allow direnv  
`direnv allow`  
install requirements  
`pip3 install -r requirements.txt`  
run server  
`flask run -h localhost -p $PORT` on main dirrectory(not '/emptyServer')  
IF you run it in `emptyServer`, first run `export FLASK_APP=server.py`  
  
=====  
  
 ##USAGE:  
after running you can go to the http://localhost:8001  
every request logging to the `log` file  
all requests wtithout `GET` method logging as ERROR  
all requests to the url != /api logging as ERROR  
all requests with argumet invalid=1  
at the /api, you run three process  
evry process logging  
if you request got parameter notawaiting=1, process2 lgging as ERROR  
  
=====  
  
 ##TESTS:  
pylint-6/10  
  
go to the test folder  
`cd emptyServer/tests`  
run `pytest`  
  
[Русский](#Русский)  
[English](#English)  
  
 #Русский
  
 ##Заметка:  
Я знаю,что в рабочей программе, `.env` файл, должен быть в `.gitignore`  
  
=====  
  
 ##Подготовка к установке:  
Хорошо работает с direnv и venv. Вам нужен установленный python3 venv для простоты использования.  
`pip3 install venv`  
  
=====  
  
 ##Установка:
Клонируем:
`git clone https://github.com/arseniiyamnii/flaskEmptyServer_TestTask.git`
потом `cd` в дирректорию.  
`cd flaskEmptyServer_TestTask`  
создадим новый venv  
`python3 -m venv .`  
Разрешим direnv работу в дирректории  
`direnv allow`  
Устанвим зависимости  
`pip3 install -r requirements.txt`  
Запускаем сервер  
`flask run -h localhost -p $PORT` в главной дирректории(не в  '/emptyServer')  
Если вы запускаете в дирректории `emptyServer`, для начала выполните `export FLASK_APP=server.py`  
  
=====  
  
 ##Использование:  
После запуска пройдите по ссылке http://localhost:8001  
Каждый запрос логируется в `log` файл  
Все запрсы не через `GET` метод логируются как Ошибка  
Все запросы не на URL /api логируются как Ошибка  
Все запросы с параметром invalid=1 логируются как Ошибка  
При переходе по  /api, вы запускаете 3 процесса  
Каждый процесс логируется  
Если в запросе есть параметр  notawaiting=1, второй процесс Логируется как ошибка  
  
=====  
  
 ##ТЕСТЫ:  
pylint-6/10  
  
Для тестироывния пройдите в дирректорию с тестами  
`cd emptyServer/tests`  
Запустите `pytest`  
Есть 3 теста на каждый вид URL


