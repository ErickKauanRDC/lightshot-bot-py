from PIL import Image 
from selenium import webdriver
from time import sleep
from random import choice
from selenium.webdriver.common import action_chains
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
import string
import random
from selenium.webdriver import ActionChains
def randomUrl():
    letras = string.ascii_lowercase
    numeros = string.digits
    url = ''
    for i in range(2):
        url += choice(letras)
    for i in range(4):
        url += choice(numeros)
    return url

def pegarImagemUm():
    driver = webdriver.Chrome()
    driver.get('https://prnt.sc/'+randomUrl())
    sleep(3)
    img = driver.find_element_by_xpath('/html/body/div[3]/div/div/img')
    with open('image1.png','wb') as file:
        file.write(img.screenshot_as_png)
    driver.close()
def pegarImagemDois():
    driver = webdriver.Chrome()
    driver.get('https://prnt.sc/'+randomUrl())
    sleep(3)
    img = driver.find_element_by_xpath('/html/body/div[3]/div/div/img')
    with open('image2.png','wb') as file:
        file.write(img.screenshot_as_png)
    driver.close()
def juntarImagens():
    imagem1 = Image.open('image1.png')
    imagem2 = Image.open('image2.png')
     
    aux = ''
    if(imagem2.height*imagem2.width > imagem1.height*imagem1.width):
        aux = imagem1
        imagem1 = imagem2
        imagem2 = aux
    x = random.randint(0,imagem1.width)
    y = random.randint(0,imagem1.height)   
    x = int(x/4)
    y = int(y/4)
    imagem1.paste(imagem2,(x,y))
    print(x)
    print(y)
    imagem1.resize
    imagem1.save('imagem-final.png')
def postar():
    driver = webdriver.Chrome()
    a = ActionChains(driver)
    driver.get('file:///C:/Users/erick/lightshot-bot-py/imagem-final.png')
    sleep(5)
    a.key_down(Keys.CONTROL).send_keys('C').key_up(Keys.CONTROL).perform()
    driver.get('https://twitter.com/home')
    sleep(5)
    driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input').send_keys('**********')#Login 
    driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input').send_keys('**********')#Senha
    driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span/span').click()
    sleep(5)
    driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div').click()
    driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div').click()
    driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div').send_keys(Keys.CONTROL+"v")
    a.key_down(Keys.CONTROL).send_keys('V').key_up(Keys.CONTROL).perform()

    sleep(5)
    driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]').click()
    sleep(5)
    driver.close()

while 1<2:
    pegarImagemUm()
    pegarImagemDois()
    juntarImagens()
    postar()
