# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from bs4 import BeautifulSoup
# from .models import Article
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options


# def scrape_google_news():
#     service = Service(r"F:\BTES Training\Module 3 (Back End)\NewsAggrgator\chromedriver-win64\chromedriver.exe")
#     driver = webdriver.Chrome(service=service)
#     url = "https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en"
#     driver.get(url)

#     driver.implicitly_wait(5)

#     # Scroll to load more articles if needed
#     for _ in range(10):
#         driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
#         time.sleep(3)

#     # Parse the page source with BeautifulSoup
#     soup = BeautifulSoup(driver.page_source, "html.parser")
#     driver.quit()

#     articles = soup.find_all('a', class_="gPFEn")
#     publishers = soup.find_all('img', class_="qEdqNd y3G2Ed") # msvBD zC7z7b
#     print(publishers)
    
#     if not articles:
#         print("No articles found.")
#         return

#     for article,publisher in zip(articles,publishers):
#         try:
#             title = article.text.strip()
#             href = article.get('href')
#             if href.startswith('./'):
#                 link = f"https://news.google.com{href[1:]}"
#             else:
#                 link = href

#             publisher_logo = publisher.get('src')
#             # Save to database
#             Article.objects.get_or_create(title=title, link=link, category="general",publisher_logo = publisher_logo)

#             print(f"Saved Article: {title}")
#         except Exception as e:
#             print(f"Error processing article: {e}")



# def scrape_google_news1():
    
    
#     service = Service(r"F:\BTES Training\Module 3 (Back End)\NewsAggrgator\chromedriver-win64\chromedriver.exe")
#     driver = webdriver.Chrome(service=service)
#     ops=webdriver.ChromeOptions()
#     url = "https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en"
#     driver.get(url)

#     driver.implicitly_wait(5)
#     print("Going to for u....")
    
#     for_u_btn=driver.find_element(By.XPATH,"//*[@class='EctEBd']").click()
#     ops.add_argument("--disable notification")
#     print("gone....")
    
#     # Scroll to load more articles if needed
#     for _ in range(10):
#         driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
#         time.sleep(3)

#     # Parse the page source with BeautifulSoup
#     soup = BeautifulSoup(driver.page_source, "html.parser")
#     driver.quit()

#     articles = soup.find_all('a', class_="gPFEn")
#     publishers = soup.find_all('img', class_="qEdqNd y3G2Ed")
#     print(publishers)
    
#     if not articles:
#         print("No articles found.")
#         return

#     for article,publisher in zip(articles,publishers):
#         try:
#             title = article.text.strip()
#             href = article.get('href')
#             if href.startswith('./'):
#                 link = f"https://news.google.com{href[1:]}"
#             else:
#                 link = href

#             publisher_logo = publisher.get('src')
#             # Save to database
#             Article.objects.get_or_create(title=title, link=link, category="general",publisher_logo = publisher_logo)

#             print(f"Saved Article: {title}")
#         except Exception as e:
#             print(f"Error processing article: {e}")


# def scrape_google_news2():
    
    
#     service = Service(r"F:\BTES Training\Module 3 (Back End)\NewsAggrgator\chromedriver-win64\chromedriver.exe")
#     driver = webdriver.Chrome(service=service)
#     ops=webdriver.ChromeOptions()
#     url = "https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en"
#     driver.get(url)

#     driver.implicitly_wait(5)
#     print("Going to for u....")
    
#     India=driver.find_element(By.XPATH,"//*[@id='gb']/div[3]/div/c-wiz/div[1]/div[6]").click()
#     ops.add_argument("--disable notification")
#     print("gone....")
    
#     # Scroll to load more articles if needed
#     for _ in range(10):
#         driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
#         time.sleep(3)

#     # Parse the page source with BeautifulSoup
#     soup = BeautifulSoup(driver.page_source, "html.parser")
#     driver.quit()

#     articles = soup.find_all('a', class_="gPFEn")
#     publishers = soup.find_all('img', class_="qEdqNd y3G2Ed")
#     print(publishers)
    
#     if not articles:
#         print("No articles found.")
#         return

