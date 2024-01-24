from selenium import webdriver
a = [1, 2, 2, 4, 5, 6, 7, 8]
print(len(a))
for i in range(0,len(a)):
    a.pop()
print(a)

weights = [70, 80, 90]
costs = [100, 200, 300]

print(zip(weights, costs))

for weight, cost in zip(weights, costs):
    print(f'Weight: {weight}, Cost: {cost}')

options = webdriver.ChromeOptions()
# caps = webdriver.DesiredCapabilities.CHROME.copy()
caps = options.to_capabilities()
caps['unexpectedAlertBehaviour'] = "dismiss"
browser_driver = webdriver.Chrome(desired_capabilities=caps)
print(browser_driver.capabilities)

browser_driver.quit()