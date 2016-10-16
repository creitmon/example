from selenium import webdriver


class Ad:
    def __init__(self, url, title, price, owner_name, added_date, location, product_condition):
        self.url = url
        self.title = title
        self.price = price
        self.owner_name = owner_name
        self.added_date = added_date
        self.location = location
        self.product_condition = product_condition



browser = webdriver.Chrome()
browser.get("https://olx.ua")
browser.find_element_by_css_selector("input#headerSearch")

elem = browser.find_element_by_css_selector("input#headerSearch")
# elem.send_keys("iphone 7\n") #поиск запускается имитируя энтер \n
elem.send_keys("iphone 7")
elem.submit()  # подтвеждение введенных данных поиска

elements_with_links = browser.find_elements_by_css_selector('h3 > a.detailsLink')  # ищет по названию

# for elem in elements_with_links:
#     elem.get_attribute('href')
# elements_with_links = cli.find_elements_by_css_selector('img.fleft') #ищет по картинке

links = [x.get_attribute('href') for x in elements_with_links]
parsed_elements = []
for link in links:
    browser.get(link)
    title = browser.find_element_by_css_selector('h1.brkword').text
    price = browser.find_elements_by_css_selector('div.pricelabel')[0].text
    owner_name = browser.find_elements_by_css_selector('div.userdetails > span.xx-large')[0].text
    added_date = browser.find_elements_by_css_selector('span.pdingleft10.brlefte5')[0].text.split(',')[1]
    address = browser.find_elements_by_css_selector('strong.c2b')[0].text
    product_condition = browser.find_elements_by_css_selector('strong > a')[3].text
    description = browser.find_element_by_css_selector('p.pding10')[0].text
    parsed_elements.append(Ad(link,
                              title,
                              price,
                              owner_name,
                              added_date,
                              address,
                              product_condition,
                              description))
