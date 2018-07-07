


What is this ?
------

This is a simple rest api that helps to store scores online

How it works
------
this api offer routes to add/update results , those results are stored on local SQLite3 Database

How do i launch it?
------

1. [Python 3](https://www.python.org/downloads/)
2. [Pip](https://pip.pypa.io/en/stable/installing/)
3. Then, ```pip install flask```
4. Then, clone this repo (attention! it will be cloned to the current directory, so make sure you do it in some kinda documents or special one) ```git clone https://github.com/SalahEddineBC/RankingApi myproject ```
5. Then, ```cd myproject ```
6. Finally, ```python server.py```   

Docuementation
------

Routes
------

``` GET / ``` :    to fetch the list of players   
``` POST /add ```:    parameters :    ```{name:PlayerName,      Score:PlayerScore   }``` to add PlayerName with PlayScore to the list or update it if playerName already exists

License
------
GPL v3

Contribution
------
Feel free to contribute.
