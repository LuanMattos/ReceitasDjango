# :page_facing_up: Receitas - Django
Site de receitas com Django
<br>
<br>
### Executar a aplicação

```bash
# Clone este repositório 
$ git clone git@github.com:LuanMattos/ReceitasDjango.git

# Acesse a pasta do projeto no terminal/cmd
$ cd RECEITASDJANGO

# Instale o virtual env
$ python -m venv

# Ative o venv
Windows $ venv\Scripts\activate 

#execute o banco de dados postgres:
$ docker-compose up -d

#Execute as migrações
$ python manage.py migrate

#Execute o servidor
$ python manage.py runserver

# O servidor inciará na porta:8000 - acesse http://localhost:800 
# Usuário e Senha do admin = admin (http://localhost:800/admin)

No admin é onde você cadastra suas receitas/pessoas e etc..
```

# :art: Layout

![alt text](https://github.com/LuanMattos/ReceitasDjango/blob/main/media/doc/1.png "Screenshot 1")

<br>
<br>

![alt text](https://github.com/LuanMattos/ReceitasDjango/blob/main/media/doc/2.png "Screenshot 2")


