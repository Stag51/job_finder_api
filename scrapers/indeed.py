import requests
from bs4 import BeautifulSoup

def fetch_indeed_jobs(job_title: str, location: str):
    jobs = []
    url = f"https://www.indeed.com/jobs?q={job_title}&l={location.replace(' ', '+')}"
    headers = {"User-Agent": "Mozilla/5.0"}

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    for job_card in soup.select(".result"):
        title = job_card.select_one("h2 span")
        company = job_card.select_one(".companyName")
        location_tag = job_card.select_one(".companyLocation")
        link_tag = job_card.select_one("a")
        
        jobs.append({
            "job_title": title.text if title else "",
            "company": company.text if company else "",
            "location": location_tag.text if location_tag else location,
            "experience": "N/A",
            "jobNature": "N/A",
            "salary": "Not listed",
            "apply_link": f"https://indeed.com{link_tag['href']}" if link_tag else ""
        })
    return jobs
