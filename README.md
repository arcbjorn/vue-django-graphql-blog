# Simple Blog Set-Up (Vue, Django & Graphene GraphQL)

### 1. Clone repository

```sh
git clone https://github.com/arcbjorn/vue-django-graphql-blog
```

### 2. Set up Virtual Environment

```sh
cd vue-django-graphql-blog
pipenv shell
```

### 3. Make Default Migrations & Start the server

```sh
python manage.py migrate
python manage.py runserver
```

<details>
 <summary>Don’t forget that you need to create a superuser account, if you'd like to access the django admin</summary>

```
(blogql) $ python manage.py createsuperuser
Username: myusername
Email address: username@gmail.com
Password: 
Password (again): 
Superuser created successfully.
```

</details>

### 4. Install NPM Dependencies & Run the Vue App

```sh
cd vue-django-graphql-blog/blogfront
npm install
npm run dev
```

App on the port:
[http://localhost:8080](http://localhost:8080).

Special thanks to Graphene devs:
[https://graphene-python.org/](https://graphene-python.org/)