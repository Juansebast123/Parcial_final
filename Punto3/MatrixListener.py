# Generated from Matrix.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MatrixParser import MatrixParser
else:
    from MatrixParser import MatrixParser

# This class defines a complete listener for a parse tree produced by MatrixParser.
class MatrixListener(ParseTreeListener):

    # Enter a parse tree produced by MatrixParser#program.
    def enterProgram(self, ctx:MatrixParser.ProgramContext):
        pass

    # Exit a parse tree produced by MatrixParser#program.
    def exitProgram(self, ctx:MatrixParser.ProgramContext):
        pass


    # Enter a parse tree produced by MatrixParser#stmtList.
    def enterStmtList(self, ctx:MatrixParser.StmtListContext):
        pass

    # Exit a parse tree produced by MatrixParser#stmtList.
    def exitStmtList(self, ctx:MatrixParser.StmtListContext):
        pass


    # Enter a parse tree produced by MatrixParser#stmt.
    def enterStmt(self, ctx:MatrixParser.StmtContext):
        pass

    # Exit a parse tree produced by MatrixParser#stmt.
    def exitStmt(self, ctx:MatrixParser.StmtContext):
        pass


    # Enter a parse tree produced by MatrixParser#matrixDecl.
    def enterMatrixDecl(self, ctx:MatrixParser.MatrixDeclContext):
        pass

    # Exit a parse tree produced by MatrixParser#matrixDecl.
    def exitMatrixDecl(self, ctx:MatrixParser.MatrixDeclContext):
        pass


    # Enter a parse tree produced by MatrixParser#dimension.
    def enterDimension(self, ctx:MatrixParser.DimensionContext):
        pass

    # Exit a parse tree produced by MatrixParser#dimension.
    def exitDimension(self, ctx:MatrixParser.DimensionContext):
        pass


    # Enter a parse tree produced by MatrixParser#optInit.
    def enterOptInit(self, ctx:MatrixParser.OptInitContext):
        pass

    # Exit a parse tree produced by MatrixParser#optInit.
    def exitOptInit(self, ctx:MatrixParser.OptInitContext):
        pass


    # Enter a parse tree produced by MatrixParser#assignStmt.
    def enterAssignStmt(self, ctx:MatrixParser.AssignStmtContext):
        pass

    # Exit a parse tree produced by MatrixParser#assignStmt.
    def exitAssignStmt(self, ctx:MatrixParser.AssignStmtContext):
        pass


    # Enter a parse tree produced by MatrixParser#printStmt.
    def enterPrintStmt(self, ctx:MatrixParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by MatrixParser#printStmt.
    def exitPrintStmt(self, ctx:MatrixParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by MatrixParser#expr.
    def enterExpr(self, ctx:MatrixParser.ExprContext):
        pass

    # Exit a parse tree produced by MatrixParser#expr.
    def exitExpr(self, ctx:MatrixParser.ExprContext):
        pass


    # Enter a parse tree produced by MatrixParser#operand.
    def enterOperand(self, ctx:MatrixParser.OperandContext):
        pass

    # Exit a parse tree produced by MatrixParser#operand.
    def exitOperand(self, ctx:MatrixParser.OperandContext):
        pass


    # Enter a parse tree produced by MatrixParser#matrixLiteral.
    def enterMatrixLiteral(self, ctx:MatrixParser.MatrixLiteralContext):
        pass

    # Exit a parse tree produced by MatrixParser#matrixLiteral.
    def exitMatrixLiteral(self, ctx:MatrixParser.MatrixLiteralContext):
        pass


    # Enter a parse tree produced by MatrixParser#row.
    def enterRow(self, ctx:MatrixParser.RowContext):
        pass

    # Exit a parse tree produced by MatrixParser#row.
    def exitRow(self, ctx:MatrixParser.RowContext):
        pass



del MatrixParser