#     for article,publisher in zip(articles,publishers):
#         try:
#             title = article.text.strip()
#             href = article.get('href')
#             if href.startswith('./'):
#                 link = f"https://news.google.com{href[1:]}"
#             else:
#                 link = href

#             publisher_logo = publisher.get('src')
#             # Save to database
#             Article.objects.get_or_create(title=title, link=link, category="general",publisher_logo = publisher_logo)

#             print(f"Saved Article: {title}")
#         except Exception as e:
#             print(f"Error processing article: {e}")


# def scrape_google_news3():    
#     service = Service(r"F:\BTES Training\Module 3 (Back End)\NewsAggrgator\chromedriver-win64\chromedriver.exe")
#     driver = webdriver.Chrome(service=service)
#     ops=webdriver.ChromeOptions()
#     url = "https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en"
#     driver.get(url)

#     driver.implicitly_wait(5)
#     print("Going to for u....")
    
#     Business=driver.find_element(By.XPATH,"//*[@id='gb']/div[3]/div/c-wiz/div[1]/div[9]").click()
#     ops.add_argument("--disable notification")
#     print("gone....")
    
#     # Scroll to load more articles if needed
#     for _ in range(10):
#         driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
#         time.sleep(3)

#     # Parse the page source with BeautifulSoup
#     soup = BeautifulSoup(driver.page_source, "html.parser")
#     driver.quit()

#     articles = soup.find_all('a', class_="gPFEn")
#     publishers = soup.find_all('img', class_="qEdqNd y3G2Ed")
#     print(publishers)
    
#     if not articles:
#         print("No articles found.")
#         return

#     for article,publisher in zip(articles,publishers):
#         try:
#             title = article.text.strip()
#             href = article.get('href')
#             if href.startswith('./'):
#                 link = f"https://news.google.com{href[1:]}"
#             else:
#                 link = href

#             publisher_logo = publisher.get('src')
#             # Save to database
#             Article.objects.get_or_create(title=title, link=link, category="business",publisher_logo = publisher_logo)

#             print(f"Saved Article: {title}")
#         except Exception as e:
#             print(f"Error processing article: {e}")


# def scrape_google_news4():    
#     service = Service(r"F:\BTES Training\Module 3 (Back End)\NewsAggrgator\chromedriver-win64\chromedriver.exe")
#     driver = webdriver.Chrome(service=service)
#     ops=webdriver.ChromeOptions()
#     url = "https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en"
#     driver.get(url)

#     driver.implicitly_wait(5)
#     print("Going to for u....")
    
#     entertain=driver.find_element(By.XPATH,"//*[@id='gb']/div[3]/div/c-wiz/div[1]/div[11]").click()
#     ops.add_argument("--disable notification")
#     print("gone....")
    
#     # Scroll to load more articles if needed
#     for _ in range(10):
#         driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
#         time.sleep(3)

#     # Parse the page source with BeautifulSoup
#     soup = BeautifulSoup(driver.page_source, "html.parser")
#     driver.quit()

#     articles = soup.find_all('a', class_="gPFEn")
#     publishers = soup.find_all('img', class_="qEdqNd y3G2Ed")
#     print(publishers)
    
#     if not articles:
#         print("No articles found.")
#         return

#     for article,publisher in zip(articles,publishers):
#         try:
#             title = article.text.strip()
#             href = article.get('href')
#             if href.startswith('./'):
#                 link = f"https://news.google.com{href[1:]}"
#             else:
#                 link = href

#             publisher_logo = publisher.get('src')
#             # Save to database
#             Article.objects.get_or_create(title=title, link=link, category="entertainment",publisher_logo = publisher_logo)

#             print(f"Saved Article: {title}")
#         except Exception as e:
#             print(f"Error processing article: {e}")


# def scrape_google_news5():    
#     service = Service(r"F:\BTES Training\Module 3 (Back End)\NewsAggrgator\chromedriver-win64\chromedriver.exe")
#     driver = webdriver.Chrome(service=service)
#     # ops=webdriver.ChromeOptions()
#     url = "https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en"
#     driver.get(url)

#     driver.implicitly_wait(5)
#     print("Going to for u....")
    
