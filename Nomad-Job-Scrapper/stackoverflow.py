import requests;
from bs4 import BeautifulSoup;

URL = f"https://stackoverflow.com/jobs?q=python&sort=i";

#페이지
def get_last_page():
  result = requests.get(URL);
  soup = BeautifulSoup(result.text, "html.parser");
  
  pages = soup.find("div", {"class": "s-pagination"}).find_all("a");
  last_page = pages[-2].get_text(strip=True); #next를 제외한 마지막 숫자
  
  return int(last_page);

#일자리, 회사, 위치, 지원링크
def extract_job(html):
  title = html.find("a", {"class": "s-link"})["title"];
  
  company, location = html.find("h3", {"class": "fs-body1"}).find_all("span", recursive=False); 
  #unpacking value : list 안에 2개의 item이 있을 때 사용
  #recursive = False : 첫번째 단계의 span만 가져옴 
  # <span> 첫번째 단계
  #   <span> 두번째 단계
  #   </span>
  # </span>

  company = company.get_text(strip=True);
  location = location.get_text(strip=True).strip("\n");

  job_id = html["data-jobid"]

  return {'title': title, 'company': company, 'location': location, 'apply_link': f"https://stackoverflow.com/jobs/{job_id}"};

def extract_jobs(last_page):
  jobs = [];

  for page in range(last_page):
    print(f"Scrapping Stackoverflow Page : {page}");
    result = requests.get(f"{URL}&pg={page + 1}");
    soup = BeautifulSoup(result.text, "html.parser");

    results = soup.find_all("div", {"class": "-job"});

    for result in results:
      job = extract_job(result);
      jobs.append(job);
    
  return jobs;

def get_jobs():
  last_page = get_last_page();

  jobs = extract_jobs(last_page);

  return jobs;