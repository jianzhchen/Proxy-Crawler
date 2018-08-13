from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import webbrowser


def main():
    url = 'http://spys.one/free-proxy-list/CN/'
    http_only = True
    outputfile = "output.txt"
    ip_port_list = []

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(url)
    driver.find_element_by_css_selector("select#xpp > option[value='2']").click()
    if http_only:
        driver.find_element_by_css_selector("select#xf5 > option[value='1']").click()
    html = driver.page_source
    html = BeautifulSoup(html, 'html.parser')
    inner = html.select('body > table')[1].tbody
    inner = inner.find_all('tr', recursive=False)[3].td.table.tbody
    inner = inner.find_all('tr', {"onmouseover": "this.style.background='#002424'"}, recursive=False)

    for row in inner:
        ip_port_list.append([row.find_all('font')[1].contents[0], row.find_all('font')[1].contents[3]])

    file = open(outputfile, 'w')
    for pair in ip_port_list:
        ip = pair[0]
        port = pair[1]
        proxy = str(ip) + ':' + str(port)
        print(proxy)
        file.write(proxy + '\n')

    file.close()
    webbrowser.open(outputfile)

main()
