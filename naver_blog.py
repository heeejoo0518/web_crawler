from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime

keyword = ["소통", "팀워크", "협력", "도전", "능동", "열정", "적극", "성실", "근면", "정직", "인내심", "창의", "글로벌역량", "주인의식", "책임"]#15개

#오늘, 일년전 날짜 계산
today = datetime.today()
past = datetime(today.year-1, today.month, today.day)
today = today.strftime("%Y.%m.%d")
past = past.strftime("%Y.%m.%d")

baseUrl = "https://section.blog.naver.com/Search/Post.nhn"
baseUrl = baseUrl + "?startDate="+past+"&endDate="+today + "&rangeType=PERIOD"

driver = webdriver.Chrome("C:/Users/abcd_/workspace/chromedriver.exe")
driver.get(baseUrl)

for word in keyword:
    #파일 경로지정&오픈
    savePath = "C:/blog/" + word + ".txt"
    saveFile = open(savePath, 'w', encoding='utf8')

    # 검색창 clear
    driver.find_element_by_name("sectionBlogQuery").clear()

    # 검색창 입력
    elem = driver.find_element_by_name("sectionBlogQuery")
    elem.send_keys(word)

    # 검색클릭
    elem = driver.find_element_by_xpath('//*[@id="header"]/div[1]/div/div[2]/form/fieldset/a[1]')
    elem.click()

    ###############300페이지 블로그 끌어오기
    for page in range(1,301):
        blogs = driver.find_elements_by_class_name("list_search_post")
        for blog in blogs:
            title = blog.find_element_by_class_name("title").text
            saveFile.write(title)
            print(title)
            try:
                body = blog.find_element_by_class_name("text").text
                saveFile.write(body)
            except NoSuchElementException:
                print("본문없음")

        driver.get(baseUrl + "&pageNo=" + str(page+1)+"&keyword="+word)

    ###############
    saveFile.close()
