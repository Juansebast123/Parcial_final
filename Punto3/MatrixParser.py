# Generated from Matrix.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,14,99,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,0,1,1,1,
        1,1,1,5,1,31,8,1,10,1,12,1,34,9,1,1,1,3,1,37,8,1,1,2,1,2,1,2,3,2,
        42,8,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,3,
        5,58,8,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,9,
        1,9,3,9,75,8,9,1,10,1,10,1,10,1,10,5,10,81,8,10,10,10,12,10,84,9,
        10,1,10,1,10,1,11,1,11,1,11,1,11,5,11,92,8,11,10,11,12,11,95,9,11,
        1,11,1,11,1,11,0,0,12,0,2,4,6,8,10,12,14,16,18,20,22,0,0,94,0,24,
        1,0,0,0,2,27,1,0,0,0,4,41,1,0,0,0,6,43,1,0,0,0,8,48,1,0,0,0,10,57,
        1,0,0,0,12,59,1,0,0,0,14,63,1,0,0,0,16,68,1,0,0,0,18,74,1,0,0,0,
        20,76,1,0,0,0,22,87,1,0,0,0,24,25,3,2,1,0,25,26,5,0,0,1,26,1,1,0,
        0,0,27,32,3,4,2,0,28,29,5,1,0,0,29,31,3,4,2,0,30,28,1,0,0,0,31,34,
        1,0,0,0,32,30,1,0,0,0,32,33,1,0,0,0,33,36,1,0,0,0,34,32,1,0,0,0,
        35,37,5,1,0,0,36,35,1,0,0,0,36,37,1,0,0,0,37,3,1,0,0,0,38,42,3,6,
        3,0,39,42,3,12,6,0,40,42,3,14,7,0,41,38,1,0,0,0,41,39,1,0,0,0,41,
        40,1,0,0,0,42,5,1,0,0,0,43,44,5,2,0,0,44,45,5,11,0,0,45,46,3,8,4,
        0,46,47,3,10,5,0,47,7,1,0,0,0,48,49,5,3,0,0,49,50,5,12,0,0,50,51,
        5,4,0,0,51,52,5,12,0,0,52,53,5,5,0,0,53,9,1,0,0,0,54,55,5,6,0,0,
        55,58,3,20,10,0,56,58,1,0,0,0,57,54,1,0,0,0,57,56,1,0,0,0,58,11,
        1,0,0,0,59,60,5,11,0,0,60,61,5,6,0,0,61,62,3,16,8,0,62,13,1,0,0,
        0,63,64,5,7,0,0,64,65,5,8,0,0,65,66,5,11,0,0,66,67,5,9,0,0,67,15,
        1,0,0,0,68,69,3,18,9,0,69,70,5,10,0,0,70,71,3,18,9,0,71,17,1,0,0,
        0,72,75,5,11,0,0,73,75,3,20,10,0,74,72,1,0,0,0,74,73,1,0,0,0,75,
        19,1,0,0,0,76,77,5,3,0,0,77,82,3,22,11,0,78,79,5,4,0,0,79,81,3,22,
        11,0,80,78,1,0,0,0,81,84,1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,
        85,1,0,0,0,84,82,1,0,0,0,85,86,5,5,0,0,86,21,1,0,0,0,87,88,5,3,0,
        0,88,93,5,12,0,0,89,90,5,4,0,0,90,92,5,12,0,0,91,89,1,0,0,0,92,95,
        1,0,0,0,93,91,1,0,0,0,93,94,1,0,0,0,94,96,1,0,0,0,95,93,1,0,0,0,
        96,97,5,5,0,0,97,23,1,0,0,0,7,32,36,41,57,74,82,93
    ]

