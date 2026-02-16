# Mini Resume Collector

A simple REST API for collecting and managing candidate resumes, built with FastAPI.

## Python Version

Python 3.13.9

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Haynes79/miniresume-haynes-e-j.git
   cd miniresume-haynes-e-j
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**
   
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
      ```bash
          source .venv/bin/activate
      ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Steps to Run the Application

1. **Start the server**
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the application**
   
   The application will be available at: `http://127.0.0.1:8000`
   
   Interactive API documentation (Swagger UI): `http://127.0.0.1:8000/docs`
   
   Alternative API documentation (ReDoc): `http://127.0.0.1:8000/redoc`

## API Endpoints

### 1. Health Check

**Endpoint:** `GET /health`

**Description:** Check if the API is running and healthy

**Response:**
```json
{
  "status": "healthy"
}
```
---

### 2. Create Resume

**Endpoint:** `POST /resumes`

**Description:** Create a new resume entry

**Request Body:**
```json
{
  "full_name": "John Doe",
  "email": "john.doe@example.com",
  "phone": "9876543210",
  "skills": ["Python", "FastAPI", "REST API"],
  "experience_years": 2.5
}
```

**Response (201 Created):**
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "full_name": "John Doe",
  "email": "john.doe@example.com",
  "phone": "9876543210",
  "skills": ["Python", "FastAPI", "REST API"],
  "experience_years": 2.5
}
```

---

### 3. Get All Resumes

**Endpoint:** `GET /resumes`

**Description:** Retrieve all stored resumes

**Response (200 OK):**
```json
[
  {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "full_name": "John Doe",
    "email": "john.doe@example.com",
    "phone": "9876543210",
    "skills": ["Python", "FastAPI", "REST API"],
    "experience_years": 2.5
  }
]
```
---

### 4. Get Resume by ID

**Endpoint:** `GET /resumes/{resume_id}`

**Description:** Retrieve a specific resume by its ID

**Response (200 OK):**
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "full_name": "John Doe",
  "email": "john.doe@example.com",
  "phone": "9876543210",
  "skills": ["Python", "FastAPI", "REST API"],
  "experience_years": 2.5
}
```

**Response (404 Not Found):**
```json
{
  "detail": "Resume with ID {resume_id} not found"
}
```

## Validation Rules

- **full_name**: 3-100 characters
- **email**: Valid email format
- **phone**: 10-15 characters
- **skills**: At least 1 skill required
- **experience_years**: Must be >= 0

## Project Structure

```
miniresume-haynes-e-j/
├── main.py              # Main application file
├── requirements.txt     # Python dependencies
└── README.md           
```

## Technologies Used

- **FastAPI**: Modern, fast web framework for building APIs
- **Pydantic**: Data validation using Python type annotations
- **Uvicorn**: ASGI server for running the application

## Notes

- Data is stored in-memory and will be lost when the server restarts
- No database is used as per assignment requirements
- The API follows REST standards with appropriate HTTP status codes
