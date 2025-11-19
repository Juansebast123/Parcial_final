from MatrixParser import MatrixParser
from MatrixVisitor import MatrixVisitor

class EvalVisitor(MatrixVisitor):
    def __init__(self):
        super().__init__()
        # memoria: nombre -> (filas, columnas, matriz(datos))
        self.mem = {}

    # program: stmtList EOF
    def visitProgram(self, ctx: MatrixParser.ProgramContext):
        return self.visit(ctx.stmtList())

    # stmtList: stmt (';' stmt)* ';'?
    def visitStmtList(self, ctx: MatrixParser.StmtListContext):
        for s in ctx.stmt():
            self.visit(s)
        return None

    def visitMatrixDecl(self, ctx: MatrixParser.MatrixDeclContext):
        name = ctx.ID().getText()

        dim_ctx = ctx.dimension()
        rows = int(dim_ctx.INT(0).getText())
        cols = int(dim_ctx.INT(1).getText())

        # matriz por defecto: ceros
        data = [[0 for _ in range(cols)] for _ in range(rows)]

        # si hay inicializacion con literal de matriz
        if ctx.optInit().matrixLiteral():
            data = self.visit(ctx.optInit().matrixLiteral())

        # (Opcional) validar que data sea rows x cols

        self.mem[name] = (rows, cols, data)
        return None

    # assignStmt: ID '=' expr
    def visitAssignStmt(self, ctx: MatrixParser.AssignStmtContext):
        name = ctx.ID().getText()
        result = self.visit(ctx.expr())

        if not result:
            raise Exception("La expresión no devolvió matriz")

        rows = len(result)
        cols = len(result[0]) if rows > 0 else 0

        self.mem[name] = (rows, cols, result)
        return None

    # printStmt: 'print' '(' ID ')'
    def visitPrintStmt(self, ctx: MatrixParser.PrintStmtContext):
        name = ctx.ID().getText()
        if name not in self.mem:
            raise Exception(f"Matriz no declarada: {name}")
        rows, cols, data = self.mem[name]
        print(f"{name} ({rows}x{cols}):")
        for r in data:
            print(r)
        return None

    # expr: operand '*' operand
    def visitExpr(self, ctx: MatrixParser.ExprContext):
        left = self.visit(ctx.operand(0))
        right = self.visit(ctx.operand(1))
        return self.matrix_mul(left, right)

    # operand: ID | matrixLiteral
    def visitOperand(self, ctx: MatrixParser.OperandContext):
        if ctx.ID():
            name = ctx.ID().getText()
            if name not in self.mem:
                raise Exception(f"Matriz no declarada: {name}")
            _, _, data = self.mem[name]
            return data
        else:
            return self.visit(ctx.matrixLiteral())

    # matrixLiteral: '[' row (',' row)* ']'
    def visitMatrixLiteral(self, ctx: MatrixParser.MatrixLiteralContext):
        filas = []
        for r in ctx.row():
            filas.append(self.visit(r))
        return filas

    # row: '[' INT (',' INT)* ']'
    def visitRow(self, ctx: MatrixParser.RowContext):
        return [int(tok.getText()) for tok in ctx.INT()]

    # -------- util: producto de matrices A (m x n) y B (n x p) --------
    def matrix_mul(self, A, B):
        m = len(A)
        n = len(A[0]) if m > 0 else 0
        n2 = len(B)
        p = len(B[0]) if n2 > 0 else 0

        if n != n2:
            raise Exception(f"Dimensiones incompatibles: {m}x{n} * {n2}x{p}")

        C = [[0 for _ in range(p)] for _ in range(m)]
        for i in range(m):
            for j in range(p):
                s = 0
                for k in range(n):
                    s += A[i][k] * B[k][j]
                C[i][j] = s
        return C
