from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from random import randint
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

pagination_url = 'https://in.indeed.com/jobs?q={}&l={}&radius=100&sc=0kf%3Aattr%28X62BT%29%3B&filter=0&sort=date&start={}'

job = 'python+developer'
location = 'Noida%2C+Uttar+Pradesh'

csv_columns = ['title', 'company', 'location', 'link', 'salary']
csv_file = "jobs_data.csv"

driver = webdriver.Edge()

try:
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()

        driver.get(pagination_url.format(job, location, 0))
        time.sleep(randint(2, 6))
        job_count_elements = driver.find_elements(By.CLASS_NAME, 'jobsearch-JobCountAndSortPane-jobCount')
        max_iter_pages = 0

        if job_count_elements:
            job_count_text = job_count_elements[0].text
            job_count = int(job_count_text.split(' ')[0].replace(',', ''))
            max_iter_pages = (job_count) // 15

        for i in range(max_iter_pages):
            driver.get(pagination_url.format(job, location, i * 10))
            time.sleep(randint(2, 4))

            try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "mosaic-jobResults")))
                job_page = driver.find_element(By.ID, "mosaic-jobResults")
                jobs = job_page.find_elements(By.CLASS_NAME, "job_seen_beacon")

                for jj in jobs:
                    try:
                        job_title = jj.find_element(By.CLASS_NAME, "jobTitle")
                        job_info = {
                            'title': job_title.text,
                            'company': jj.find_element(By.CSS_SELECTOR,"[data-testid='company-name'].css-1x7z1ps.eu4oa1w0").text,
                            'location': jj.find_element(By.CSS_SELECTOR,"[data-testid='text-location'].css-t4u72d.eu4oa1w0").text,
                            'link': job_title.find_element(By.CSS_SELECTOR,"a").get_attribute("href")
                        }

                        try:
                            salary = jj.find_element(By.CLASS_NAME, "salary-snippet-container").text
                        except NoSuchElementException:
                            try:
                                salary = jj.find_element(By.CSS_SELECTOR,"[data-testid='attribute_snippet_testid'].css-1ihavw2.eu4oa1w0").text
                            except NoSuchElementException:
                                salary = None

                        job_info['salary'] = salary
                        writer.writerow(job_info)
                    except Exception as job_error:
                        print(f"Error processing job: {job_error}")

            except TimeoutException:
                print("Timed out waiting for page to load")
                break

except Exception as e:
    print("An error occurred:", e)

finally:
    driver.quit()
