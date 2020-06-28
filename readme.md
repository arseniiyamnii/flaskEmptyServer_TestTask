pylint-7.5/10  
  
Note:  
I KNOW that in workingprogram, `.env` file must be in `.gitignore`  
  
=====  
  
INSTALL  
it works with direnv and venv. You need installed python3 venv to use this easy.  
`pip3 install venv`  
then `cd` to the dirrectory.  
`cd flaskEmptyServer_TestTask`  
create new venv  
`python3 -m venv .`  
allow direnv  
`direnv allow`  
install requirements  
`pip3 install -r requirements.txt`  
run server  
`flask run -h localhost -p $PORT` on main dirrectory(not '/src')  
IF you run it in `srs`, first run `export FLASK_APP=__init__.py`  
  
=====  
  
USAGE  
after running you can go to the http://localhost:8001  
every request logging to the `log` file  
all requests wtithout `GET` method logging as ERROR  
all requests to the url != /api logging as ERROR  
all requests with argumet invalid=1  
at the /api, you run three process  
evry process logging  
if you request got parameter notawaiting=1, process2 lgging as ERROR  
  
=====  
  
TESTS  
pylint-6/10  
  
go to the test folder  
`cd emptyServer/tests`  
run `pytest`  

