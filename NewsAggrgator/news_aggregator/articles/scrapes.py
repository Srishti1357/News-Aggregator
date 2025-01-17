from selenium import webdriver

driver=webdriver.Chrome()

from selenium.webdriver.common.by import By
ops=webdriver.ChromeOptions()
driver=webdriver.Chrome(ops)
ops.add_argument("--disable notification")
driver.get("https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN%3Aen")

home=driver.find_element(By.CLASS_NAME,"brSCsc").click()
for_u_btn = driver.find_element(By.XPATH, "//*[@class='EctEBd']").click()
ops.add_argument("--disable notification")
follow=driver.find_element(By.XPATH,"//*[@id='gb']/div[3]/div/c-wiz/div[1]/div[3]").click()
ops.add_argument("--disable notification")
news_Show=driver.find_element(By.XPATH,"//*[@id='gb']/div[3]/div/c-wiz/div[1]/div[4]").click()
ops.add_argument("--disable notification")
India=driver.find_element(By.XPATH,"//*[@id='gb']/div[3]/div/c-wiz/div[1]/div[6]").click()
ops.add_argument("--disable notification")
World=driver.find_element(By.XPATH,"//*[@id='gb']/div[3]/div/c-wiz/div[1]/div[7]").click()
ops.add_argument("--disable notification")
Local=driver.find_element(By.XPATH,"//*[@id='gb']/div[3]/div/c-wiz/div[1]/div[8]").click()
ops.add_argument("--disable notification")
Business=driver.find_element(By.XPATH,"//*[@id='gb']/div[3]/div/c-wiz/div[1]/div[9]").click()
ops.add_argument("--disable notification")





technology=driver.find_element(By.XPATH,"//*[@id='gb']/div[3]/div/c-wiz/div[1]/div[10]").click()
ops.add_argument("--disable notification")
entertain=driver.find_element(By.XPATH,"//*[@id='gb']/div[3]/div/c-wiz/div[1]/div[11]").click()
ops.add_argument("--disable notification")
sport=driver.find_element(By.XPATH,"//*[@id='gb']/div[3]/div/c-wiz/div[1]/div[12]").click()
ops.add_argument("--disable notification")
science=driver.find_element(By.XPATH,"//*[@id='gb']/div[3]/div/c-wiz/div[1]/div[13]").click()
ops.add_argument("--disable notification")
health=driver.find_element(By.XPATH,"//*[@id='gb']/div[3]/div/c-wiz/div[1]/div[14]").click()
ops.add_argument("--disable notification")