# Строим сеть
# docker network create grid
# Запускаем hub
# docker run -d -p 4442-4444:4442-4444 --net grid --name selenium-hub selenium/hub:latest
#
# запускаем узел на firefox
# docker run -d --net grid -e SE_EVENT_BUS_HOST=selenium-hub --shm-size="2g" -e SE_EVENT_BUS_PUBLISH_PORT=4442  -e SE_EVENT_BUS_SUBSCRIBE_PORT=4443 selenium/node-firefox:latest
# запускаем узел на chrome
# docker run -d --net grid -e SE_EVENT_BUS_HOST=selenium-hub --shm-size="2g" -e SE_EVENT_BUS_PUBLISH_PORT=4442  -e SE_EVENT_BUS_SUBSCRIBE_PORT=4443 selenium/node-chrome:latest
#
# Направьте свои тесты WebDriver на hub_url = "http://localhost:4444/wd/hub"
#
#
# hub_url = "http://localhost:4444/wd/hub"
# options = webdriver.ChromeOptions()
# options.set_capability("platformName", "linux")
# options2 = webdriver.FirefoxOptions()
# options2.set_capability("platformName", "linux")
#
# Подключитесь к удаленному браузеру через Selenium Grid
# driver = webdriver.Remote(command_executor=hub_url, options=options)
# driver2 = webdriver.Remote(command_executor=hub_url, options=options2)


from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#hub_url = "http://192.168.1.5:4444/wd/hub"
hub_url = "http://localhost:4444/wd/hub"
#capabilities = DesiredCapabilities.CHROME.copy()
#capabilities["platform"] = "LINUX"  # Используйте "LINUX" для контейнеров

options = webdriver.ChromeOptions()
options.set_capability("platformName", "linux")
options2 = webdriver.FirefoxOptions()
options2.set_capability("platformName", "linux")


#options["platform"] = "LINUX"

# Подключитесь к удаленному браузеру через Selenium Grid
driver = webdriver.Remote(command_executor=hub_url, options=options)
driver2 = webdriver.Remote(command_executor=hub_url, options=options2)
driver3 = webdriver.Remote(command_executor=hub_url, options=options)


#driver = webdriver.Remote(command_executor=hub_url, options=options)

#caps = options.to_capabilities()
#caps = {"browserName": "chrome"}
#driver = webdriver.Remote("http://localhost:4444/wd/hub")
url = 'https://www.google.ru/'
driver.get(url)
driver2.get(url)
#driver.quit()

#docker run -d -p 4444:4444 -p 7900:7900 --shm-size="2g" selenium/standalone-chrome:latest