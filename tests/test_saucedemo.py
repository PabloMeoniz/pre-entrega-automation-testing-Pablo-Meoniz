import pytest
from selenium.webdriver.common.by import By
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # Agrega el directorio padre al path
from utils.helpers import login_sauce_demo
from utils.helpers import get_driver
@pytest.fixture
def driver():
    #configurcion para consultar a selenium web driver
    driver = get_driver()
    yield driver
    driver.quit()

"""
def test_login(driver):
    login_sauce_demo(driver) # evalua la funcion de login si funciona correctamente
    assert "/inventory.html" in driver.current_url #evalua si esta en la pagina de inventario despues del login
    titulo = driver.find_element(By.CSS_SELECTOR, "div.header_secondary_container .title").text #busca el titulo de la pagina
    assert titulo == 'Products' #verifica que el titulo sea PRODUCTS
"""

"""
def test_catalogo(driver):
    login_sauce_demo(driver)

    products = driver.find_elements(By.CLASS_NAME, 'inventory_item')                #busca los productos en la pagina
    products = driver.find_elements(By.CLASS_NAME, 'inventory_list')                # busca los productos en la pagina
    assert len(products) > 0                                                        #verifica que haya productos en la pagina
    
                                                                                    #logeo de usuario con username y password
                                                                                    #click al boton de login
                                                                                    #podamos verificar el titulo pero del html
                                                                                    #comprobar si existen productos en la pagina visibles (len()>0)
                                                                                    #verificar elementos importantes de la pagina
"""   


def test_carrito(driver):
    login_sauce_demo(driver)

    products = driver.find_elements(By.CLASS_NAME, 'inventory_list')                #busca los productos en la pagina
    total_products = len(products)                                              # cuenta la cantidad de productos encontrados       
    products[0].find_element(By.TAG_NAME, 'button').click()                          # hace click en el boton del primer producto para agregar al carrito

    badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
    assert badge ==       #busca el elemento del carrito
     #logueo de usuario con username y password
    #click al boton de login
    #redirigir a la pagina de inventario (ventanita principal)

'''
def test_carrito():
    #logeo de usuario con username y password
    #click al boton de login
    #llevarme a la pagina de carrito de compra
    #incremento de carrito al agregar un producto al carrito
    #comprobar que en el carrito aparezca el producto correcto

'''