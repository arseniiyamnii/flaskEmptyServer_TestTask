Note:  
I KNOW that in working example `.env` file must be in `.gitignore`
it works with direnv and venv. You need installed python3 venv to use this easy.  
`sudo apt install direnv`  
`pip3 install venv`  
then `cd` to the dirrectory.  
`python3 -m venv .`  
`direnv allow`  
`pip3 install -r requirements.txt`  

`flask run -h localhost -p $PORT` on main dirrectory(not src)
if you run in `srs`, run `export FLASK_APP=main.py`
OR simple:  
`pip3 install flask`  
and then run `main.py`  

but i recommend use first way
