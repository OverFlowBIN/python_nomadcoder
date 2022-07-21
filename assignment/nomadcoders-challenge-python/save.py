import csv

def save_to_file(jobs):
  # open => 없으면 새로 생성해줌 있으면 open
  file = open("jobs.csv", mode="w")
  writer = csv.writer(file)
  writer.writerow(["title","company","location","link"])
  for job in jobs:
    writer.writerow(list(job.values())) # job.valuse() type => dictionry
  return