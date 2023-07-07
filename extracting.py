from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

web_url = 'https://www.thesun.co.uk/sport/football/'
path = 'C:\Development\chromedriver'

options = Options()
options.headless = True

service = Service(executable_path = path)
driver = webdriver.Chrome(service = service)

driver.get(web_url)

news_container = driver.find_elements(by='xpath',value='//div[@class="teaser-item teaser__small  theme-football"]')
all_titles = []
all_subtitles = []
all_links = []
for container in news_container:
    title = container.find_element(by='xpath',value='./div/a/span')
    sub_title = container.find_element(by='xpath',value='./div/a/h3')
    # link = container.find_element(by='xpath',value='./div/a')
    all_titles.append(title.text)
    all_subtitles.append(sub_title.text)
    # all_links.append(link)


# print(all_titles)
# print(all_subtitles)
# print(all_links)


import pandas as pd
data_dict = {
    'title': all_titles,
    'sub_title': all_subtitles
}

df = pd.DataFrame(data_dict)
try:
    df.to_csv('football_headlines.csv', index=False)
except:
    FileExistsError()



# //div[@class="teaser-item teaser__small  theme-football"]/a
# news_content = []
# for new_news in news:
#     news_content.append(new_news.text)

# news_content = [each_news.text for each_news in news]
# print(news_content)


# //div[@class="teaser-item teaser__small  theme-football"]