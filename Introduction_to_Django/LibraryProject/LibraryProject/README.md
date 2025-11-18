# Introduction to Django — LibraryProject

This repository contains a small Django project used for learning and demonstrating basic Django concepts.

Project path
- `Introduction_to_Django/LibraryProject`

Contents
- `manage.py` — Django project management script.
- `LibraryProject/` — Django project module containing `settings.py`, `urls.py`, `wsgi.py`, and `asgi.py`.
- `db.sqlite3` — Development SQLite database (included for convenience).
- `requirements.txt` — Python dependencies used by the project.

Prerequisites
- Python (a compatible 3.x runtime). A modern Python 3.10+ is recommended for Django 5.x.
- `pip` (comes with Python installations).
- PowerShell on Windows (this README includes PowerShell commands).

Quick setup (Windows PowerShell)

1. Open PowerShell and navigate to the repository root (where `manage.py` is located):

```
cd .\Introduction_to_Django
```

2. (Optional) Create a virtual environment if you don't have one already:

```
python -m venv myenv
```

3. Activate the virtual environment (PowerShell):

```
.\myenv\Scripts\Activate.ps1
```

4. Install dependencies:

```
pip install -r requirements.txt
```

5. Apply migrations and prepare the database:

```
python manage.py migrate
```

6. Create a superuser (admin):

```
python manage.py createsuperuser
```

7. Run the development server:

```
python manage.py runserver
```

The site will be available at `http://127.0.0.1:8000/` by default.

Notes about this project
- The project uses SQLite for development (`db.sqlite3` included). For production, use a more robust database (PostgreSQL, MySQL, etc.) and update `LibraryProject/settings.py` accordingly.
- The repository already contains a virtual environment named `myenv`. If you prefer, create a fresh virtual environment to avoid conflicts.

Project structure (top-level)

```
Introduction_to_Django/
├─ db.sqlite3
├─ manage.py
├─ LibraryProject/
│  ├─ __init__.py
│  ├─ asgi.py
│  ├─ settings.py
│  ├─ urls.py
│  └─ wsgi.py
```

Common tasks
- Run the shell with project context: `python manage.py shell`.
- Make and apply migrations for apps:

```
python manage.py makemigrations
python manage.py migrate
```
- Start a new app:

```
python manage.py startapp <app_name>
```

Testing
- If you add tests, run them with:

```
python manage.py test
```

Contributing
- This repository is used for learning and experimentation. Feel free to add small apps, exercises, or documentation improvements.
- If you add features, update `requirements.txt` with `pip freeze > requirements.txt` to keep dependencies consistent.

License
- No license specified. Treat this as an educational project.

Need help?
- If you want, I can also:
  - Add a `.gitignore` tuned for Python/Django projects.
  - Add sample apps or expand the README with screenshots or examples.
  - Run checks or tests in your environment and report back.

---

File created: `README.md`