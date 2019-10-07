import selenium
import time
from selenium.webdriver.common.keys import Keys
class TwitterBot:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.bot= selenium.webdriver.Chrome('C:/Users/KRISH SHAH/Downloads/chromedriver_win32/chromedriver')
    def login(self):
    	bot=self.bot 
    	bot.get("https://twitter.com/login") 
    	print("login page arrived")
    	time.sleep(3)
    	email=bot.find_element_by_class_name('js-username-field') 
    	passw=bot.find_element_by_class_name('js-password-field') 
    	email.clear()
    	print('cleared email')
    	passw.clear()
    	print('cleared password')
    	email.send_keys(self.username)
    	print('entered username')
    	passw.send_keys(self.password)
    	print('entered password')
    	passw.send_keys(Keys.RETURN)
    	print('Succesfully Logged in'+self.username)
    	time.sleep(3)
    	 
    def searchfor(self,hashtag):
    	bot=self.bot
    	bot.get('https://twitter.com/search?q='+hashtag+'%20&src=typed_query')
    	print('Searching for hashtag '+hashtag+'...')
    	for i in range(1,3):
    		bot.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    		print('Scrolling')
    		time.sleep(3)	
    def like(self):
    	bot=self.bot
    	like=bot.find_elements_by_class_name('r-4qtqp9')
    	for l in like:
    		l.click()	
    		time.sleep(5)	

k=TwitterBot('888888','88888')
k.login()
k.searchfor('Artificial')
k.like()