#     health_section = driver.find_element(By.XPATH, "//span[text()='Health']")

#     # ops.add_argument("--disable notification")
#     print("gone....")
    
#     # Scroll to load more articles if needed
#     for _ in range(10):
#         driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
#         time.sleep(3)

#     # Parse the page source with BeautifulSoup
#     soup = BeautifulSoup(driver.page_source, "html.parser")
#     driver.quit()

#     articles = soup.find_all('a', class_="gPFEn")
#     publishers = soup.find_all('img', class_="qEdqNd y3G2Ed")
#     print(publishers)
    
#     if not articles:
#         print("No articles found.")
#         return

#     for article,publisher in zip(articles,publishers):
#         try:
#             title = article.text.strip()
#             href = article.get('href')
#             if href.startswith('./'):
#                 link = f"https://news.google.com{href[1:]}"
#             else:
#                 link = href

#             publisher_logo = publisher.get('src')
#             # Save to database
#             Article.objects.get_or_create(title=title, link=link, category="health",publisher_logo = publisher_logo)

#             print(f"Saved Article: {title}")
#         except Exception as e:
#             print(f"Error processing article: {e}")

# def scrape_google_news6():    
#     service = Service(r"F:\BTES Training\Module 3 (Back End)\NewsAggrgator\chromedriver-win64\chromedriver.exe")
#     driver = webdriver.Chrome(service=service)
#     ops=webdriver.ChromeOptions()
#     url = "https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en"
#     driver.get(url)

#     driver.implicitly_wait(5)
#     print("Going to for u....")
    
#     science = driver.find_element(By.XPATH, "//span[text()='Science']")

#     ops.add_argument("--disable notification")
#     print("gone....")
    
#     # Scroll to load more articles if needed
#     for _ in range(10):
#         driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
#         time.sleep(3)

#     # Parse the page source with BeautifulSoup
#     soup = BeautifulSoup(driver.page_source, "html.parser")
#     driver.quit()

#     articles = soup.find_all('a', class_="gPFEn")
#     publishers = soup.find_all('img', class_="qEdqNd y3G2Ed")
#     print(publishers)
    
#     if not articles:
#         print("No articles found.")
#         return

#     for article,publisher in zip(articles,publishers):
#         try:
#             title = article.text.strip()
#             href = article.get('href')
#             if href.startswith('./'):
#                 link = f"https://news.google.com{href[1:]}"
#             else:
#                 link = href

#             publisher_logo = publisher.get('src')
#             # Save to database
#             Article.objects.get_or_create(title=title, link=link, category="science",publisher_logo = publisher_logo)

#             print(f"Saved Article: {title}")
#         except Exception as e:
#             print(f"Error processing article: {e}")


# def scrape_google_news7():    
#     service = Service(r"F:\BTES Training\Module 3 (Back End)\NewsAggrgator\chromedriver-win64\chromedriver.exe")
#     driver = webdriver.Chrome(service=service)
#     ops=webdriver.ChromeOptions()
#     url = "https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en"
#     driver.get(url)

#     driver.implicitly_wait(5)
#     print("Going to for u....")
    
#     sports = driver.find_element(By.XPATH, "//span[text()='Sports']")

#     ops.add_argument("--disable notification")
#     print("gone....")
    
#     # Scroll to load more articles if needed
#     for _ in range(10):
#         driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
#         time.sleep(3)

#     # Parse the page source with BeautifulSoup
#     soup = BeautifulSoup(driver.page_source, "html.parser")
#     driver.quit()

#     articles = soup.find_all('a', class_="gPFEn")
#     publishers = soup.find_all('img', class_="qEdqNd y3G2Ed")
#     print(publishers)
    
#     if not articles:
#         print("No articles found.")
#         return

#     for article,publisher in zip(articles,publishers):
#         try:
#             title = article.text.strip()
#             href = article.get('href')
#             if href.startswith('./'):
#                 link = f"https://news.google.com{href[1:]}"
#             else:
#                 link = href

#             publisher_logo = publisher.get('src')
#             # Save to database
#             Article.objects.get_or_create(title=title, link=link, category="sports",publisher_logo = publisher_logo)

