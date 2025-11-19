# Matrix Language – Intérprete de Matrices con ANTLR4 y Python

Este proyecto implementa un **mini lenguaje para trabajar con matrices**, usando **ANTLR4** para generar el *lexer*, *parser* y *visitor*, mientras que Python ejecuta las instrucciones mediante un visitor personalizado (`MatrixEvalVisitor.py`).

El programa permite:

- Declarar matrices con dimensiones fijas  
- Inicializarlas mediante literales como `[[1,2,3],[4,5,6]]`
- Realizar multiplicación matricial `A * B`
- Asignar matrices
- Imprimir matrices con `print(X)`

---

## 📌 Estructura del Proyecto

```
Parcial Final/
│── main.py
│── Matrix.g4
│── MatrixLexer.py           # Generado por ANTLR
│── MatrixParser.py          # Generado por ANTLR
│── MatrixVisitor.py         # Generado por ANTLR
│── MatrixEvalVisitor.py
│── README.md
```

---

## ▶️ Ejecución del Programa

El archivo `main.py` contiene un programa de prueba:

```txt
mat A[2,3] = [[1,2,3],[4,5,6]];
mat B[3,2] = [[9,8],[7,6],[5,4]];
mat C[2,2];
C = A * B;
print(C);
```

Este programa:

1. Declara matrices A, B y C  
2. Multiplica `A * B`  
3. Guarda el resultado en C  
4. Imprime la matriz resultante  

---

## 🧮 Resultado Esperado

Multiplicando:

A (2×3) × B (3×2) da como resultado una matriz de 2×2:

```
C (2x2):
[ (1*9)+(2*7)+(3*5),  (1*8)+(2*6)+(3*4) ]
[ (4*9)+(5*7)+(6*5),  (4*8)+(5*6)+(6*4) ]
```

Evaluando:

- C[0][0] = 9 + 14 + 15 = **38**
- C[0][1] = 8 + 12 + 12 = **32**
- C[1][0] = 36 + 35 + 30 = **101**
- C[1][1] = 32 + 30 + 24 = **86**

Resultado final:

```
C (2x2):
[38, 32]
[101, 86]
```

---

## ⚙️ Compilación de la Gramática

Para generar el lexer, parser y visitor:

```bash
antlr4 -Dlanguage=Python3 -visitor Matrix.g4
```

---

## 📘 Descripción de Archivos

### 🔹 `Matrix.g4`
Define la gramática del lenguaje:
- Declaración de matrices (`mat`)
- Asignaciones
- Expresiones con multiplicación
- Literales de matriz `[ [1,2,3], [4,5,6] ]`
- Impresión

### 🔹 `MatrixEvalVisitor.py`
Implementa:
- Memoria de matrices
- Validación de dimensiones
- Multiplicación matricial
- Ejecución de sentencias
- Impresión formateada

### 🔹 `main.py`
Carga un programa como texto, lo parsea y ejecuta.

---

## 👨‍💻 Autor
Proyecto desarrollado por: **Julián David Briñez Sánchez**

Lenguajes de Programación – Universidad Sergio Arboleda  
