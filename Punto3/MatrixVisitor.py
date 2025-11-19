# Generated from Matrix.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MatrixParser import MatrixParser
else:
    from MatrixParser import MatrixParser

# This class defines a complete generic visitor for a parse tree produced by MatrixParser.

class MatrixVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MatrixParser#program.
    def visitProgram(self, ctx:MatrixParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatrixParser#stmtList.
    def visitStmtList(self, ctx:MatrixParser.StmtListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatrixParser#stmt.
    def visitStmt(self, ctx:MatrixParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatrixParser#matrixDecl.
    def visitMatrixDecl(self, ctx:MatrixParser.MatrixDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatrixParser#dimension.
    def visitDimension(self, ctx:MatrixParser.DimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatrixParser#optInit.
    def visitOptInit(self, ctx:MatrixParser.OptInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatrixParser#assignStmt.
    def visitAssignStmt(self, ctx:MatrixParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatrixParser#printStmt.
    def visitPrintStmt(self, ctx:MatrixParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatrixParser#expr.
    def visitExpr(self, ctx:MatrixParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatrixParser#operand.
    def visitOperand(self, ctx:MatrixParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatrixParser#matrixLiteral.
    def visitMatrixLiteral(self, ctx:MatrixParser.MatrixLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MatrixParser#row.
    def visitRow(self, ctx:MatrixParser.RowContext):
        return self.visitChildren(ctx)



del MatrixParser