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
├── src/
│   └── ucr/
│       └── ac/
│           └── cr/
│
│               ├── model/
│               │   ├── usuario.py
│               │   ├── powerbank.py
│               │   └── prestamo.py
│               │
│               ├── repository/
│               │   ├── usuario_repository.py
│               │   ├── powerbank_repository.py
│               │   └── prestamo_repository.py
│               │
│               ├── service/
│               │   ├── usuario_service.py
│               │   ├── prestamo_service.py
│               │   └── login_service.py
│               │
│               ├── controller/
│               │   ├── usuario_controller.py
│               │   ├── prestamo_controller.py
│               │   └── login_controller.py
│               │
│               ├── view/
│               │   ├── login_view.py
│               │   ├── menu_view.py
│               │   ├── usuario_view.py
│               │   ├── powerbank_view.py
│               │   ├── prestamo_view.py
│               │   └── reporte_view.py
│               │
│               ├── data/
│               │   ├── usuarios.json
│               │   ├── powerbanks.json
│               │   └── prestamos.json
│               │
│               └── main.py
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

## Instrucciones de uso
