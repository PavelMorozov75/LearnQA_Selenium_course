from selenium import webdriver
a = [1, 2, 2, 4, 5, 6, 7, 8]
print(len(a))
for i in range(0,len(a)):
    a.pop()
print('a = ', a)

weights = [70, 80, 90]
costs = [100, 200, 300]

print(zip(weights, costs))

for weight, cost in zip(weights, costs):
    print(f'Weight: {weight}, Cost: {cost}')

options = webdriver.ChromeOptions()
caps = webdriver.DesiredCapabilities.CHROME.copy()
#caps = options.to_capabilities()
caps['unexpectedAlertBehaviour'] = "dismiss"
browser_driver = webdriver.Chrome(desired_capabilities=caps)
print(browser_driver.capabilities)

browser_driver.quit()
#_____________________________________________________________
options = webdriver.ChromeOptions()
caps = options.to_capabilities()
caps["profile.default_content_settings.popups"] = 0
caps["download.default_directory"] = "/path/to/download/directory"

driver = webdriver.Chrome(desired_capabilities=caps)
print(driver.capabilities)
driver.quit()

#Новая рабочая схема для selenium выше 4.10
options = webdriver.ChromeOptions()
options.set_capability("platformName", "windows")
options.set_capability('unexpectedAlertBehaviour', 'dismiss')


browser_driver = webdriver.Chrome(options=options)
print(browser_driver.capabilities)
browser_driver.quit()