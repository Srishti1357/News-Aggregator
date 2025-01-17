from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from .models import Article
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


def scrape_google_news():
    service = Service(r"F:\BTES Training\Module 3 (Back End)\NewsAggrgator\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    url = "https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en"
    driver.get(url)

    driver.implicitly_wait(5)

    for _ in range(10):
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
        time.sleep(3)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    articles = soup.find_all('a', class_="gPFEn")
    publishers = soup.find_all('img', class_="qEdqNd y3G2Ed")
    print(publishers)
    
    if not articles:
        print("No articles found.")
        return

    for article,publisher in zip(articles,publishers):
        try:
            title = article.text.strip()
            href = article.get('href')
            if href.startswith('./'):
                link = f"https://news.google.com{href[1:]}"
            else:
                link = href

            publisher_logo = publisher.get('src')
            # Save to database
            Article.objects.get_or_create(title=title, link=link, category="general",publisher_logo = publisher_logo)

            print(f"Saved Article: {title}")
        except Exception as e:
            print(f"Error processing article: {e}")



def scrape_google_news1():
    
    
    service = Service(r"F:\BTES Training\Module 3 (Back End)\NewsAggrgator\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    ops=webdriver.ChromeOptions()
    url = "https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en"
    driver.get(url)

    driver.implicitly_wait(5)
    print("Going to for u....")
    
    for_u_btn=driver.find_element(By.XPATH,"//*[@class='EctEBd']").click()
    ops.add_argument("--disable notification")
    print("gone....")
    
    # Scroll to load more articles if needed
    for _ in range(10):
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
        time.sleep(3)

    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    articles = soup.find_all('a', class_="gPFEn")
    publishers = soup.find_all('img', class_="qEdqNd y3G2Ed")
    print(publishers)
    
    if not articles:
        print("No articles found.")
        return

    for article,publisher in zip(articles,publishers):
        try:
            title = article.text.strip()
            href = article.get('href')
            if href.startswith('./'):
                link = f"https://news.google.com{href[1:]}"
            else:
                link = href

            publisher_logo = publisher.get('src')
            # Save to database
            Article.objects.get_or_create(title=title, link=link, category="general",publisher_logo = publisher_logo)

            print(f"Saved Article: {title}")
        except Exception as e:
            print(f"Error processing article: {e}")


def scrape_google_news2():
    
    
    service = Service(r"F:\BTES Training\Module 3 (Back End)\NewsAggrgator\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    ops=webdriver.ChromeOptions()
    url = "https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en"
    driver.get(url)

    driver.implicitly_wait(5)
    print("Going to for u....")
    
    India=driver.find_element(By.XPATH,"//*[@id='gb']/div[3]/div/c-wiz/div[1]/div[6]").click()
    ops.add_argument("--disable notification")
    print("gone....")
    
    # Scroll to load more articles if needed
    for _ in range(10):
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
        time.sleep(3)

    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    articles = soup.find_all('a', class_="gPFEn")
    publishers = soup.find_all('img', class_="qEdqNd y3G2Ed")
    print(publishers)
    
    if not articles:
        print("No articles found.")
        return

    for article,publisher in zip(articles,publishers):
        try:
            title = article.text.strip()
            href = article.get('href')
            if href.startswith('./'):
                link = f"https://news.google.com{href[1:]}"
            else:
                link = href

            publisher_logo = publisher.get('src')
            # Save to database
            Article.objects.get_or_create(title=title, link=link, category="general",publisher_logo = publisher_logo)

            print(f"Saved Article: {title}")
        except Exception as e:
            print(f"Error processing article: {e}")


def scrape_google_news3():    
    service = Service(r"F:\BTES Training\Module 3 (Back End)\NewsAggrgator\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    ops=webdriver.ChromeOptions()
    url = "https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en"
    driver.get(url)

    driver.implicitly_wait(5)
    print("Going to for u....")
    
    Business=driver.find_element(By.XPATH,"//*[@id='gb']/div[3]/div/c-wiz/div[1]/div[9]").click()
    ops.add_argument("--disable notification")
    print("gone....")
    
    # Scroll to load more articles if needed
    for _ in range(10):
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
        time.sleep(3)

    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    articles = soup.find_all('a', class_="gPFEn")
    publishers = soup.find_all('img', class_="qEdqNd y3G2Ed")
    print(publishers)
    
    if not articles:
        print("No articles found.")
        return

    for article,publisher in zip(articles,publishers):
        try:
            title = article.text.strip()
            href = article.get('href')
            if href.startswith('./'):
                link = f"https://news.google.com{href[1:]}"
            else:
                link = href

            publisher_logo = publisher.get('src')
            # Save to database
            Article.objects.get_or_create(title=title, link=link, category="business",publisher_logo = publisher_logo)

            print(f"Saved Article: {title}")
        except Exception as e:
            print(f"Error processing article: {e}")


def scrape_google_news4():    
    service = Service(r"F:\BTES Training\Module 3 (Back End)\NewsAggrgator\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    ops=webdriver.ChromeOptions()
    url = "https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en"
    driver.get(url)

    driver.implicitly_wait(5)
    print("Going to for u....")
    
    entertain=driver.find_element(By.XPATH,"//*[@id='gb']/div[3]/div/c-wiz/div[1]/div[11]").click()
    ops.add_argument("--disable notification")
    print("gone....")
    
    # Scroll to load more articles if needed
    for _ in range(10):
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
        time.sleep(3)

    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    articles = soup.find_all('a', class_="gPFEn")
    publishers = soup.find_all('img', class_="qEdqNd y3G2Ed")
    print(publishers)
    
    if not articles:
        print("No articles found.")
        return

    for article,publisher in zip(articles,publishers):
        try:
            title = article.text.strip()
            href = article.get('href')
            if href.startswith('./'):
                link = f"https://news.google.com{href[1:]}"
            else:
                link = href

            publisher_logo = publisher.get('src')
            # Save to database
            Article.objects.get_or_create(title=title, link=link, category="entertainment",publisher_logo = publisher_logo)

            print(f"Saved Article: {title}")
        except Exception as e:
            print(f"Error processing article: {e}")


def scrape_google_news5():    
    service = Service(r"F:\BTES Training\Module 3 (Back End)\NewsAggrgator\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    # ops=webdriver.ChromeOptions()
    url = "https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en"
    driver.get(url)

    driver.implicitly_wait(5)
    print("Going to for u....")
    
    health_section = driver.find_element(By.XPATH, "//span[text()='Health']")

    # ops.add_argument("--disable notification")
    print("gone....")
    
    # Scroll to load more articles if needed
    for _ in range(10):
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
        time.sleep(3)

    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    articles = soup.find_all('a', class_="gPFEn")
    publishers = soup.find_all('img', class_="qEdqNd y3G2Ed")
    print(publishers)
    
    if not articles:
        print("No articles found.")
        return

    for article,publisher in zip(articles,publishers):
        try:
            title = article.text.strip()
            href = article.get('href')
            if href.startswith('./'):
                link = f"https://news.google.com{href[1:]}"
            else:
                link = href

            publisher_logo = publisher.get('src')
            # Save to database
            Article.objects.get_or_create(title=title, link=link, category="health",publisher_logo = publisher_logo)

            print(f"Saved Article: {title}")
        except Exception as e:
            print(f"Error processing article: {e}")

def scrape_google_news6():    
    service = Service(r"F:\BTES Training\Module 3 (Back End)\NewsAggrgator\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    ops=webdriver.ChromeOptions()
    url = "https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en"
    driver.get(url)

    driver.implicitly_wait(5)
    print("Going to for u....")
    
    science = driver.find_element(By.XPATH, "//span[text()='Science']")

    ops.add_argument("--disable notification")
    print("gone....")
    
    # Scroll to load more articles if needed
    for _ in range(10):
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
        time.sleep(3)

    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    articles = soup.find_all('a', class_="gPFEn")
    publishers = soup.find_all('img', class_="qEdqNd y3G2Ed")
    print(publishers)
    
    if not articles:
        print("No articles found.")
        return

    for article,publisher in zip(articles,publishers):
        try:
            title = article.text.strip()
            href = article.get('href')
            if href.startswith('./'):
                link = f"https://news.google.com{href[1:]}"
            else:
                link = href

            publisher_logo = publisher.get('src')
            # Save to database
            Article.objects.get_or_create(title=title, link=link, category="science",publisher_logo = publisher_logo)

            print(f"Saved Article: {title}")
        except Exception as e:
            print(f"Error processing article: {e}")


def scrape_google_news7():    
    service = Service(r"F:\BTES Training\Module 3 (Back End)\NewsAggrgator\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    ops=webdriver.ChromeOptions()
    url = "https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en"
    driver.get(url)

    driver.implicitly_wait(5)
    print("Going to for u....")
    
    sports = driver.find_element(By.XPATH, "//span[text()='Sports']")

    ops.add_argument("--disable notification")
    print("gone....")
    
    # Scroll to load more articles if needed
    for _ in range(10):
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
        time.sleep(3)

    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    articles = soup.find_all('a', class_="gPFEn")
    publishers = soup.find_all('img', class_="qEdqNd y3G2Ed")
    print(publishers)
    
    if not articles:
        print("No articles found.")
        return

    for article,publisher in zip(articles,publishers):
        try:
            title = article.text.strip()
            href = article.get('href')
            if href.startswith('./'):
                link = f"https://news.google.com{href[1:]}"
            else:
                link = href

            publisher_logo = publisher.get('src')
            # Save to database
            Article.objects.get_or_create(title=title, link=link, category="sports",publisher_logo = publisher_logo)

            print(f"Saved Article: {title}")
        except Exception as e:
            print(f"Error processing article: {e}")


def scrape_google_news8():    
    service = Service(r"F:\BTES Training\Module 3 (Back End)\NewsAggrgator\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    ops=webdriver.ChromeOptions()
    url = "https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en"
    driver.get(url)

    driver.implicitly_wait(5)
    print("Going to for u....")
    
    # tech = driver.find_element(By.XPATH, "//span[text()='Technology']")
    technology=driver.find_element(By.XPATH,"//*[@id='gb']/div[3]/div/c-wiz/div[1]/div[10]").click()
    ops.add_argument("--disable notification")
    print("gone....")
    
    # Scroll to load more articles if needed
    for _ in range(10):
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
        time.sleep(3)

    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()

    articles = soup.find_all('a', class_="gPFEn")
    publishers = soup.find_all('img', class_="qEdqNd y3G2Ed")
    print(publishers)
    
    if not articles:
        print("No articles found.")
        return

    for article,publisher in zip(articles,publishers):
        try:
            title = article.text.strip()
            href = article.get('href')
            if href.startswith('./'):
                link = f"https://news.google.com{href[1:]}"
            else:
                link = href

            publisher_logo = publisher.get('src')
            # Save to database
            Article.objects.get_or_create(title=title, link=link, category="technology",publisher_logo = publisher_logo)

            print(f"Saved Article: {title}")
        except Exception as e:
            print(f"Error processing article: {e}")


if __name__ == "__main__":
    scrape_google_news()
    scrape_google_news1()
    scrape_google_news2()
    scrape_google_news3()
    scrape_google_news4()
    scrape_google_news5()
    scrape_google_news6()
    scrape_google_news7()
    scrape_google_news8()