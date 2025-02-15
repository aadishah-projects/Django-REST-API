# Django REST API

A simple Django REST API for managing student records. This API supports CRUD operations for handling data related to students, such as their name, age, and description.

## Features

- **Create**: Add new student records.
- **Read**: Retrieve student details.
- **Update**: Modify existing student records.
- **Delete**: Remove student records.

## Technologies Used

- **Backend**: Django REST framework
- **Database**: SQLite (default, can be switched to other DBs like PostgreSQL or MySQL)
- **API Testing**: Django REST Framework Browsable API

## Installation

Follow these steps to set up the project on your local machine:

1. Clone the repository:
   ```bash
   git clone https://github.com/aadishah-projects/Django-REST-API.git
   cd Django-REST-API
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the API at:
   - **Browsable API**: `http://127.0.0.1:8000/home/`

## Usage

### Endpoints

- **GET** `/home/`: Retrieve a list of all students.
- **POST** `/home/`: Create a new student record.
- **DELETE** `/home/{id}/`: Delete a specific student record.
- **PUT** `/home/{id}/`: Update an existing student record.

### Example Request

To create a new student, send a `POST` request to `/home/` with the following payload:

```json
{
  "name": "John Doe",
  "age": 20,
  "description": "A computer science student."
}
```

### Browsable API

You can use the built-in Django REST framework's browsable API for testing and interacting with the endpoints. Simply navigate to the `/home/` URL in your browser.

![image](https://github.com/user-attachments/assets/4ee0e5aa-6859-406b-8a6d-08623d876268)

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature description"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