class MatrixParser ( Parser ):

    grammarFileName = "Matrix.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'mat'", "'['", "','", "']'", "'='", 
                     "'print'", "'('", "')'", "'*'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "INT", 
                      "WS", "COMMENT" ]

    RULE_program = 0
    RULE_stmtList = 1
    RULE_stmt = 2
    RULE_matrixDecl = 3
    RULE_dimension = 4
    RULE_optInit = 5
    RULE_assignStmt = 6
    RULE_printStmt = 7
    RULE_expr = 8
    RULE_operand = 9
    RULE_matrixLiteral = 10
    RULE_row = 11

    ruleNames =  [ "program", "stmtList", "stmt", "matrixDecl", "dimension", 
                   "optInit", "assignStmt", "printStmt", "expr", "operand", 
                   "matrixLiteral", "row" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    ID=11
    INT=12
    WS=13
    COMMENT=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmtList(self):
            return self.getTypedRuleContext(MatrixParser.StmtListContext,0)


        def EOF(self):
            return self.getToken(MatrixParser.EOF, 0)

        def getRuleIndex(self):
            return MatrixParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MatrixParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.stmtList()
            self.state = 25
            self.match(MatrixParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MatrixParser.StmtContext)
            else:
                return self.getTypedRuleContext(MatrixParser.StmtContext,i)


        def getRuleIndex(self):
            return MatrixParser.RULE_stmtList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmtList" ):
                listener.enterStmtList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmtList" ):
                listener.exitStmtList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtList" ):
                return visitor.visitStmtList(self)
            else:
                return visitor.visitChildren(self)




    def stmtList(self):

        localctx = MatrixParser.StmtListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmtList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.stmt()
            self.state = 32
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 28
                    self.match(MatrixParser.T__0)
                    self.state = 29
                    self.stmt() 
                self.state = 34
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 35
                self.match(MatrixParser.T__0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def matrixDecl(self):
            return self.getTypedRuleContext(MatrixParser.MatrixDeclContext,0)


        def assignStmt(self):
            return self.getTypedRuleContext(MatrixParser.AssignStmtContext,0)


        def printStmt(self):
            return self.getTypedRuleContext(MatrixParser.PrintStmtContext,0)


        def getRuleIndex(self):
            return MatrixParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MatrixParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stmt)
        try:
            self.state = 41
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.matrixDecl()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.assignStmt()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 40
                self.printStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatrixDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MatrixParser.ID, 0)

        def dimension(self):
            return self.getTypedRuleContext(MatrixParser.DimensionContext,0)


        def optInit(self):
            return self.getTypedRuleContext(MatrixParser.OptInitContext,0)


        def getRuleIndex(self):
            return MatrixParser.RULE_matrixDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatrixDecl" ):
                listener.enterMatrixDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatrixDecl" ):
                listener.exitMatrixDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatrixDecl" ):
                return visitor.visitMatrixDecl(self)
            else:
                return visitor.visitChildren(self)




    def matrixDecl(self):

        localctx = MatrixParser.MatrixDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_matrixDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(MatrixParser.T__1)
            self.state = 44
            self.match(MatrixParser.ID)
            self.state = 45
            self.dimension()
            self.state = 46
            self.optInit()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimensionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(MatrixParser.INT)
            else:
                return self.getToken(MatrixParser.INT, i)

        def getRuleIndex(self):
            return MatrixParser.RULE_dimension

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDimension" ):
                listener.enterDimension(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDimension" ):
                listener.exitDimension(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimension" ):
                return visitor.visitDimension(self)
            else:
                return visitor.visitChildren(self)




    def dimension(self):

        localctx = MatrixParser.DimensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_dimension)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(MatrixParser.T__2)
            self.state = 49
            self.match(MatrixParser.INT)
            self.state = 50
            self.match(MatrixParser.T__3)
            self.state = 51
            self.match(MatrixParser.INT)
            self.state = 52
            self.match(MatrixParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OptInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def matrixLiteral(self):
            return self.getTypedRuleContext(MatrixParser.MatrixLiteralContext,0)


        def getRuleIndex(self):
            return MatrixParser.RULE_optInit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOptInit" ):
                listener.enterOptInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOptInit" ):
                listener.exitOptInit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOptInit" ):
                return visitor.visitOptInit(self)
            else:
                return visitor.visitChildren(self)




    def optInit(self):

        localctx = MatrixParser.OptInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_optInit)
        try:
            self.state = 57
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.match(MatrixParser.T__5)
                self.state = 55
                self.matrixLiteral()
                pass
            elif token in [-1, 1]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MatrixParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(MatrixParser.ExprContext,0)


        def getRuleIndex(self):
            return MatrixParser.RULE_assignStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignStmt" ):
                listener.enterAssignStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignStmt" ):
                listener.exitAssignStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStmt" ):
                return visitor.visitAssignStmt(self)
            else:
                return visitor.visitChildren(self)




    def assignStmt(self):

        localctx = MatrixParser.AssignStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assignStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(MatrixParser.ID)
            self.state = 60
            self.match(MatrixParser.T__5)
            self.state = 61
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MatrixParser.ID, 0)

        def getRuleIndex(self):
            return MatrixParser.RULE_printStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStmt" ):
                listener.enterPrintStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStmt" ):
                listener.exitPrintStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStmt" ):
                return visitor.visitPrintStmt(self)
            else:
                return visitor.visitChildren(self)




    def printStmt(self):

        localctx = MatrixParser.PrintStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_printStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(MatrixParser.T__6)
            self.state = 64
            self.match(MatrixParser.T__7)
            self.state = 65
            self.match(MatrixParser.ID)
            self.state = 66
            self.match(MatrixParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MatrixParser.OperandContext)
            else:
                return self.getTypedRuleContext(MatrixParser.OperandContext,i)


        def getRuleIndex(self):
            return MatrixParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = MatrixParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.operand()
            self.state = 69
            self.match(MatrixParser.T__9)
            self.state = 70
            self.operand()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MatrixParser.ID, 0)

        def matrixLiteral(self):
            return self.getTypedRuleContext(MatrixParser.MatrixLiteralContext,0)


        def getRuleIndex(self):
            return MatrixParser.RULE_operand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperand" ):
                listener.enterOperand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperand" ):
                listener.exitOperand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = MatrixParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_operand)
        try:
            self.state = 74
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.match(MatrixParser.ID)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.matrixLiteral()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatrixLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def row(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MatrixParser.RowContext)
            else:
                return self.getTypedRuleContext(MatrixParser.RowContext,i)


        def getRuleIndex(self):
            return MatrixParser.RULE_matrixLiteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatrixLiteral" ):
                listener.enterMatrixLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatrixLiteral" ):
                listener.exitMatrixLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatrixLiteral" ):
                return visitor.visitMatrixLiteral(self)
            else:
                return visitor.visitChildren(self)




    def matrixLiteral(self):

        localctx = MatrixParser.MatrixLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_matrixLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(MatrixParser.T__2)
            self.state = 77
            self.row()
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 78
                self.match(MatrixParser.T__3)
                self.state = 79
                self.row()
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 85
            self.match(MatrixParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(MatrixParser.INT)
            else:
                return self.getToken(MatrixParser.INT, i)

        def getRuleIndex(self):
            return MatrixParser.RULE_row

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRow" ):
                listener.enterRow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRow" ):
                listener.exitRow(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRow" ):
                return visitor.visitRow(self)
            else:
                return visitor.visitChildren(self)




    def row(self):

        localctx = MatrixParser.RowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_row)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(MatrixParser.T__2)
            self.state = 88
            self.match(MatrixParser.INT)
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 89
                self.match(MatrixParser.T__3)
                self.state = 90
                self.match(MatrixParser.INT)
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 96
            self.match(MatrixParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





