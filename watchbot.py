from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Replace with your Chromedriver executable path
chromedriver_path = 'C:/Users/dijikul/Downloads/chromedriver.exe'

# Replace with the Twitch username you want to watch
twitch_username = 'LuckyLouie33'

# Initialize Chromedriver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Maximize window
driver = webdriver.Chrome(chromedriver_path, options=options)

# Navigate to Twitch homepage
driver.get('https://www.twitch.tv')

# Wait for the search box to load and enter the channel name
search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[@data-a-target="tw-input"]'))
)
search_box.send_keys(twitch_username)
search_box.send_keys(Keys.RETURN)

# Wait for the search results to load and click on the correct channel
channel_link = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, f'//a[@data-a-target="preview-card-image-link"][@href="/{twitch_username}"]'))
)
channel_link.click()

# Wait for the stream to load and click on the play button
play_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//button[@data-a-target="player-play-pause-button"]'))
)
play_button.click()

# Keep the window open to watch the stream
input('Press Enter to quit')
driver.quit()
