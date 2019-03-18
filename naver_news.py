from selenium import webdriver

keyword = ["소통", "팀워크", "협력", "도전", "능동", "열정", "적극", "성실", "근면", "정직", "인내심", "창의", "글로벌역량", "주인의식", "책임"]#15개

driver = webdriver.Chrome("C:/Users/abcd_/workspace/chromedriver.exe")
driver.get("https://search.naver.com/search.naver?where=news&sm=tab_jum")

# 검색옵션 열어놓기
elem = driver.find_element_by_id("_search_option_btn")
elem.click()

for word in keyword:
    #검색창 clear
    driver.find_element_by_id("nx_query").clear()

    # 검색창 입력
    elem = driver.find_element_by_id("nx_query")
    elem.send_keys(word)

    # 검색클릭
    elem = driver.find_element_by_class_name("bt_search")
    elem.click()

    # 기간옵션클릭
    elem = driver.find_element_by_xpath('//*[@id="snb"]/div/ul/li[2]')
    elem.click()

    # 1년 클릭
    elem = driver.find_element_by_xpath('//*[@id="_nx_option_date"]/div[1]/ul[1]/li[6]')
    elem.click()

    savePath = "C:/news/" + word + ".txt"
    saveFile = open(savePath, 'w', encoding='utf8')

    ###############300페이지 뉴스 끌어오기
    for page in range(300):
        news = driver.find_element_by_class_name("type01")
        news = news.find_elements_by_tag_name("li")

        for i in range(len(news)):
            article_id = news[i].get_attribute("id")
            if article_id == "":
                continue
            #print("id=", article_id)
            xpath = '//*[@id="'+article_id+'"]/dl' #/dt/a'

            title = news[i].find_element_by_xpath(xpath+'/dt/a').get_attribute("title")
            saveFile.write(title)
            print(title)

            article = news[i].find_element_by_xpath(xpath+'/dd[2]').text
            saveFile.write(article)
            print(article)

        driver.find_element_by_class_name("next").click()
    ##############

    saveFile.close()
