import csv;

def save_to_file(jobs):
  file = open("jobs.csv", mode = "w", encoding="utf-8"); 
  #open : 파일을 열고, 파일이 없으면 생성
  #mode : 읽기, 쓰기전용 등을 설정

  writer = csv.writer(file);
  writer.writerow(["title", "company", "location", "link"]); #첫 줄 추가

  for job in jobs:
    writer.writerow(list(job.values()));

  #return