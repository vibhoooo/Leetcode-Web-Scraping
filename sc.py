from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

def scrape_problem(url):
    driver = webdriver.Chrome()
    driver.get(url)

    try:
        problem_name_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'truncate')]"))
        )
        problem_name = problem_name_element.text

        description_element = driver.find_element(By.CLASS_NAME, "elfjS")
        description = description_element.text

        with open("leetcode_problems.csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow(["Problem name", "Problem description"])
            writer.writerow([problem_name, description])
        
        print("Data written to leetcode_problems.csv successfully!")

    except Exception as e:
        print("An error occurred:", e)

    finally:
        driver.quit()

url = input("Enter the URL of the LeetCode problem: ")
scrape_problem(url)