#             print(f"Saved Article: {title}")
#         except Exception as e:
#             print(f"Error processing article: {e}")


# def scrape_google_news8():    
#     service = Service(r"F:\BTES Training\Module 3 (Back End)\NewsAggrgator\chromedriver-win64\chromedriver.exe")
#     driver = webdriver.Chrome(service=service)
#     ops=webdriver.ChromeOptions()
#     url = "https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en"
#     driver.get(url)

#     driver.implicitly_wait(5)
#     print("Going to for u....")
    
#     # tech = driver.find_element(By.XPATH, "//span[text()='Technology']")
#     technology=driver.find_element(By.XPATH,"//*[@id='gb']/div[3]/div/c-wiz/div[1]/div[10]").click()
#     ops.add_argument("--disable notification")
#     print("gone....")
    
#     # Scroll to load more articles if needed
#     for _ in range(10):
#         driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
#         time.sleep(3)

#     # Parse the page source with BeautifulSoup
#     soup = BeautifulSoup(driver.page_source, "html.parser")
#     driver.quit()

#     articles = soup.find_all('a', class_="gPFEn")
#     publishers = soup.find_all('img', class_="qEdqNd y3G2Ed")
#     print(publishers)
    
#     if not articles:
#         print("No articles found.")
#         return

#     for article,publisher in zip(articles,publishers):
#         try:
#             title = article.text.strip()
#             href = article.get('href')
#             if href.startswith('./'):
#                 link = f"https://news.google.com{href[1:]}"
#             else:
#                 link = href

#             publisher_logo = publisher.get('src')
#             # Save to database
#             Article.objects.get_or_create(title=title, link=link, category="technology",publisher_logo = publisher_logo)

#             print(f"Saved Article: {title}")
#         except Exception as e:
#             print(f"Error processing article: {e}")


# if __name__ == "__main__":
#     scrape_google_news()
#     scrape_google_news1()
#     scrape_google_news2()
#     scrape_google_news3()
#     scrape_google_news4()
#     scrape_google_news5()
#     scrape_google_news6()
#     scrape_google_news7()
#     scrape_google_news8()






from bs4 import BeautifulSoup
import requests
from datetime import datetime
from .models import Article
from datetime import datetime


def scrape_cnn():
    # Fetch the XML content from the URL
    url = "https://edition.cnn.com/sitemap/news.xml"
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to fetch CNN Sitemap")
        return
    
    # Parse the XML content with BeautifulSoup
    soup = BeautifulSoup(response.content,'lxml')

    # Extract all <url> elements
    urlsss = soup.find_all('url')

    # Iterate through each <url> and extract relevant data
    for i in urlsss:
        # Extract <news:title>
        title_tag = i.find("news:title")
        title = title_tag.get_text(strip=True)


        # Extract <loc>
        loc_tag = i.find('loc')
        link = loc_tag.get_text(strip = True)

        # Extract <image:loc>
        image_loc_tag = i.find('image:loc')
        image_loc = image_loc_tag.get_text() if image_loc_tag else "None"

        #Extract <video:content_loc>
        video_loc_tag = i.find('video:content_loc')
        video_loc = video_loc_tag.get_text() if video_loc_tag else "None"

        update = i.find('lastmod')
        updated = update.get_text() 
        lastmod = datetime.fromisoformat(updated.replace("Z", "+00:00"))

        publisher_logo = "https://play-lh.googleusercontent.com/bwm2w2FDiqbM4iDj-NRceDS2pMzztQaK-xptPCubSd7xMblWWrNIjITZNVlkcN3tag"

        Article.objects.get_or_create(title=title, link=link, category="home",publisher_logo = publisher_logo, image = image_loc, video = video_loc, lastmod = lastmod)
        print(f"Saved Article: {title}")

        

    # print(urlsss)



