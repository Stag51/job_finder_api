from pydantic import BaseModel
from typing import List

class JobRequest(BaseModel):
    position: str
    experience: str
    salary: str
    jobNature: str
    location: str
    skills: str

class JobItem(BaseModel):
    job_title: str
    company: str
    experience: str
    jobNature: str
    location: str
    salary: str
    apply_link: str

class JobResponse(BaseModel):
    relevant_jobs: List[JobItem]
