entregables:
1 Repositorio público en GitHub con todo el código del proyecto: https://github.com/PabloMeoniz/pre-entrega-automation-testing-Pablo-Meoniz
2 Arcihvo README.md que incluya:
Proposito del proyecto: Testear una página web de compras utilizando tecnologias de testing automático y con reportes.

Tecnologias utilizadas:
Python como lenguaje principal, Selenium webdriver para automatización, Pytest para extructura de testing y git para control de versionado subido a Github para compartir en público.

Instrucciones de instalación de dependencias:
instalar git desde el sitio oficial
git.exe
instlar python desde el sitio oficial
python.exe
instalar pytest y pytest-html 
pip install pytest
pip install pytest-html
pip install selenium
Loguearse en Github y ejecutar: 
git init
git commit -m "first commmit"
git branch -M main
git remote add origin https://github.com/PabloMeoniz/pre-entrega-automation-testing-Pablo-Meoniz
git push -u origin main

3 Reporte HTML generado por Pytest con resultados de la ejecución.

Comado para ejecutar los reportes:
Pytest -v --html=../reports/reporte.html


4 Evidencias adicionales: capturas de pantalla automáticas en caso de fallos y logs de ejecución.
comando para realizar las capturas: 
def driver():
    #configurcion para consultar a selenium web driver
    driver = get_driver()
    yield driver
    driver.quit()

driver.save_screenshot("evidencia_productos_carrito.png") 

Estructura minima:
test/
utils/(funciones auxiliares)
reports/

Compartir enlace al repositorio antes de la fecha limite
https://github.com/PabloMeoniz/pre-entrega-automation-testing-Pablo-Meoniz
Commits frecuentes y con mensajes descriptivos que reflejen el progreso.

README.md completo y claro.
    datos/ (si aplica datos externos como CSV/JSON)
    reports/ (reportes HTML y capturas)

