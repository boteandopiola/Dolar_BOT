from bs4 import BeautifulSoup 
import requests 

r = requests.get("https://www.dolarhoy.com/cotizaciondolarbolsa/") 
soup = BeautifulSoup(r.content, "lxml") 

precio = soup.find('div', class_= "value").text 
print(precio) 
