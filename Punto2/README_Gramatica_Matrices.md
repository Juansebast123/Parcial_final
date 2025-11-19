# Gramática del Lenguaje de Matrices

Este documento describe formalmente la gramática del lenguaje diseñado para **declarar, inicializar, operar y mostrar matrices**.  
El lenguaje permite la declaración de matrices, su inicialización mediante literales, operaciones como la multiplicación de matrices y la impresión.

---

## 📌 Descripción General

El lenguaje soporta:

- Declaración de matrices (`mat A[2,3]`)
- Inicialización opcional (`=[[1,2,3],[4,5,6]]`)
- Asignaciones (`C = A * B`)
- Impresión (`print(C)`)
- Multiplicación de matrices
- Literales en forma de lista de filas

---

# 📚 Gramática Completa (BNF)

## Programa

```
Programa → SentenciaLista EOF
```

---

## Lista de Sentencias

```
SentenciaLista → Sentencia ';' SentenciaLista
               | ε
```

---

## Sentencia

```
Sentencia → DeclMatriz
          | AsigMatriz
          | Print
```

---

## Declaración de Matriz

```
DeclMatriz → 'mat' id Dimension OptInit
```

---

## Dimensión

```
Dimension → '[' num ',' num ']'
```

---

## Inicialización Opcional

```
OptInit → '=' MatLiteral
        | ε
```

---

## Asignación

```
AsigMatriz → id '=' Expresion
```

---

## Impresión

```
Print → 'print' '(' id ')'
```

---

## Expresión

```
Expresion → Operando '*' Operando
```

---

## Operando

```
Operando → id
         | MatLiteral
```

---

## Literal de Matriz

```
MatLiteral → '[[' FilaLista ']]'
```

---

## Lista de Filas

```
FilaLista → Fila RestoFilas
```

---

## Resto de Filas

```
RestoFilas → ',' Fila RestoFilas
           | ε
```

---

## Fila

```
Fila → num RestoNums
```

---

## Resto de Números

```
RestoNums → ',' num RestoNums
          | ε
```

---

# 📌 Ejemplo Completo

```
mat A[2,3] = [[1,2,3],[4,5,6]];
mat B[3,2] = [[9,8],[7,6],[5,4]];
mat C[2,2];
C = A * B;
print(C);
```

---

# 🧠 Resumen

La gramática permite construir un lenguaje sencillo pero potente para manipulación de matrices.  
Está diseñada para ser implementada en ANTLR mediante un Visitor que ejecute las operaciones correspondientes.

