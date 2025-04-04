import requests

def fetch_linkedin_jobs(api_key: str, job_title: str, location: str):
    url = f"https://www.linkedin.com/jobs/search/?keywords={job_title}&location={location}"
    endpoint = "https://api.scrapingdog.com/linkedin/job"
    params = {
        "67f697f673fd8272886b79f1": api_key,
        "link": url
    }

    response = requests.get(endpoint, params=params)
    if response.status_code == 200:
        return response.json().get("jobs", [])
    return []



# 67f697f673fd8272886b79f1