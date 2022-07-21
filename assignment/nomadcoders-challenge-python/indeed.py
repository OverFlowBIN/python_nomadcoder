import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL= f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit={LIMIT}"


def get_last_page():
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")
  pagination = soup.find("div", {"class": "pagination"})
  
  #pages는 list
  links = pagination.find_all('a')
   
  pages = [];
  for link in links[:-1]:
    # pages.append(link.find("span", {"class": "pn"}).string)
      pages.append(int(link.string)) # string이 하나뿐이면 이렇게 바로 link안에 string을 가져올 수 있다.
  
  max_page = pages[-1]
  return max_page


def extract_job(html):
  title = html.find("td", {"class": "resultContent"}).find("span")["title"]
  company = html.find("span", {"class": "companyName"}).string
  location = html.find("div", {"class": "companyLocation"}).string
  job_id = html.find("a")["data-jk"]
  
  return {
    "title": title,
    "company": company,
    "location": location,
    "link": f"https://kr.indeed.com/viewjob?jk={job_id}"
  }
  

def extract_jobs(last_page):
  
  jobs = [];
  for page in range(last_page):
    print(f"Scrapping 'indeed' page {page + 1}")
    result = requests.get(f"{URL}&start={page * LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class": "cardOutline"})
    for result in results:
      job = extract_job(result)
      jobs.append(job)
  return jobs


def get_jobs():
  last_page = get_last_page()
  jobs = extract_jobs(last_page)
  return jobs