from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
import time

# Set to headless
options = Options()
options.headless = True

# set the channel name
channel_name = "LuckyLouie33"

# initialize the Firefox webdriver
driver = webdriver.Firefox()

# navigate to the Twitch homepage
driver.get("https://www.twitch.tv/" + channel_name)

# wait for the page to load
time.sleep(3)

try:
    # locate the "Start Watching" div by its text
    start_watching_div = driver.find_element(By.XPATH, "//div[text()='Start Watching']")

    # click the div to start watching the stream
    start_watching_div.click()

except:
    pass
    #print("Start Watching div")

# Wait for stream to load
time.sleep(1)

### set the player volume to 0.1
# locate the player volume slider by its ID
player_volume_slider = driver.find_element(By.CSS_SELECTOR, "input[id^='player-volume-slider-']")
# use ActionChains to move the slider to the desired value
action_chains = ActionChains(driver)
# Turn the volume down by dragfging the mouse (offset is pixels - not volume-units)
action_chains.click_and_hold(player_volume_slider).move_by_offset(-45, 0).release().perform()


# keep the window open and the stream playing for 30 minutes
time.sleep(1800)

# close the browser
driver.quit()
