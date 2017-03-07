
import sympy
import Library_StringExpressionToSympyExpression
import Library_SympyExpressionToPythonFunction


def Main():

    ExpressionString = 'cos(x) + y + 4'

    ExpressionCasted = Library_StringExpressionToSympyExpression.Main(ExpressionString)

    ExpressionPythonFunction = Library_SympyExpressionToPythonFunction.Main(ExpressionCasted)

    Result =  ExpressionPythonFunction(0.0, 1.0) #Should give us 6
    print 'Result', Result
    assert(Result == 6)

    Result2 = ExpressionPythonFunction( y = 1.0, x = 0.0)
    print 'Result2', Result2
    assert(Result2 == 6)


    #`z` is added, Extra precision is also added
    ExpressionPythonFunctionExtraVariableNames = \
        Library_SympyExpressionToPythonFunction.Main(
            SympyExpression = ExpressionCasted,
            FloatPrecision = 100,
            NewSympyFunctionDefaults = {'x':0.0, 'y':1.0, 'z':2.0}, 
            )

    Result3 = ExpressionPythonFunctionExtraVariableNames(y = 1.0, x = 0.0, z = 2.0)
    print 'Result3', Result3
    assert(Result3 == 6)


    # `y` is not included:
    ExpressionPythonFunctionLessVariableNames = \
        Library_SympyExpressionToPythonFunction.Main(
            SympyExpression = ExpressionCasted,
            NewSympyFunctionDefaults = {'x':0.0}, 
            )
    Result4 = ExpressionPythonFunctionLessVariableNames(x = 0.0)
    print 'Result4', Result4



    
    #`y` is not included, and `z` is added:
    ExpressionPythonFunctionDifferentVariableName = \
        Library_SympyExpressionToPythonFunction.Main(
            SympyExpression = ExpressionCasted,
            NewSympyFunctionDefaults = {'x':0.0, 'z':2.0}, 
            )
    Result5 = ExpressionPythonFunctionDifferentVariableName(x = 0.0, z=2.0)
    print 'Result5', Result5


    ArgsPacked6 = {'x' : 0.0, 'z':2.0}
    Result6 = ExpressionPythonFunctionDifferentVariableName(**ArgsPacked6)
    print 'Result6', Result6


    #Do an expression which is just a constant
    print 'Creating Const Function...'
    ConstFunction = Library_SympyExpressionToPythonFunction.Main(
        SympyExpression = Library_StringExpressionToSympyExpression.Main('1234.5678'),
        NewSympyFunctionDefaults = {'x':0.0, 'z':2.0}, 
        )
    Result7 = ConstFunction()
    print 'Result7', Result7
    

    ThreeVarFunction = Library_SympyExpressionToPythonFunction.Main(
        SympyExpression = Library_StringExpressionToSympyExpression.Main('z**3 + x**2 + y**1'),
        NewSympyFunctionDefaults = { 'y': 0.0, 'z':0.0, 'x':0.0}, 
        )
    Result8 = ThreeVarFunction(x = 1,y = 2,z = 3)
    print 'Result8', Result8

    Result9 = ThreeVarFunction(1,2,3) #Variable names sorted alphebetically as function args
    print 'Result9', Result9

Main()