def scrape_business_news():
    url = "https://www.hindustantimes.com/feeds/rss/business/rssfeed.xml"
    
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        if response.status_code != 200:
            print("Failed to fetch Business Sitemap")
            return
        
        soup = BeautifulSoup(response.content, 'xml')  # Use 'xml' for RSS feeds

        items = soup.find_all('item')
        for i in items:
            title = i.find("title").get_text(strip=True) if i.find("title") else "No Title"
            link = i.find("link").get_text(strip=True) if i.find("link") else "No Link"
            
            # Extract Image
            media_content = i.find("media:content")
            image_loc = media_content["url"] if media_content else "None"

            # Extract and convert pubDate
            pub_date_tag = i.find("pubDate")
            if pub_date_tag:
                pub_date_str = pub_date_tag.get_text(strip=True)
                lastmod = datetime.strptime(pub_date_str, "%a, %d %b %Y %H:%M:%S %z")  # ✅ Fixed format
            else:
                lastmod = None

            publisher_logo = "https://encrypted-tbn1.gstatic.com/faviconV2?url=https://www.hindustantimes.com&client=NEWS_360&size=96&type=FAVICON&fallback_opts=TYPE,SIZE,URL"

            Article.objects.get_or_create(
                title=title,
                link=link,
                category="business",
                publisher_logo=publisher_logo,
                image=image_loc,
                lastmod=lastmod
            )
            print(f"Saved Article: {title}")

    except Exception as e:
        print(f"Error fetching articles: {e}")



def scrape_entertainment_news():
    url = "https://www.hindustantimes.com/feeds/rss/entertainment/rssfeed.xml"
    
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        if response.status_code != 200:
            print("Failed to fetch Entertainment Sitemap")
            return
        
        soup = BeautifulSoup(response.content, 'xml')  # Use 'xml' for RSS feeds

        items = soup.find_all('item')
        for i in items:
            title = i.find("title").get_text(strip=True) if i.find("title") else "No Title"
            link = i.find("link").get_text(strip=True) if i.find("link") else "No Link"
            
            # Extract Image
            media_content = i.find("media:content")
            image_loc = media_content["url"] if media_content else "None"

            # Extract and convert pubDate
            pub_date_tag = i.find("pubDate")
            if pub_date_tag:
                pub_date_str = pub_date_tag.get_text(strip=True)
                lastmod = datetime.strptime(pub_date_str, "%a, %d %b %Y %H:%M:%S %z")  # ✅ Fixed format
            else:
                lastmod = None

            publisher_logo = "https://encrypted-tbn1.gstatic.com/faviconV2?url=https://www.hindustantimes.com&client=NEWS_360&size=96&type=FAVICON&fallback_opts=TYPE,SIZE,URL"

            Article.objects.get_or_create(
                title=title,
                link=link,
                category="business",
                publisher_logo=publisher_logo,
                image=image_loc,
                lastmod=lastmod
            )
            print(f"Saved Article: {title}")

    except Exception as e:
        print(f"Error fetching articles: {e}")



def scrape_sports_news():
    url = "https://www.hindustantimes.com/feeds/rss/sports/rssfeed.xml"
    
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        if response.status_code != 200:
            print("Failed to fetch Sports Sitemap")
            return
        
        soup = BeautifulSoup(response.content, 'xml')  # Use 'xml' for RSS feeds

        items = soup.find_all('item')
        for i in items:
            title = i.find("title").get_text(strip=True) if i.find("title") else "No Title"
            link = i.find("link").get_text(strip=True) if i.find("link") else "No Link"
            
            # Extract Image
            media_content = i.find("media:content")
            image_loc = media_content["url"] if media_content else "None"

            # Extract and convert pubDate
            pub_date_tag = i.find("pubDate")
            if pub_date_tag:
                pub_date_str = pub_date_tag.get_text(strip=True)
                lastmod = datetime.strptime(pub_date_str, "%a, %d %b %Y %H:%M:%S %z")  # ✅ Fixed format
            else:
                lastmod = None

            publisher_logo = "https://encrypted-tbn1.gstatic.com/faviconV2?url=https://www.hindustantimes.com&client=NEWS_360&size=96&type=FAVICON&fallback_opts=TYPE,SIZE,URL"

            Article.objects.get_or_create(
                title=title,
                link=link,
                category="sports",
                publisher_logo=publisher_logo,
                image=image_loc,
                lastmod=lastmod
            )
            print(f"Saved Article: {title}")

    except Exception as e:
        print(f"Error fetching articles: {e}")




