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

def extract_jobs(last_page):
  jobs = [];

  for page in range(last_page):
    result = requests.get(f"{URL}&pg={page + 1}");
    soup = BeautifulSoup(result.text, "html.parser");

    results = soup.find_all("div", {"class": "-job"});

    for result in results:
      print(result["data-jobid"]);

def get_jobs():
  last_page = get_last_page();

  jobs = extract_jobs(last_page);

  return jobs;