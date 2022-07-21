import requests
from bs4 import BeautifulSoup


URL= f"https://stackoverflow.com/jobs/companies?q=Python"


# 1. get page, 2. make request, 3. extra jobs

def get_last_page():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")
  pages = soup.find("div", {"class":"s-pagination"}).find_all("a")
  # last_pages = pages[-2].get_text().strip() 또는
  last_page = pages[-2].get_text(strip = True)
  return int(last_page)


def extract_job(html):
  # (location, title) =  => unpacking 사용
  (location, title) = html.find("div", {"class": "d-flex gs12 gsx ff-row-wrap fs-body1"}).find_all("div", {"class": "flex--item fc-black-500 fs-body1"}, recursive=False)
  # find_all의 callback함수 중 recursive는
  # True를 하면 해당 element 내부 모든걸 찾고
  # False를 하면 바로 밑에 있는것 만 찾는다.

  # unpacking 이용하기
  # title = location_and_title[1].get_text()
  # location = location_and_title[0].get_text()
  company = html.find("a", {"class": "s-link"})
  link = company['href']
  
  return {
    "title": title.get_text(),
    "company": company.get_text(),
    "location": location.get_text(),
    "apply_link": f"https://stackoverflow.com/{link}"
  }
  


def extract_jobs(last_page):
  jobs = []
  for page in range(last_page):
    print(f"Scrapping 'stackoverflow' page {page + 1}")
    result = requests.get(f"{URL}&pg={page + 1}")
    # print(result.status_code)
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class" : "dismissable-company"})
    for result in results:
      # print(result.find("div", {"class": "dismiss-trigger"})['data-id'])
      job = extract_job(result)
      jobs.append(job)
  return jobs
                          
  

def get_jobs():
  last_page = get_last_page()
  jobs = extract_jobs(last_page)
  return jobs;
  
