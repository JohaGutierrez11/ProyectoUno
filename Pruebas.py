import  time
from selenium import webdriver
from selenium.webdriver.common.by import By
#tiempo de espera
t_1=1
t_2=2
#Conexion
#path de donde se encuentra el webdriver
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
#pagina web
driver.get("https://www.demoblaze.com/index.html")
#maximinizar pantalla
driver.maximize_window()
time.sleep(t_1)
#scroll a la pantalla para visualizar productos
driver.execute_script('window.scrollTo(0,300)')
time.sleep(t_1)

### Agregar dos productos en el carrito
#Eligiendo el primer producto
driver.find_element(By.XPATH,"//a[@href='prod.html?idp_=1'][contains(.,'Samsung galaxy s6')]").click()
time.sleep(t_1)
#Agregando el producto
driver.find_element(By.XPATH,"//a[normalize-space()='Add to cart']").click()
time.sleep(t_1)
#Aceptando el producto
alert = driver.switch_to.alert.accept()
driver.save_screenshot('ScreenShot/imagePrimerProducto.png')
time.sleep(t_2)
#Regresando al inicio
driver.find_element(By.ID,'nava').click()
time.sleep(t_1)
driver.execute_script('window.scrollTo(0,600)')
time.sleep(t_2)
#Eligiendo el segundo producto
driver.find_element(By.XPATH,"//a[contains(.,'Iphone 6 32gb')]").click()
time.sleep(t_1)
#Agregando el producto
driver.find_element(By.XPATH,"//a[normalize-space()='Add to cart']").click()
time.sleep(t_1)
#Aceptando el producto
alert = driver.switch_to.alert.accept()
driver.save_screenshot('ScreenShot/imageSegundoProducto.png')
time.sleep(t_2)

## Ir al carrito
driver.find_element(By.ID,"cartur").click()
time.sleep(t_2)

## Ingresando datos en el formulario de compra
driver.find_element(By.XPATH,"//button[@type='button'][contains(.,'Place Order')]").click()
time.sleep(t_1)
driver.find_element(By.ID,"name").send_keys("Johanna Gutierrez")
driver.find_element(By.ID,"country").send_keys("Ecuador")
driver.find_element(By.ID,"city").send_keys("Quito")
driver.find_element(By.ID,"card").send_keys("999999999")
driver.execute_script('window.scrollTo(0,100)')
driver.find_element(By.ID,"month").send_keys("07")
driver.find_element(By.ID,"year").send_keys("1994")
driver.save_screenshot("ScreenShot/imageDatosIngresados.png")
time.sleep(t_2)

### Finalizar la compra
driver.find_element(By.XPATH,"//button[@type='button'][contains(.,'Purchase')]").click()
time.sleep(t_2)
driver.save_screenshot("ScreenShot/imageAceptarCompra.png")
driver.find_element(By.XPATH,"//button[@class='confirm btn btn-lg btn-primary'][contains(.,'OK')]").click()
time.sleep(t_2)

driver.close()