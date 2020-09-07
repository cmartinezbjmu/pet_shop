# PetShop - Ubits



PetShop es una aplicación que le permite a los usuarios registrados agregar, editar y eliminar citas para sus mascotas. Esta plataforma está siendo desarrollada con el framework Django.

## Requisitos de instalación

```bash
* Python versión = 3.8
* PostgreSQL version >= 11
* Instalar el administrador de entornos virtuales 'pipenv'(https://pypi.org/project/pipenv/) 
```

## Instalación

- Clone el repositorio con el comando "git clone https://github.com/cmartinezbjmu/pet_shop.git"
- Acceda al directorio del proyecto y ejecute "pipenv install" para instalar todas las dependecias del proyecto.
- Cree un archivo .env en la raíz del proyecto con los siguientes datos

```bash
  - SECRET_KEY=l(ws_1u18omfey+vgyxakv!rgyhx6x(9_(w*pq5s%$zp!o68pn
  - DBNAME=petshopdb
  - DBUSER=postgres
  - DBPASS=admin
  - DBHOST=127.0.0.1
  - DBPORT=5432
```

Nota: Los valores expuestos aquí son de ejemplo y deben cambiarse para evitar fallas de seguridad en la aplicación.

## Ejecute la aplicación

Inicie el entorno virtual

```bash
pipenv shell
```

Ejecute las migraciones en la base de datos

```bash
python manage.py migrate
```

Finalmente, inicie la aplicación

```bash
python manage.py runserver
```
