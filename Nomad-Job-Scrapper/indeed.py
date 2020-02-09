import requests;
from bs4 import BeautifulSoup;

LIMIT = 50;
INDEED_URL = f"https://kr.indeed.com/jobs?q=python&limit={LIMIT}";

def extract_indeed_pages():
  indeed_result = requests.get(INDEED_URL);

  indeed_soup = BeautifulSoup(indeed_result.text, "html.parser"); #indeed_result.text는 html을 가져옴 / indeed의 페이지 숫자를 가져옴

  pagination = indeed_soup.find("div", {"class":"pagination"}); #indeed의 pagination을 찾음

  links = pagination.find_all('a'); #pagination의 모든 링크를 찾음, a = anchor
  pages = [];

  for link in links[0:-1]: #마지막 item은 제외
    pages.append(int(link.string)); 
    #link.find("span").string : 각 링크 안의 span을 찾고 그 안의 string을 찾음
    #link.string : 각 링크 안의 string을 찾음 (링크 안의 string이 하나만 있기 때문에 이렇게 써도 동일한 결과 나옴)

  max_page = pages[-1]; #마지막 페이지의 숫자

  return max_page;

def extract_indeed_jobs(last_page):
  jobs = [];

  #for page in range(last_page):
  result = requests.get(f"{INDEED_URL}&start={0 * LIMIT}");

  indeed_soup = BeautifulSoup(result.text, "html.parser");
  results = indeed_soup.find_all("div", {"class": "jobsearch-SerpJobCard"});
  
  for result in results:
    title = result.find("div", {"class": "title"}).find("a")["title"];
    print(title);

  return jobs;