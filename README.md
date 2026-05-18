# Sistema-Power-Bank
## Descripción
El Sistema de Préstamos de Power Banks es una aplicación desarrollada en Python orientada a la administración y control del préstamo de baterías portátiles en instituciones educativas, espacios públicos o centros de estudio.
<br>
El sistema permite gestionar usuarios, controlar préstamos y devoluciones, verificar disponibilidad de dispositivos y aplicar multas por retrasos, brindando una solución organizada y eficiente para mantener la disponibilidad de los power banks.
<br>
El proyecto fue desarrollado aplicando buenas prácticas de programación, arquitectura MVC, principios SOLID y persistencia de datos mediante archivos JSON.
<br><br>

## Estructura del Sistema

```plaintext
SistemaPowerBank/
│
├── .venv/
│
├── data/
│   ├── usuarios.json
│   ├── powerbanks.json
│   └── prestamos.json
│
├── docs/
│   └── Entregable 1 - Adelanto.pdf
│
├── src/
│   └── ucr/
│       └── ac/
│           └── cr/
│               │
│               ├── controller/
│               │   └── sistema_controller.py
│               │
│               ├── model/
│               │   ├── usuario.py
│               │   ├── powerbank.py
│               │   └── prestamo.py
│               │
│               ├── repository/
│               │   ├── base_repository.py
│               │   ├── usuario_repository.py
│               │   ├── powerbank_repository.py
│               │   └── prestamo_repository.py
│               │
│               ├── service/
│               │   ├── __init__.py
│               │   ├── usuario_service.py
│               │   ├── powerbank_service.py
│               │   └── prestamo_service.py
│               │
│               ├── view/
│               │   ├── __init__.py
│               │   ├── ventana_admin.py
│               │   ├── ventana_login.py
│               │   ├── ventana_powerbank.py
│               │   ├── ventana_prestamo.py
│               │   ├── ventana_principal.py
│               │   ├── ventana_reporte_prestamos.py
│               │   ├── ventana_reportes.py
│               │   └── ventana_usuario.py
│               │
│               └── main.py
│
├── .gitignore
└── README.md
```
<br><br>
## Principios SOLID Aplicados

### S — Single Responsibility Principle (SRP)

Cada clase tiene una única responsabilidad dentro del sistema.

#### Ejemplos:
- Usuario: representa únicamente la información de los usuarios.
- UsuarioRepository: administra el almacenamiento y lectura de usuarios.
- UsuarioService: contiene la lógica de negocio relacionada con usuarios.
- VentanaUsuario: maneja únicamente la interfaz gráfica de usuarios.

### O — Open/Closed Principle (OCP)

El sistema permite agregar nuevas funcionalidades sin modificar la estructura principal existente.

#### Ejemplos:
- Se implementó el módulo de login sin modificar los modelos principales.
- Se agregó la funcionalidad de eliminación de usuarios desde la capa de servicios y controladores.
- Se añadió la eliminación de power banks manteniendo la arquitectura por capas.
- Se pueden crear nuevos reportes agregando métodos en servicios y vistas.

### L — Liskov Substitution Principle (LSP)

Las clases derivadas pueden reemplazar a su clase base sin afectar el funcionamiento del sistema.

#### Ejemplos:
- UsuarioRepository: reutiliza los métodos de lectura y guardado de datos.
- PowerBankRepository: utiliza la misma estructura de persistencia.
- PrestamoRepository: reutiliza la lectura y escritura de archivos JSON.
- Todos los repositorios mantienen el comportamiento esperado de BaseRepository.


### I — Interface Segregation Principle (ISP)

Cada módulo utiliza únicamente las funcionalidades que necesita.

#### Ejemplos:
- Las vistas no manejan directamente archivos JSON.
- Los repositorios no contienen lógica gráfica ni ventanas.
- Los servicios no crean componentes visuales.
- Los controladores únicamente comunican las vistas con los servicios.


### D — Dependency Inversion Principle (DIP)

Las capas superiores dependen de abstracciones y no directamente de implementaciones concretas.

#### Ejemplos:
- Las vistas interactúan con SistemaController.
- El controlador se comunica con los servicios.
- Los servicios utilizan los repositorios.
- La interfaz gráfica no depende directamente de los archivos JSON.
<br><br>
## Instrucciones de Uso

### 1. Ejecutar el sistema

Ejecutar el archivo principal del proyecto:


python src/ucr/ac/cr/main.py


---

### 2. Inicio del sistema

Al iniciar el programa, se muestra la ventana de login.

Si el usuario no tiene una cuenta registrada, debe seleccionar la opción de registro.

---

### 3. Registro de usuarios

Para registrarse, el usuario debe ingresar:

- ID
- Nombre
- Correo
- Teléfono
- Contraseña

Después del registro, el usuario puede iniciar sesión utilizando su correo y contraseña.

---

### 4. Funciones del usuario normal

Al iniciar sesión como usuario normal, el sistema muestra las siguientes opciones:

- Préstamos y devoluciones
- Reportes
- Salir

---

### 5. Préstamos y devoluciones

En esta sección el usuario puede:

- Realizar préstamos ingresando el ID del préstamo y el ID del Power Bank.
- Realizar devoluciones ingresando el ID del préstamo.

Cuando un Power Bank es prestado, su estado cambia de:

Disponible -> Prestado


Cuando se realiza la devolución, el estado vuelve a:

Prestado -> Disponible


El sistema genera una multa automáticamente si la devolución se realiza luego se 2 horas del prestamo.
<br>La multa se genera a partir de las 2 horas luego del prestamo, se suma un monto de 500 colones por cada hora adicional que se exceda del limite.

---

### 6. Reportes para usuarios

El usuario normal puede:

- Ver los Power Banks registrados.
- Consultar su historial de préstamos.

---

### 7. Acceso como administrador

Para ingresar como administrador, se creó un usuario con rol `Admin` dentro del archivo `usuarios.json`:

```plaintext
[
    {
        "id_usuario": "1",
        "nombre": "Administrador",
        "correo": "admin@ucr.ac.cr",
        "telefono": "88888888",
        "password": "1234",
        "rol": "Admin"
    }
]
```

---

### 8. Funciones del administrador

Al iniciar sesión como administrador, se habilitan funciones adicionales:

- Registrar Power Banks.
- Eliminar Power Banks.
- Eliminar usuarios.
- Ver reportes generales.
- Consultar todos los usuarios registrados.
- Consultar todas las Power Banks registradas con su respectivo estado.
- Consultar todos los préstamos realizados.

---

### 9. Restricciones del sistema

Un Power Bank únicamente puede eliminarse si se encuentra en estado:

Disponible


Si el Power Bank se encuentra en estado:

Prestado


no podrá eliminarse hasta que sea devuelto.

---

### 10. Reinicio de datos

Para limpiar los datos almacenados del sistema, los archivos JSON pueden dejarse con listas vacías.

Ejemplo:
[]
