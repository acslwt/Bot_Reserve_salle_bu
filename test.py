import datetime
import json
import quickstart

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def liste_classname_function(liste):
      return liste.split()

#Creation des horaires libres

salle_libre = quickstart.main()
print(salle_libre)

#Importer les horaires ou je dois reserver.

# Créer une session Firefox

options = Options()
# options.headless = True
options.binary_location = r"C:/Program Files/Mozilla Firefox/firefox.exe"
driver = webdriver.Firefox(executable_path="C:\Python310\geckodriver.exe",options=options)
driver.implicitly_wait(30)
driver.maximize_window()

#Obtenir le jour actuel

# now = datetime.datetime.today()

# url = "https://affluences.com/bu-sciences-1/reservation?type=3381&date="+str(now.year)+"-"+str(now.month)+"-"+str(now.day+5)
# driver.get(url)

# button = driver.find_element(By.XPATH,"//button[text()=' 9:00 AM ']")
# liste_classname = liste_classname(button.get_attribute("class"))
# print(liste_classname)
######################################################################
for i in range(3,len(salle_libre)):
  actual_date_reserve = datetime.datetime.today()+datetime.timedelta(i)
  print(actual_date_reserve)
  day = actual_date_reserve.day
  month = actual_date_reserve.month
  if day<10:
        day = "0"+str(day)
  if month<10:
        day = "0"+str(month)
        
  url = "https://affluences.com/bu-sciences-1/reservation?type=3381&date="+str(actual_date_reserve.year)+"-"+str(month)+"-"+str(day)
  driver.get(url)
  print("tu es sur la page : "+url)
  for hour in salle_libre[i]:
    current_hour = "//button[text()=' "+str(hour%12)+":00 AM ']"
    heure_reserve = driver.find_elements_by_xpath(current_hour)
    number_reserve_possible = len(heure_reserve)
    print("Nombre reservation possible : "+str(number_reserve_possible))
    current_reserve = 0
    unselectable = True
    while current_reserve<number_reserve_possible and unselectable:
      liste_classname = liste_classname_function(heure_reserve[current_reserve].get_attribute("class"))
      if 'unselectable' not in liste_classname:
        unselectable = False
      current_reserve+=1
    if(unselectable==False):
      heure_for_reserve=heure_reserve[current_reserve-1]
      driver.execute_script("arguments[0].click();",heure_for_reserve)
      print("tu clique sur : "+str(heure_for_reserve.text))
      
      button_book = heure_for_reserve.find_element(By.XPATH,"..")
      button_book = heure_for_reserve.find_element(By.XPATH,"..")
      button_book = heure_for_reserve.find_element(By.XPATH,"..")
      button_book = heure_for_reserve.find_element(By.XPATH,"//span[text()='Book']")
      button_book = button_book.find_element(By.XPATH,"..")
      button_book = button_book.find_element(By.XPATH,"..")
      button_book = button_book.find_element(By.XPATH,"..")
      button_book.click()
      print("tu clique sur : "+str(button_book.text))

# Localiser la zone de texte
# heure_reserve = driver.find_elements_by_xpath("//button[text()=' 8:00 AM ']")
# button_reserve = button_reserve.find_element(By.XPATH,"..")
# button_reserve = button_reserve.find_element(By.XPATH,"..")
# button_reserve = button_reserve.find_element(By.XPATH,"..")
# print(heure_reserve)
print("_________________________________________________")
# print(button_reserve.find_element(By.XPATH,"//span[text()='Book']").text)
# search_field = driver.find_element(By.XPATH, "//input[@name='q']")
# search_field.clear()

# # Saisir et confirmer le mot-clé
# search_field.send_keys("Mot-clé")
# search_field.submit()

# # Consulter la liste des résultats affichés à la suite de la recherche
# # à l’aide de la méthode find_elements_by_class_name
# lists= driver.find_elements_by_class_name("_Rm")

# # Passer en revue tous les éléments et restituer le texte individuel

# i=0
# for listitem in lists:
#   print (listitem.get_attribute("innerHTML"))
#   i=i+1
#   if(i>10):
#     break

# # Fermer la fenêtre du navigateur
# driver.quit()