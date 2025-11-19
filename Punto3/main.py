from antlr4 import *
from MatrixLexer import MatrixLexer
from MatrixParser import MatrixParser
from MatrixEvalVisitor import EvalVisitor

def main():
    # Programa de prueba:
    code = """
    mat A[2,3] = [[1,2,3],[4,5,6]];
    mat B[3,2] = [[9,8],[7,6],[5,4]];
    mat C[2,2];
    C = A * B;
    print(C);
    """

    # Crear el input para ANTLR
    input_stream = InputStream(code)

    # Lexer y parser
    lexer = MatrixLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = MatrixParser(token_stream)

    # Regla inicial
    tree = parser.program()

    # Visitor que evalúa el programa
    visitor = EvalVisitor()
    visitor.visit(tree)

if __name__ == "__main__":
    main()
