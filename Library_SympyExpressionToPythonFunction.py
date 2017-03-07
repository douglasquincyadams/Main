"""
SOURCE:
    Get list of VariableNames:
    http://stackoverflow.com/questions/30018977/how-can-i-get-a-list-of-the-symbols-in-a-sympy-expression

    Convert string into runable C-code
    https://github.com/neurophysik/jitcode/blob/master/jitcode/_jitcode.py
    http://stackoverflow.com/questions/42426967/create-usable-python-function-from-a-c-string-sympy-use-case

DESCRIPTION:

    Takes a sympy expression, and then turns it into a python callable function
    This is useful for when you have a function which is represented in the sympy notation for variaous manipulation,
    And then you want to run python things on it.
    I.E. you want to graph many values of it with matplotlib, or cram in many values with numpy

ARGS:
    SympyExpression
        Type:
            <type 'sympy.expr'>
        Description:
            Can have any number of free floating VariableNames
            e.g.    x + y  + z

    NewSympyFunctionDefaults
        Type: 
            <type 'dict'>
        Description:
            Has any subset of the Sympy Expressions Fre floating variables

    ReturnNative

        Type: 
            <type 'bool'>
        Description:
            The returned function takes math numbers as arguments and returns math numbers as results
            Should those number reuslts be cast back to native python complex values?
            ORRRR shoul dthose number results remain in sympy format?
            
            ReturnNative ==True -> returns complex math numbers which are readable by python

    FunctionConstructionMethod

RETURNS:

    PythonFunction
        Description:
            Python understood function which then expects all the free floating VariableNames as input
            e.g. 
                def PythonFunction( 
                    x, y, z 
                    ):
                    return expression(x=x, y=y, z=z)

            

        Type:
]           Python Lambda

"""
import copy
import inspect
import sympy
import sympy.printing
import sympy.utilities
import numpy
import scipy
import cffi
import Library_CopyFunction

def Main(
    SympyExpression = None,
    NewSympyFunctionDefaults = None,
    FloatPrecision = None,
    FunctionConstructionMethod = None, #TODO -> more!
    ReturnNative = False,
    PrintExtra = False,
    ):

    if FunctionConstructionMethod is None:
        FunctionConstructionMethod = 'evalf'


    VariableNames = None
    #Figure out the sympy function defaults:
    VariableNameCount = 0
    VariableSymbols = SympyExpression.free_symbols
    if (NewSympyFunctionDefaults is None):

        #Get the VariableNames from the sympy expression:
        VariableNames = sorted([str(var) for var in SympyExpression.free_symbols])
        VariableNameCount = len(VariableNames)
        if (PrintExtra):
            print 'VariableNameCount', VariableNameCount
            print 'VariableNames'
            print VariableNames
            
        #We copy the function with a set of None defaults using detected free parameters, 
        #   so that we have named VariableNames...    
        NewSympyFunctionDefaults = dict()
        for Variable in VariableNames:
            VariableName = str(Variable)
            if (PrintExtra):
                print 'VariableName'
                print VariableName
            NewSympyFunctionDefaults[VariableName] = 0

    else:
        VariableNames = sorted(NewSympyFunctionDefaults.keys())
        VariableNameCount = len(VariableNames)

    if (PrintExtra):
        print 'NewSympyFunctionDefaults'
        print NewSympyFunctionDefaults
    #print 'FloatPrecision', FloatPrecision
    if (PrintExtra): print 'VariableNames', VariableNames

    #Cast the expression into a python function:
    PythonFunction = None
    if (FunctionConstructionMethod == 'lambdify'): 


        LambdifyFunction = sympy.utilities.lambdify.lambdify(VariableSymbols, SympyExpression)

        def PythonFunction( 
            *args, 
            **kwargs  
            ):
            Result = LambdifyFunction()
            return Result

        raise Exception('TODO')
    elif (FunctionConstructionMethod == 'ccode'): 
        #TODO See -> jitcode
        ExpressionCCode = sympy.printing.ccode(SympyExpression)
        #many options here... they are all bad
        print 'ExpressionCCode'
        print ExpressionCCode
    
        raise Exception('TODO')
    elif (FunctionConstructionMethod == 'evalf'): 
        def PythonFunction( 
            *args, 
            **kwargs  
            ):

            if (PrintExtra): print 'args', args
            if (PrintExtra): print 'kwargs', kwargs
            ArgsCount = len(args)
            KwargsCount = len(kwargs)

            FunctionValueAssignments = copy.deepcopy(NewSympyFunctionDefaults)
            for VariableName, VariableNumber in zip(VariableNames, range(VariableNameCount)):
                VariableValue = None
                if (VariableNumber < ArgsCount):
                    VariableValue = args[VariableNumber]
                elif(VariableNumber < KwargsCount):
                    VariableValue = kwargs[VariableName]
                if (PrintExtra): print '---VariableValue', VariableValue
                FunctionValueAssignments[VariableName] = VariableValue

            if (PrintExtra): print 'FunctionValueAssignments', FunctionValueAssignments

            FunctionSymbolValueAssignments = {}
            for VariableName, VariableValue in FunctionValueAssignments.iteritems():
                FunctionSymbolValueAssignments[sympy.Symbol(VariableName) ] = VariableValue

            ReturnValue = SympyExpression.evalf(
                FloatPrecision, 
                subs=FunctionSymbolValueAssignments
                ) #Evalf is really slow...

            if (ReturnNative):
                ReturnValue = complex(ReturnValue)

            return ReturnValue

    return PythonFunction






    #Why didn't I make a deep copy? (of the returned function)
    #   seems logical to make a deep copy 
    #   to allow for passing around the function as an argrument 
    #   and allow for parallelism
    # --> figureed out why 2016_05_31 -> 
    #   Because you can always make a deep copy after calling this method, 
    #   and the overhead is slower
    """
    #Make a copy of the new python function with new defaults:
    PythonFunctionNamedArgs = Library_CopyFunction.Main( 
        Function = PythonFunction, 
        NewName = 'SympyFunctionNamedArgs',
        NewDefaults = NewSympyFunctionDefaults ,
        PrintExtra = PrintExtra,
        )
    return PythonFunctionNamedArgs
    """


















