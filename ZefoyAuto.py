import utils
import undetected_chromedriver as uc
from time import sleep
from selenium.webdriver import ChromeOptions
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image



class ZefoyAutomator:
    def __init__(self, post_url, type = "views") -> None:
        self.post_url = post_url
        self.type = type
        self.options = ChromeOptions()
        self.selectors = {
            "captcha_input": "body > div.noscriptcheck > div.ua-check > form > div > div > div > input",
            "captcha_img": "img",
            "close_captcha_error": "#errorcapthcaclose > div > div > div.modal-footer > button",
            "followers": "body > div:nth-child(8) > div > div.noscriptcheck > div > div > div:nth-child(2) > div > button",
            "hearts": "body > div:nth-child(8) > div > div.noscriptcheck > div > div > div:nth-child(3) > div > button",
            "comment_hearts": "body > div:nth-child(8) > div > div.noscriptcheck > div > div > div:nth-child(4) > div > button",
            "views": "body > div:nth-child(8) > div > div.noscriptcheck > div > div > div:nth-child(5) > div > button",
            "shares": "body > div:nth-child(8) > div > div.noscriptcheck > div > div > div:nth-child(6) > div > button",
            "favorites": "body > div:nth-child(8) > div > div.noscriptcheck > div > div > div:nth-child(6) > div > button",
            "live_stream": "body > div:nth-child(8) > div > div.noscriptcheck > div > div > div:nth-child(7) > div > button",
            "search_input": "body > div.col-sm-5.col-xs-12.p-1.container.t-views-menu > div > form > div > input",
            "search_button": "body > div.col-sm-5.col-xs-12.p-1.container.t-views-menu > div > form > div > div > button",
            "send_button": "#c2VuZC9mb2xeb3dlcnNfdGlrdG9V > div.row.text-light.d-flex.justify-content-center > div > form > button",
            "wait_time_paragraph": "#c2VuZC9mb2xeb3dlcnNfdGlrdG9V > span.br.views-countdown"
        }
        self.domain = "https://zefoy.com/"
        self.headless = True
        self.driver = None
    
    def solve_captcha(self): 
        solved = False
        while not solved:
            wait = WebDriverWait(self.driver, 5)
            captcha_img = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.selectors["captcha_img"])))
            captcha_input = self.driver.find_element(By.CSS_SELECTOR, self.selectors["captcha_input"])
            captcha_img.screenshot("captcha.png")
            
            image = Image.open("captcha.png")
            image.show()
            captcha_answer = input("Enter the captcha answer: ")
            captcha_input.send_keys(captcha_answer)
            captcha_input.submit()
            image.close()
            
            try:
                close_error_dial = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.selectors["close_captcha_error"])))
                close_error_dial.click()
                print("Captcha incorrect")
            except (TimeoutException, NoSuchElementException) as e:
                print("Captcha passed!")
                solved = True
            
    def send(self):
        wait = WebDriverWait(self.driver, 5)
        search_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.selectors["search_button"])))
        search_button.click()
        try:
            print(f"Attempting to send {self.type}...")
            sleep(5)
            paragraph_wait_time = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.selectors["wait_time_paragraph"]))).text
            wait_time = utils.convert_time_to_seconds(paragraph_wait_time)
            print(f"Waiting {wait_time} seconds before sending next batch...")
        except (NoSuchElementException, TimeoutException) as e:
            send_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.selectors["send_button"])))
            send_button.click()
            print("Successfully sent 1000+ views")
        finally:
            sleep(5)
            return self.send()
    
    def launch(self):
        try:
            self.driver = uc.Chrome(headless=self.headless)
            self.driver.get(self.domain)
            self.solve_captcha()
            
            wait = WebDriverWait(self.driver, 5)
            
            bot_options_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.selectors[self.type])))
            bot_options_button.click()
            send_bots_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.selectors["search_input"])))
            send_bots_input.send_keys(self.post_url)
        except:
            self.driver.quit()
        

post_url = input("Enter tiktok post url: ")
botter = ZefoyAutomator(post_url)
botter.launch()
botter.send()