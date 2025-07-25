from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os

# ---------------------- Step 0: Load .env ---------------------- #
load_dotenv()
EMAIL = os.getenv("LINKEDIN_EMAIL")
PASSWORD = os.getenv("LINKEDIN_PASSWORD")

# ---------------------- Step 1: Setup & Login ---------------------- #
def linkedin_login(email, password):
    options = Options()
    options.headless = False  # Set to True if you want headless browsing
    driver = webdriver.Chrome(options=options)

    driver.get('https://www.linkedin.com/login')
    time.sleep(2)

    driver.find_element(By.ID, 'username').send_keys(email)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(3)
    return driver

# ---------------------- Step 2: Search Jobs ---------------------- #
def search_jobs(driver, keyword="Data Scientist", location="India"):
    driver.get('https://www.linkedin.com/jobs')
    time.sleep(3)

    search_keywords = driver.find_element(By.XPATH, '//input[contains(@placeholder, "Search jobs")]')
    search_location = driver.find_element(By.XPATH, '//input[contains(@placeholder, "Search location")]')

    search_keywords.send_keys(keyword)
    search_location.clear()
    search_location.send_keys(location)

    driver.find_element(By.XPATH, '//button[@aria-label="Search"]').click()
    time.sleep(5)

# ---------------------- Step 3: Scrape Jobs (Updated) ---------------------- #
def scrape_jobs(driver):
    job_data = []

    # Scroll multiple times to load more jobs
    for _ in range(5):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

    # Save page for debugging (optional)
    with open("page.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # New LinkedIn structure: scrape from job cards
    jobs = soup.select('ul.jobs-search__results-list li')

    for job in jobs:
        try:
            title = job.select_one('h3').text.strip() if job.select_one('h3') else 'N/A'
            company = job.select_one('h4').text.strip() if job.select_one('h4') else 'N/A'
            post_date = job.find('time')['datetime'] if job.find('time') else 'N/A'
            job_data.append([title, company, post_date])
        except Exception as e:
            print("⚠ Error while parsing job:", e)
            continue

    return job_data

# ---------------------- Step 4: Save to CSV ---------------------- #
def save_to_csv(job_data, filename="linkedin_jobs.csv"):
    df = pd.DataFrame(job_data, columns=['Title', 'Company', 'Posted'])
    df.to_csv(filename, index=False)
    print(f"✅ Jobs saved to {filename}")
    return df

# ---------------------- Step 5: Remove Duplicates ---------------------- #
def remove_duplicates(input_file="linkedin_jobs.csv", output_file="linkedin_jobs_clean.csv"):
    df = pd.read_csv(input_file)
    df.drop_duplicates(inplace=True)
    df.to_csv(output_file, index=False)
    print(f"🧹 Cleaned data saved to {output_file}")
    return df

# ---------------------- Step 6: Visualize ---------------------- #
def visualize_jobs(df):
    if df.empty:
        print("⚠ No data to visualize.")
        return

    company_counts = df['Company'].value_counts().head(10)
    plt.figure(figsize=(10,6))
    company_counts.plot(kind='bar', color='indigo')
    plt.title('Top 10 Companies Hiring on LinkedIn')
    plt.xlabel('Company')
    plt.ylabel('Number of Job Listings')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# ---------------------- Main Runner ---------------------- #
if __name__ == "__main__":
    if not EMAIL or not PASSWORD:
        print("❌ Email or password not found in .env file!")
        exit()

    print("🚀 Logging into LinkedIn...")
    driver = linkedin_login(EMAIL, PASSWORD)
    search_jobs(driver, keyword="Data Scientist", location="India")
    print("🔍 Scraping job listings...")
    job_data = scrape_jobs(driver)
    driver.quit()

    if job_data:
        save_to_csv(job_data)
        clean_df = remove_duplicates()
        visualize_jobs(clean_df)
    else:
        print("⚠ No jobs scraped. Try increasing scroll delay or check selectors.")
