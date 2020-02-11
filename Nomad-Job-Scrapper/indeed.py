import requests;
from bs4 import BeautifulSoup;

LIMIT = 50;
URL = f"https://kr.indeed.com/jobs?q=python&limit={LIMIT}";

#페이지
def extract_pages():
  result = requests.get(URL);
  soup = BeautifulSoup(result.text, "html.parser"); 
  #result.text는 html을 가져옴 / indeed의 페이지 숫자를 가져옴

  pagination = soup.find("div", {"class":"pagination"}); 
  #indeed의 pagination을 찾음

  links = pagination.find_all('a'); 
  #pagination의 모든 링크를 찾음, a = anchor
  
  pages = [];

  for link in links[0:-1]: #마지막 item은 제외
    pages.append(int(link.string)); 
    #link.find("span").string : 각 링크 안의 span을 찾고 그 안의 string을 찾음
    #link.string : 각 링크 안의 string을 찾음 (링크 안의 string이 하나만 있기 때문에 이렇게 써도 동일한 결과 나옴)

  max_page = pages[-1]; #마지막 페이지의 숫자

  return max_page;

#일자리, 회사, 위치
def extract_job(html):
  title = html.find("div", {"class": "title"}).find("a")["title"]; #일자리
  company = html.find("span", {"class": "company"});

  if company:
    company_anchor = company.find("a");

    if company_anchor is not None: #span 안의 company에 링크가 있을 때
      company = str(company_anchor.string);
    else: #span 안의 company에 링크가 없을 때
      company = str(company.string);
    
    company = company.strip(); #공백 삭제

  else:
    company = None;

  location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]; #위치
  job_id = html["data-jk"];
  
  return {'title': title, 'company': company, 'location': location, 'link': f"https://kr.indeed.com/viewjob?jk={job_id}"};

#총괄
def extract_indeed_jobs(last_page):
  jobs = []; #배열

  for page in range(last_page):
    print(f"Scrapping page {page}");

    result = requests.get(f"{URL}&start={page * LIMIT}");

    soup = BeautifulSoup(result.text, "html.parser");
    results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"}); 
    #find_all : 모든 리스트를 가져옴 / find : 첫번째만 가져옴
  
    for result in results: #result(=html) : 일자리
      job = extract_job(result);
      jobs.append(job); #jobs에 job을 넣어줌

  return jobs;

def get_jobs():
  last_page = extract_pages();
  jobs = extract_indeed_jobs(last_page);
  
  return(jobs);