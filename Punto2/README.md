El lenguaje soporta:

- Declaración de matrices (`mat A[2,3]`)
- Inicialización opcional (`=[[1,2,3],[4,5,6]]`)
- Asignaciones (`C = A * B`)
- Impresión (`print(C)`)
- Multiplicación de matrices
- Literales en forma de lista de filas

---

# Gramática Completa

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

## Dimension

```
Dimension → '[' num ',' num ']'
```

---

## Inicializacion

```
OptInit → '=' MatLiteral
        | ε
```

---

## Asignacion

```
AsigMatriz → id '=' Expresion
```

---

## Impresion

```
Print → 'print' '(' id ')'
```

---

## Expresion

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

# Ejemplo Completo

```
mat A[2,3] = [[1,2,3],[4,5,6]];
mat B[3,2] = [[9,8],[7,6],[5,4]];
mat C[2,2];
C = A * B;
print(C);
```

---


