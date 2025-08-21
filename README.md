# 🚀 Automatización de Pruebas de Login en OrangeHRM Demo

El inicio de sesión es una funcionalidad **crítica en cualquier aplicación web**: si falla, los usuarios no pueden acceder al sistema.  
Este proyecto valida automáticamente el **inicio de sesión exitoso** en la plataforma **OrangeHRM Demo**, asegurando que el acceso al **Dashboard** funcione correctamente.  

---

## 🛠️ Herramientas usadas
- **Python 3.x** – Lenguaje principal  
- **Selenium WebDriver** – Automatización de navegadores  
- **Pytest** – Ejecución y reporte de pruebas  
- **WebDriver Manager** – Configuración automática del driver de Chrome  
- **Page Object Model (POM)** – Patrón de diseño para mantener el código limpio y escalable  

---

## 👩‍💻 Mi rol
- Diseñé y desarrollé los **scripts de prueba automatizados**.  
- Implementé el patrón **Page Object Model (POM)** para separar la lógica de páginas y pruebas.  
- Configuré la ejecución de tests con **Pytest**.  
- Documenté el proyecto con instrucciones claras en este **README.md**.  

---

## 📂 Estructura del proyecto
```bash
PythonProject1/
│
├─ pages/
│   ├─ login_page.py          # Clase LoginPage
│   └─ dashboard_page.py      # Clase DashboardPage
│
├─ tests/
│   └─ tests_login.py         # Test de login
│
├─ requirements.txt           # Librerías necesarias
└─ README.md                  # Documentación

