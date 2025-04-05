from fastapi import FastAPI
from models import JobRequest, JobResponse, JobItem
from scrapers.linkedin import fetch_linkedin_jobs
from scrapers.indeed import fetch_indeed_jobs

app = FastAPI()
API_KEY = "67f697f673fd8272886b79f1"

@app.post("/find_jobs", response_model=JobResponse)
def find_jobs(payload: JobRequest):
    linkedin_jobs = fetch_linkedin_jobs(API_KEY, payload.position, payload.location)
    indeed_jobs = fetch_indeed_jobs(payload.position, payload.location)

    # Combine all jobs (Rozee/Glassdoor can be added too)
    combined_jobs = linkedin_jobs + indeed_jobs

    # For now, we return first 5 jobs. You can add LLM-based filtering here.
    filtered = combined_jobs[:5]

    # Map into response schema
    response = [
        JobItem(
            job_title=job.get("title", job.get("job_title", "")),
            company=job.get("company", ""),
            experience=job.get("experience", "N/A"),
            jobNature=job.get("jobNature", "N/A"),
            location=job.get("location", payload.location),
            salary=job.get("salary", "Not listed"),
            apply_link=job.get("link", job.get("apply_link", "#"))
        ) for job in filtered
    ]
    
    return JobResponse(relevant_jobs=response)
