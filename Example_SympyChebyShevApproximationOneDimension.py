import sympy
#import sympy.mpmath
import matplotlib.pyplot as plt
import json
import pprint

#------------------------------------------------------------------------------


import Library_GenerateBesselFunction
import Library_SympyChebyShevApproximationOneDimension
import Library_SympyExpressionToPythonFunction
import Library_GraphOneDimensionalFunction


ApproximationOrder = 10

#CREATE THE EXAMPLE EXRESSION:
Kind = 1
Order = 2
ExampleSympyExpression = sympy.sin(sympy.Symbol('x'))

"""
Library_GenerateBesselFunction.Main(
    ResultType =  'sympy',
    Kind =  Kind,
    Order =  Order,
    VariableNames = ['x'],
    ) 
"""
PythonOriginalFunction = Library_SympyExpressionToPythonFunction.Main( 
    ExampleSympyExpression ,
    FloatPrecision = 100,
    )

#CREATE THE NATIVE CHEBY APPROXIMATION

ChebyDomainMin = 5.
ChebyDomainMax = 10.
ChebyDomain = [ChebyDomainMin, ChebyDomainMax]
ChebyExpandedPolynomialCoefficients, ChebyError = sympy.mpmath.chebyfit(
    PythonOriginalFunction, 
    ChebyDomain, 
    ApproximationOrder, 
    error=True
    )
print 'ChebyExpandedPolynomialCoefficients'
pprint.pprint( ChebyExpandedPolynomialCoefficients )
def PythonChebyChevApproximation(Point):
    Result = sympy.mpmath.polyval(ChebyExpandedPolynomialCoefficients, Point)
    return Result


#CREATE THE GENERIC ONE DIMENSIONAL CHEBY APPROXIMATION:
SympyChebyApproximation = Library_SympyChebyShevApproximationOneDimension.Main(
    SympyExpression = ExampleSympyExpression*sympy.cos( sympy.Symbol('a') ),
    ApproximationSymbol = sympy.Symbol('x'),
    DomainMinimumPoint = [ChebyDomainMin],
    DomainMaximumPoint = [ChebyDomainMax],
    ApproximationOrder = ApproximationOrder
    )


print 'SympyChebyApproximation', SympyChebyApproximation
SympyChebyApproximation = SympyChebyApproximation.subs(sympy.Symbol('a'), 0.0)

print 'SympyChebyApproximation', SympyChebyApproximation
PythonCastedChebyChevApproximationGeneric = Library_SympyExpressionToPythonFunction.Main( 
    SympyChebyApproximation ,
    FloatPrecision = 100,
    )

print 'PythonCastedChebyChevApproximationGeneric(1)', PythonCastedChebyChevApproximationGeneric(1.)


#GRAPH THE ORINGINAL AND ALL THE APPROXIMATION FUNCTIONS

#size the graphs
#   Default to common monitor size:  
#   1920pixels by 1080 pixels
Inch_in_Pixels = 80.0
MonitorSize = (1920.0/Inch_in_Pixels, 1080.0/Inch_in_Pixels)


Figure = plt.figure(figsize=MonitorSize)
DomainMinimumPoint = 0
DomainMaximumPoint = 15
Library_GraphOneDimensionalFunction.Main(
    Functions = [
        PythonOriginalFunction, 
        #PythonChebyChevApproximation, 
        PythonCastedChebyChevApproximationGeneric,
        ],
    FunctionLabels = [
        'BesselFunction:' + json.dumps( {'Kind' : Kind, 'Order' : Order} ) , 
        #'ChebyChevApproximation: ' +  ',TermCount='  + str(ApproximationOrder)  + ',ChebyDomain=' +str(ChebyDomain) , 
        'PythonCastedChebyChevApproximationGeneric' +  ',TermCount='  + str(ApproximationOrder)  + ',ChebyDomain=' +str(ChebyDomain) ,
        ],
    DomainMinimumPoint = DomainMinimumPoint, 
    DomainMaximumPoint = DomainMaximumPoint, 
    MainFunctionIndex = 0,
    MainFunctionDifferenceRequirement = 1,
    )

plt.show(Figure)













































