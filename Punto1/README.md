# CRUD Language -- Grammar & EDTS

**Lenguajes de Programación -- Procesadores de Lenguaje**

Este documento describe de manera clara y resumida la **gramática** y el
**Esquema de Traducción Dirigido por la Sintaxis (EDTS)** para un
lenguaje minimalista que implementa únicamente las operaciones **CRUD**:

-   **C** → Create\
-   **R** → Read\
-   **U** → Update\
-   **D** → Delete

El diseño sigue exactamente los principios vistos en clase,
especialmente los relacionados con: - manejo de ámbitos mediante
**`tsActual`** - gestión de pila de evaluación con **`sp`** y
**`maxstack`** - uso del atributo **`tipoFuncion`** para clasificar cada
sentencia

------------------------------------------------------------------------

## 📌 1. Objetivo del Lenguaje

El lenguaje ofrece soporte esencial para manipulación de datos. Las
operaciones permitidas son:

-   Crear tablas y declarar columnas\
-   Leer todos los registros de una tabla\
-   Actualizar un atributo de una tabla\
-   Borrar registros de una tabla

El enfoque es **didáctico**: se simplifica la sintaxis real de SQL para
poder modelarla con EDTS de forma clara y evaluable.

------------------------------------------------------------------------

## 🧩 2. Estructura General de la Gramática

El programa es una secuencia de sentencias CRUD:

    Programa → SentenciaLista
    SentenciaLista → Sentencia SentenciaLista | ε

Cada sentencia corresponde directamente a una de las cuatro operaciones
CRUD.

------------------------------------------------------------------------

## 🗂️ 3. Manejo de Ámbitos: `tsActual`

El EDTS utiliza una estructura de tabla de símbolos llamada
**`tsActual`**.\
Esta variable controla los **ámbitos**, igual que en el ejemplo de
funciones de la clase:

-   Al iniciar el programa → `tsActual = new TablaSimbolos(null)`
-   En `CREATE TABLE` → se abre un nuevo ámbito para registrar columnas
-   Al terminar la definición de la tabla → se cierra con
    `tsActual = tsActual.pop()`

Esto permite que: - Cada tabla tenga su propio "sub-ámbito" de columnas\
- Las demás sentencias validen nombres de tabla y columna correctamente

------------------------------------------------------------------------

## 🧮 4. Manejo de Pila: `sp` y `maxstack`

Siguiendo lo visto en generación de código intermedio:

-   Cada literal (`num`, `str`, `TRUE`, `FALSE`) simula un **`ldc`**,
    por lo tanto:
    -   `sp = sp + 1`
    -   se actualiza `maxstack` si es necesario

Aunque nuestro CRUD no tiene expresiones complejas, esto permite:

-   demostrar manejo de pila\
-   calcular un stack frame equivalente a IL\
-   mantener consistencia con la convención de evaluaciones vistas en
    clase

------------------------------------------------------------------------

## 🧪 5. Atributo Global: `tipoFuncion`

Cada sentencia produce un valor semántico global:

  Sentencia   tipoFuncion
  ----------- -------------
  Create      `void`
  Select      `resultset`
  Update      `int`
  Insert      `int`
  Delete      `int`

Esto sirve para integrar el CRUD en lenguajes más grandes con funciones
o módulos.

------------------------------------------------------------------------

## 🛠️ 6. Semántica Compacta por Operación

### ✔ **Create (C)**

Registra una tabla y sus columnas en `tsActual`.\
Abre y cierra ámbito.\
Genera código del tipo:

    CREATE TABLE nombre(col tipo, ...);

------------------------------------------------------------------------

### ✔ **Read (R)**

Verifica existencia de tabla.\
Genera:

    SELECT * FROM tabla;

------------------------------------------------------------------------

### ✔ **Update (U)**

Comprueba que: - exista la tabla\
- exista la columna\
- el tipo del nuevo valor coincida con el tipo declarado

Luego genera:

    UPDATE tabla SET columna = valor;

------------------------------------------------------------------------

### ✔ **Delete (D)**

Verifica que la tabla exista.\
Genera:

    DELETE FROM tabla;

------------------------------------------------------------------------

## 🔍 7. ¿Por qué esta gramática es ideal para un parcial?

-   Es **muy corta**\
-   Cumple con todos los elementos exigidos en clase:
    -   `tsActual` para ámbitos\
    -   `sp` y `maxstack` para pila\
    -   `tipoFuncion` para semántica de alto nivel\
-   Se parece al trabajo del corte anterior (coherencia)\
-   Fácil de sustentar oralmente

------------------------------------------------------------------------

## 🧠 8. Guion de Explicación Oral (30 segundos)

> "Mi lenguaje implementa las cuatro operaciones CRUD.\
> Manejo ámbitos con `tsActual`: al crear una tabla abro un nuevo ámbito
> para registrar columnas, y luego lo cierro con `pop()`.\
> Simulo la pila de evaluación usando `sp` y `maxstack` como en las
> expresiones del código intermedio.\
> Cada sentencia tiene un `tipoFuncion`: por ejemplo, SELECT devuelve un
> `resultset` y UPDATE devuelve un entero.\
> Con estas reglas el EDTS valida nombres, tipos y genera un código SQL
> equivalente."
