from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from os import mkdir
from os.path import isdir
from pathlib import Path


base_dir = Path(__file__).parent.resolve()
tweets_dir = f"{base_dir}/tweets"

base_url = "https://twitter.com"

timeout = 1

tweets_container_xpath = '//div[starts-with(@aria-label, "Timeline: ") and substring-after(@aria-label, "’s") = " Tweets"]'

if isdir(tweets_dir) is not True:
    mkdir(tweets_dir)

print("\nPreparing the WebDriver")

service = Service(executable_path=ChromeDriverManager().install())

options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920, 1080")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--disable-gpu")
options.add_argument("--disable-extensions")
options.add_argument("--dns-prefetch-disable")
options.add_argument("--disk-cache-size=1")
options.add_argument("--media-cache-size=1")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 6.1; rv:50.0) Gecko/20100101 Firefox/50.0")
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.page_load_strategy = "normal"

driver = webdriver.Chrome(service=service, options=options)
driver.implicitly_wait(timeout)
