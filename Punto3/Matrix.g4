grammar Matrix;

// Reglas del parser

program
    : stmtList EOF
    ;

// lista de sentencias, con ';' opcional al final
stmtList
    : stmt (';' stmt)* ';'?
    ;

stmt
    : matrixDecl
    | assignStmt
    | printStmt
    ;

// Declaración de matrices: mat A[2,3] = [[1,2,3],[4,5,6]]
matrixDecl
    : 'mat' ID dimension optInit
    ;

dimension
    : '[' INT ',' INT ']'
    ;

// optInit puede estar vacio o tener un literal de matriz
optInit
    : '=' matrixLiteral
    |
    ;

// Asignación: C = A * B;
assignStmt
    : ID '=' expr
    ;

// print(C);
printStmt
    : 'print' '(' ID ')'
    ;

// Expresion: producto de dos operandos
expr
    : operand '*' operand
    ;

// Operando: una variable o un literal de matriz
operand
    : ID
    | matrixLiteral
    ;

// Literal de matriz: [[1,2,3],[4,5,6]]
//  -> corchete exterior para la matriz, corchetes interiores para cada fila
matrixLiteral
    : '[' row (',' row)* ']'
    ;

// Fila: [1,2,3]
row
    : '[' INT (',' INT)* ']'
    ;

// ----------------------
// Tokens (lexer rules)
// ----------------------

ID      : [a-zA-Z_] [a-zA-Z_0-9]* ;

INT     : [0-9]+ ;

WS      : [ \t\r\n]+ -> skip ;

COMMENT : '//' ~[\r\n]* -> skip ;