def scrape_technology_news():
    url = "https://www.engadget.com/rss.xml"
    
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        if response.status_code != 200:
            print("Failed to fetch Sports Sitemap")
            return
        
        soup = BeautifulSoup(response.content, 'xml')  # Use 'xml' for RSS feeds

        items = soup.find_all('item')
        for i in items:
            title = i.find("title").get_text(strip=True) if i.find("title") else "No Title"
            link = i.find("link").get_text(strip=True) if i.find("link") else "No Link"
            
            # Extract Image
            media_content = i.find("media:content")
            image_loc = media_content["url"] if media_content else "None"

            # Extract and convert pubDate
            pub_date_tag = i.find("pubDate")
            if pub_date_tag:
                pub_date_str = pub_date_tag.get_text(strip=True)
                lastmod = datetime.strptime(pub_date_str, "%a, %d %b %Y %H:%M:%S %z")  # ✅ Fixed format
            else:
                lastmod = None

            publisher_logo = "https://s.yimg.com/uu/api/res/1.2/maqbCLGSv3qu5gcg3Zi49g--~B/Zmk9ZmlsbDtoPTIwMDtweW9mZj0wO3c9MjAwO2FwcGlkPXl0YWNoeW9u/https://s.yimg.com/os/creatr-uploaded-images/2021-06/80676e30-c472-11eb-bf8e-aa28f7f089bb.cf.jpg"

            Article.objects.get_or_create(
                title=title,
                link=link,
                category="technology",
                publisher_logo=publisher_logo,
                image=image_loc,
                lastmod=lastmod
            )
            print(f"Saved Article: {title}")

    except Exception as e:
        print(f"Error fetching articles: {e}")


def scrape_political_news():
    url = "https://feeds.bbci.co.uk/news/politics/rss.xml"
    
    try:
        # Fetch the RSS feed
        try:
            response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        except requests.RequestException as req_e:
            print(f"Request failed: {req_e}")
            return
        
        # Check if the request was successful
        if response.status_code != 200:
            print("Failed to fetch RSS feed. Status code:", response.status_code)
            return
        
        # Parse the RSS feed
        soup = BeautifulSoup(response.content, 'xml')  # Use 'xml' for RSS feeds
        items = soup.find_all('item')
        
        for i in items:
            # Extract Title
            title = i.find("title").get_text(strip=True) if i.find("title") else "No Title"
            
            # Extract Link
            link = i.find("link").get_text(strip=True) if i.find("link") else "No Link"
            
            # Extract Image
            media_content = i.find("media:thumbnail")
            image_loc = media_content["url"] if media_content else "None"
            
            # Extract and convert pubDate
            pub_date_tag = i.find("pubDate")
            if pub_date_tag:
                pub_date_str = pub_date_tag.get_text(strip=True)
                try:
                    # Adjust for GMT
                    lastmod = datetime.strptime(pub_date_str, "%a, %d %b %Y %H:%M:%S GMT")
                except ValueError as ve:
                    print(f"Date parsing failed for {pub_date_str}: {ve}")
                    lastmod = None
            else:
                # Assign current UTC time as a default
                lastmod = datetime.now(timezone.utc)
            
            # Publisher logo (default for BBC)
            publisher_logo = "https://news.bbcimg.co.uk/nol/shared/img/bbc_news_120x60.gif"
            
            # Save the article in the database
            try:
                Article.objects.get_or_create(
                    title=title,
                    link=link,
                    category="politics",
                    publisher_logo=publisher_logo,
                    image=image_loc,
                    lastmod=lastmod
                )
                print(f"Saved Article: {title}")
            except Exception as db_e:
                print(f"Database error for article '{title}': {db_e}")
    
    except Exception as e:
        print(f"Error fetching articles: {e}")




if __name__ == "__main__":
    scrape_cnn()
    scrape_business_news()
    scrape_entertainment_news()
    scrape_sports_news()
    scrape_technology_news()
    scrape_political_news()
