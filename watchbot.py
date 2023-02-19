from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# set the channel name
channel_name = "LuckyLouie33"

# initialize the Firefox webdriver
driver = webdriver.Firefox()

# navigate to the Twitch homepage
driver.get("https://www.twitch.tv/" + channel_name)

# wait for the page to load
time.sleep(3)

# locate the "Start Watching" div by its text
#start_watching_div = driver.find_element_by_xpath("//div[text()='Start Watching']")
start_watching_div = driver.find_element(By.XPATH, "//div[text()='Start Watching']")

# click the div to start watching the stream
start_watching_div.click()

# Wait for stream to load
time.sleep(1)

### set the player volume to 0.1
# locate the player volume slider by its ID
player_volume_slider = driver.find_element(By.CSS_SELECTOR, "input[id^='player-volume-slider-']")
# use ActionChains to move the slider to the desired value
action_chains = ActionChains(driver)
action_chains.click_and_hold(player_volume_slider).move_by_offset(-49, 0).release().perform()


# keep the window open and the stream playing for 30 minutes
time.sleep(1800)

# close the browser
driver.quit()
