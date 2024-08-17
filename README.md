# Sistema de Gestión de Admisiones Escolares

Bienvenido al repositorio del **Sistema de Gestión de Admisiones Escolares**, un proyecto desarrollado con el propósito de facilitar y automatizar el proceso de admisión en instituciones educativas brindando una solución tecnologica para la falta de gestión y eficiencia. Este sistema, construido con Django y MySQL, ofrece una solución integral para gestionar el proceso de admisiones, desde la verificación del estado de postulación hasta la confirmación de la matrícula, todo ello a través de una interfaz web intuitiva y segura.

## Descripción General

Este sistema ha sido diseñado para simplificar la interacción entre los postulantes y la institución educativa. Permite a los postulantes verificar su estado de admisión en tiempo real, realizar la confirmación de su matrícula o desistir del cupo asignado. Además, está optimizado para que el personal administrativo de la escuela pueda gestionar fácilmente los datos de los postulantes y mantener actualizada la información en la base de datos.

### Funcionalidades Principales

#### 1. **Interfaz de Usuario Intuitiva**

La interfaz web del sistema está diseñada pensando en la facilidad de uso para el postulante. A través de una página de inicio simplificada, los postulantes pueden ingresar su RUT (Número de Identificación Nacional) para verificar su estado de admisión. Dependiendo de su estado en la base de datos, recibirán un mensaje personalizado que les indicará si han sido admitidos, están en lista de espera, no han sido admitidos o si ya han desistido de su cupo.

- **Admitido**: El postulante puede proceder a confirmar su matrícula directamente desde la misma interfaz.
- **En Lista de Espera**: El postulante será notificado y podrá optar por mantenerse en la lista de espera o desistir.
- **No Admitido**: El sistema le informará que no ha sido seleccionado en esta ocasión.
- **Desistido**: Si el postulante ya ha desistido previamente, el sistema lo indicará.

#### 2. **Confirmación de Matrícula**

Una vez admitido, el postulante puede confirmar su matrícula de manera sencilla. Esta funcionalidad está implementada de manera que la información del postulante se actualice automáticamente en la base de datos, registrando la confirmación y asegurando que el cupo sea reservado. Esta confirmación se realiza con un solo clic, minimizando errores y facilitando el proceso tanto para el postulante como para la institución.

#### 3. **Mensajes Personalizados**

El sistema está configurado para mostrar mensajes personalizados basados en el estado de admisión del postulante. Esto se logra mediante consultas directas a la base de datos, que devuelven el estado actual del postulante y generan un mensaje acorde a su situación. Esta característica no solo mejora la experiencia del usuario, sino que también asegura que se comuniquen correctamente las decisiones de admisión.

#### 4. **Seguridad y Gestión de Sesiones**

La seguridad es una prioridad en el desarrollo de este sistema. Implemente un robusto sistema de gestión de sesiones que asegura que solo los usuarios autenticados puedan acceder a la información sensible. Además, se han adoptado medidas de protección contra ataques comunes como la inyección SQL y Cross-Site Scripting (XSS). Todo el tráfico de datos se maneja de forma segura para proteger la privacidad de los postulantes.

#### 5. **Carga Fácil de Datos desde Excel**

Para facilitar la gestión interna, desarrollé un script que permite al personal de la escuela cargar datos de postulantes desde archivos Excel (.xlsx) directamente a la base de datos con un solo clic. Esta funcionalidad utiliza la biblioteca Pandas para leer y procesar los datos, asegurando que la información se inserte correctamente en las tablas correspondientes. Esto ahorra tiempo y reduce la posibilidad de errores manuales en la entrada de datos.

### Tecnologías Utilizadas

- **Django**: Framework web que permite el desarrollo rápido y seguro de aplicaciones web con una estructura bien definida y escalable.
- **MySQL**: Sistema de gestión de bases de datos relacional que asegura la integridad y eficiencia en el almacenamiento y recuperación de datos.
- **HTML/CSS**: Para la construcción de la interfaz de usuario, con un diseño responsivo que se adapta a diferentes dispositivos.
- **JavaScript & jQuery**: Para la interacción dinámica y la mejora de la experiencia del usuario en la interfaz.
- **Pandas**: Biblioteca de Python utilizada para el manejo y procesamiento de datos, especialmente en la carga y manipulación de archivos Excel.


---

Este proyecto es mantenido por SSCC Manquehue, desarrollado por Vanesa Cid para la institución.
