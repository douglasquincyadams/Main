"""
SOURCE:
    Mind of Douglas Adams
DESCRIPTION:
    Creates a sympy expression 
    WHICH IS an approximation 
    to an arbitrary function
    on an arbitrary domain. 
ARGS:
    CheckArguments
        Type:
            python boolean
        Description:
            if true, checks the arguments with conditions written in the function
            if false, ignores those conditions
    PrintExtra
        Type:
            python integer
        Description:
            if greater than 0, prints addional information about the function
            if 0, function is expected to print nothing to console
            Additional Notes:
                The greater the number, the more output the function will print
                Most functions only use 0 or 1, but some can print more depending on the number
    SympyExpression
        Type:
            <type 'NoneType'>
        Description:
    DomainMinimumPoint
        Type:
            <type 'NoneType'>
        Description:
    DomainMaximumPoint
        Type:
            <type 'NoneType'>
        Description:
    ApproximationOrder
        Type:
            <type 'NoneType'>
        Description:
RETURNS:
    Result
        Type:
        Description:
"""
import numpy
import sympy
#import sympy.mpmath
import pprint
import Library_SympyExpressionToPythonFunction
import Library_GenerateChebyShevPolynomial

# Generate Chebyshev polynomials T_n(ax+b) in expanded form
"""
def chebT(ctx, a=1, b=0):
    Tb = [1]
    yield Tb
    Ta = [b, a]
    while 1:
        yield Ta
        # Recurrence: T[n+1](ax+b) = 2*(ax+b)*T[n](ax+b) - T[n-1](ax+b)
        Tmp = [0] + [2*a*t for t in Ta]
        for i, c in enumerate(Ta): Tmp[i] += 2*b*c
        for i, c in enumerate(Tb): Tmp[i] -= c
        Ta, Tb = Tmp, Ta
"""

def Main(
    SympyExpression= None,
    ApproximationSymbol = None,
    DomainMinimumPoint= None,
    DomainMaximumPoint= None,
    ApproximationOrder= None,
    CheckArguments = True,
    PrintExtra = False,
    ):

    Result = None

    if (CheckArguments):
        ArgumentErrorMessage = ""

        if (len(ArgumentErrorMessage) > 0 ):
            if(PrintExtra):
                print "ArgumentErrorMessage:\n", ArgumentErrorMessage
            raise Exception(ArgumentErrorMessage)

    #Tsymb = sympy.Symbol('t')

    DomainStart = DomainMinimumPoint[0]
    print 'DomainStart', DomainStart
    DomainEnd = DomainMaximumPoint[0]
    print 'DomainEnd', DomainEnd

    #Transform the coefficients and the result to be on arbitrary inverval instead of from 0 to 1
    DomainWidth = DomainEnd - DomainStart
    DomainCenter = (DomainEnd - DomainStart) / 2.
    t = (ApproximationSymbol*(DomainWidth) + DomainStart + DomainEnd) / 2.
    x = (2.*ApproximationSymbol - DomainStart - DomainEnd) / (DomainWidth)
    SympyExpression = SympyExpression.subs(ApproximationSymbol, t)

    #GET THE COEFFICIENTS:
    Coefficients = []
    for CoefficientNumber in range(ApproximationOrder):
        if(PrintExtra): print 'CoefficientNumber', CoefficientNumber

        Coefficient = 0.0
        for k in range(1, ApproximationOrder + 1):
            if(PrintExtra): print '  k', k

            CoefficientFunctionPart = SympyExpression.subs(ApproximationSymbol, sympy.cos( sympy.pi*( float(k) - .5 )/ float(ApproximationOrder) )  )
            if(PrintExtra): print '  CoefficientFunctionPart', CoefficientFunctionPart

            CeofficientCosArg = float(CoefficientNumber)*( float(k) - .5 )/ float( ApproximationOrder)
            if(PrintExtra): print '  ',CoefficientNumber,'*','(',k,'-.5)/(', ApproximationOrder ,') == ', CeofficientCosArg

            CoefficientCosPart      =   sympy.cos( sympy.pi*CeofficientCosArg )
            if(PrintExtra): print '  CoefficientCosPart', CoefficientCosPart

            Coefficient += CoefficientFunctionPart*CoefficientCosPart
        
        if(PrintExtra): print 'Coefficient==', Coefficient

        Coefficient = (2./ApproximationOrder)*Coefficient.evalf(10)

        if(PrintExtra): print 'Coefficient==', Coefficient

        Coefficients.append(Coefficient)

    print '\n\nCoefficients'
    pprint.pprint( Coefficients )

    
    #GET THE POLYNOMIALS:
    ChebyShevPolynomials = Library_GenerateChebyShevPolynomial.Main(
        ApproximationSymbol = ApproximationSymbol,
        ResultType = 'sympy',
        Kind= 1,
        Order= ApproximationOrder-1,
        ReturnAll = True,
        )
    
    print '\nChebyShevPolynomials'
    pprint.pprint( ChebyShevPolynomials )


    Result = 0.0 -.5*(Coefficients[0])
    for Coefficient, ChebyShevPolynomial in zip(Coefficients, ChebyShevPolynomials):
        Result += Coefficient*ChebyShevPolynomial

    #Transform the coefficients and the result to be on arbitrary inverval instead of from 0 to 1
    Result = Result.subs(ApproximationSymbol, x)

    return Result

























