from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class InstagramBot:
    def __init__(self, username, password, hashtag):
        self.username = username
        self.password = password
        self.hashtag = hashtag
        self.driver = webdriver.Chrome(executable_path=r'/Users/jacquesjacob/Downloads/chromedriver')

    def login(self):
        driver = self.driver
        driver.get('https://instagram.com')
        time.sleep(3)
        #login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        #login_button.clear()
        user_element = driver.find_element_by_xpath("//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        password_element = driver.find_element_by_xpath("//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)
        time.sleep(6)
        self.curtir_fotos(self.hashtag)

    def wait_until(self, condition, timeout=5):
        # helper to wait for element appearance
        pass

    def curtir_fotos(self, hashtag):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        time.sleep(5)
        for i in range(1, 4):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        [href for href in pic_hrefs if hashtag in hrefs]
        print(hashtag + ' total fotos: ' + str(len(pic_hrefs)))
        contagem = 0
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            time.sleep(2)
            #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                self.wait_until(ec.presence_of_element_located((By.CLASS_NAME, 'fr66n')))
                self.driver.find_element_by_class_name('fr66n').click()
                contagem = contagem + 1
                print(f"sucesso post {contagem}")
                time.sleep(3)
                try:
                    self.wait_until(ec.presence_of_element_located((By.CLASS_NAME, 'e1e1d')))
                    self.driver.find_element_by_class_name('e1e1d').click()
                    time.sleep(2)
                    self.wait_until(ec.presence_of_element_located((By.CLASS_NAME, 'vBF20._1OSdk')))
                    self.driver.find_element_by_class_name('vBF20._1OSdk').click()
                    time.sleep(9)
                    print(f"sucesso seguindo instagram {contagem}")
                except Exception as e:
                    print(f"nao foi possivel seguir este instagram {contagem}.")
                    time.sleep(3)
            except Exception as e:
                print(f"Erro: nao foi possivel curtir e seguir este post!")
                time.sleep(3)


karenbot = InstagramBot('username', 'password', 'hashtag')
karenbot.login()