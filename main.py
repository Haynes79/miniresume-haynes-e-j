from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr, Field
from typing import List
from uuid import uuid4

app = FastAPI(
    title="Mini Resume Collector API",
    description="A simple resume collection API with in-memory storage",
    version="1.0.0"
)

# In-memory storage
resumes_db = []

# Pydantic Models

class ResumeCreate(BaseModel):
    full_name: str = Field(..., min_length=3, max_length=100, description="Candidate's full name")
    email: EmailStr = Field(..., description="Candidate's email address")
    phone: str = Field(..., min_length=10, max_length=10, description="Candidate's phone number")
    skills: List[str] = Field(..., min_items=1, description="List of candidate's skills")
    experience_years: float = Field(..., ge=0, description="Years of experience")

    class Config:
        json_schema_extra = {
            "example": {
                "full_name": "John Doe",
                "email": "john.doe@example.com",
                "phone": "9876543210",
                "skills": ["Python", "FastAPI", "REST API"],
                "experience_years": 3
            }
        }

class ResumeResponse(ResumeCreate):
    id: str

# Health Check Endpoint

@app.get(
    "/health",
    status_code=status.HTTP_200_OK,
    tags=["Health"],
    summary="Health check endpoint"
)
def health_check():
    return {"status": "healthy"}


# Create Resume

@app.post(
    "/resumes",
    response_model=ResumeResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Resumes"],
    summary="Create a new resume"
)
def create_resume(resume: ResumeCreate):
    resume_id = str(uuid4())
    
    new_resume = ResumeResponse(
        id=resume_id,
        **resume.model_dump()
    )
    
    resumes_db.append(new_resume)
    
    return new_resume

# Get All Resumes

@app.get(
    "/resumes",
    response_model=List[ResumeResponse],
    tags=["Resumes"],
    summary="Get all resumes"
)
def get_resumes():
    
    return resumes_db


# Get Resume by ID

@app.get(
    "/resumes/{resume_id}",
    response_model=ResumeResponse,
    tags=["Resumes"],
    summary="Get a specific resume by ID"
)
def get_resume(resume_id: str):
    for resume in resumes_db:
        if resume.id == resume_id:
            return resume
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Resume with ID {resume_id} not found"
    )
