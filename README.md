# SchoolApp

SchoolApp is a Django-based web application for managing school-related data, including teachers, students, classes, courses, chapters, and lectures. It provides RESTful APIs for CRUD operations on these entities.

## Features

- Manage Teachers, Students, Classes, Courses, Chapters, and Lectures
- JWT Authentication
- Admin interface with Django Jazzmin
- File uploads for images and lecture files

## Requirements

- Python 3.12
- Django 5.1.4
- Django REST framework
- Django REST framework SimpleJWT
- Pillow

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/SarwechAbro/SchoolProject.git
    cd schoolapp
    ```

2. Create and activate a virtual environment:
    ```sh
    python3 -m venv myenv
    source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply the migrations:
    ```sh
    python manage.py migrate
    ```

5. Create a superuser:
    ```sh
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```sh
    python manage.py runserver
    ```

## API Endpoints

### Authentication

- `POST /token/get/` - Obtain JWT token
- `POST /token/refresh/` - Refresh JWT token
- `POST /token/verify/` - Verify JWT token

### Teachers

- `GET /teacherapi/` - List all teachers
- `POST /teacherapi/` - Create a new teacher
- `GET /teacherapi/<int:pk>/` - Retrieve a teacher by ID
- `PUT /teacherapi/<int:pk>/` - Update a teacher by ID
- `DELETE /teacherapi/<int:pk>/` - Delete a teacher by ID

### Students

- `GET /studentapi/` - List all students
- `POST /studentapi/` - Create a new student
- `GET /studentapi/<int:pk>/` - Retrieve a student by ID
- `PUT /studentapi/<int:pk>/` - Update a student by ID
- `DELETE /studentapi/<int:pk>/` - Delete a student by ID

### Classes

- `GET /classapi/` - List all classes
- `POST /classapi/` - Create a new class
- `GET /classapi/<int:pk>/` - Retrieve a class by ID
- `PUT /classapi/<int:pk>/` - Update a class by ID
- `DELETE /classapi/<int:pk>/` - Delete a class by ID

### Courses

- `GET /courseapi/` - List all courses
- `POST /courseapi/` - Create a new course
- `GET /courseapi/<int:pk>/` - Retrieve a course by ID
- `PUT /courseapi/<int:pk>/` - Update a course by ID
- `DELETE /courseapi/<int:pk>/` - Delete a course by ID

### Chapters

- `GET /chapterapi/` - List all chapters
- `POST /chapterapi/` - Create a new chapter
- `GET /chapterapi/<int:pk>/` - Retrieve a chapter by ID
- `PUT /chapterapi/<int:pk>/` - Update a chapter by ID
- `DELETE /chapterapi/<int:pk>/` - Delete a chapter by ID

### Lectures

- `GET /lectureapi/` - List all lectures
- `POST /lectureapi/` - Create a new lecture
- `GET /lectureapi/<int:pk>/` - Retrieve a lecture by ID
- `PUT /lectureapi/<int:pk>/` - Update a lecture by ID
- `DELETE /lectureapi/<int:pk>/` - Delete a lecture by ID

## Admin Interface

Access the Django admin interface at `/admin/` to manage the data through a user-friendly interface.

## License

This project is licensed under the MIT License.
