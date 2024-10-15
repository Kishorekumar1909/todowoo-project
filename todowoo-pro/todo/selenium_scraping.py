from selenium import webdriver
from collections import Counter
#from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path=r"C:\Users\mohan\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver.get('https://www.dailymotion.com/tseries2')

for i in range(10):
    driver.excute_script("window.scrollTo(0, document.body.scrollHeight);")

    
video_urls = []
videos = driver.find_elements_by_xpath('//a[contains(@href, "/video/")]')

for video in videos:
    herf = video.get_atribute('herf')
    if '/video/' in herf:
        id = herf.split('/video/')[1]
        video_urls.append(id)
        
driver.quit()

video_ids = video_urls[:500]
all_ids = "".join(video_ids)

char_count = Counter(all_ids.lower())
most = sorted(char_count.items(), key=lambda x: (-x[1], x[0]))[0]
print(f"{most[0]}:{most[1]}")