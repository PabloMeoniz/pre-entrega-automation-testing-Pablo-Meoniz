import pytest
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


def test_login(driver):
    login_sauce_demo(driver)
    #logueo de usuario con username y password
    #click al boton de login
    #redirigir a la pagina de inventario (ventanita principal)

'''
def test_catalogo():
    #logeo de usuario con username y password
    #click al boton de login
    #podamos verificar el titulo pero del html
    #comprobar si existen productos en la pagina visibles (len()>0)
    #verificar elementos importantes de la pagina
def test_carrito():
    #logeo de usuario con username y password
    #click al boton de login
    #llevarme a la pagina de carrito de compra
    #incremento de carrito al agregar un producto al carrito
    #comprobar que en el carrito aparezca el producto correcto

'''