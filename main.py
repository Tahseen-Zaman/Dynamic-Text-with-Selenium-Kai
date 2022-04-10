from selenium import webdriver 
from selenium.webdriver.chrome.options import Options

def get_drvier():
  # Set options to make browsing easier
  options = Options()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(options=options)
  driver.get("https://www.accuweather.com/en/bd/dhaka/28143/current-weather/28143")
  return driver
def text_modify(text):
  #Modify The Text from webdriver
  fahrenheit = int(text.split("°")[0])
  celsius = (fahrenheit -32)*5/9
  celsius = float("{:.2f}".format(celsius))
  output = "The Temperature now at Dhaka is " + str(celsius) + " degrees celsius"
  return output

def main(): 
  driver = get_drvier()
  element = driver.find_element(by="xpath", value="/html/body/div/div[5]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div/div")
  return text_modify(element.text)

print(main())