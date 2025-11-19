# GenerarGramaticaCRUD

Este documento describe la función `GenerarGramaticaCRUD`, la cual construye de manera dinámica una gramática libre de contexto orientada a operaciones tipo SQL (CRUD).  
La función permite activar o desactivar producciones dependiendo de las operaciones permitidas, los tipos de datos soportados y si la Primary Key está habilitada o no.

---

## 📌 Descripción General

La función recibe tres parámetros:

- **operacionesCRUD**: lista con las operaciones soportadas.  
  Ejemplo: `["CREATE", "INSERT", "SELECT", "UPDATE", "DELETE"]`

- **tiposSoportados**: lista de tipos de datos válidos para las columnas.  
  Ejemplo: `["INT", "FLOAT", "TEXT"]`

- **soportaPK**: boolean que indica si la gramática debe incluir la producción para `PRIMARY KEY`.

La función genera una estructura `Gramatica` donde se agregan producciones dependiendo de los parámetros.

---

## 📌 Producciones Generadas

### 1. Regla Inicial
```
Programa → SentenciaLista
```

### 2. Sentencias Generales
```
SentenciaLista → Sentencia SentenciaLista
SentenciaLista → ε
```

---

## 📌 CRUD

### 🔨 CREATE  
Si `"CREATE"` está habilitado:

```
Sentencia → CreateTable ';'
CreateTable → 'CREATE' 'TABLE' id '(' DefCampoLista OptPK ')'
DefCampoLista → DefCampo RestCampos
RestCampos → ',' DefCampo RestCampos
RestCampos → ε
DefCampo → id Tipo
OptPK → ',' 'PRIMARY' 'KEY' '(' id ')'
OptPK → ε
```

---

### 🧩 INSERT  
Si `"INSERT"` está habilitado:

```
Sentencia → Insert ';'
Insert → 'INSERT' 'INTO' id 'VALUES' '(' Valor ')'
```

---

### 🔍 SELECT  
Si `"SELECT"` está habilitado:

```
Sentencia → Select ';'
Select → 'SELECT' '*' 'FROM' id
```

---

### ✏️ UPDATE  
Si `"UPDATE"` está habilitado:

```
Sentencia → Update ';'
Update → 'UPDATE' id 'SET' id2 '=' Valor
```

---

### 🗑️ DELETE  
Si `"DELETE"` está habilitado:

```
Sentencia → Delete ';'
Delete → 'DELETE' 'FROM' id
```

---

## 📌 Tipos Soportados

Por cada tipo presente:

```
Tipo → 'TIPO'
```

Ejemplo:
```
Tipo → 'INT'
Tipo → 'FLOAT'
Tipo → 'TEXT'
```

---

## 📌 Valores

```
Valor → num
Valor → str
Valor → 'TRUE'
Valor → 'FALSE'
```

---

## 📌 Retorno

La función retorna la estructura completa `Gramatica` construida con todas las producciones activadas.

---

## ✔️ Uso

Ejemplo:

```
gram = GenerarGramaticaCRUD(
    ["CREATE", "INSERT", "SELECT"],
    ["INT", "TEXT"],
    soportaPK = verdadero
)
```

---

## Autor
Generado automáticamente como documentación del proyecto.
