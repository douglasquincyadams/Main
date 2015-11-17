"""
DESCRIPTION:
    Generates a polynomial of a speficied degree
    The result format is a list of python functions each of which is a term in the polynomial

ARGS:
    Degree
        Type:
            <type>
        Description:
            The number of terms in the polynomial
RETURNS:

    FunctionList

        Description:
            List of python functions, each of which is f(x) = x ^ n
                [
                function1(x) { return x^degree }	, 
                function2(x) { return x^(degree-1) }	, 
                .
                . 
                functionN(x) { return x^0 }		
                ]

"""

import numpy

def Main(
    Degree = None
    ):
    FunctionList = []
    #The exponents are count down to 0 from degree
    Exponents = list(reversed(range(Degree + 1))) 
    Exponents = numpy.array(Exponents)

    for Exponent in Exponents:
        #Create a lambda function for each exponent
        #TermFunction = lambda DataPoint, Exponent = Exponent: DataPoint**Exponent 

        def TermFunction( 
            DataPoint, 
            Exponent = Exponent 
            ): #The `Exponent = Exponent` makes an independent copy of the exponent with private scope to the function
            return DataPoint**Exponent 

        #Append the term of order Degree to the list of functions
        FunctionList.append( TermFunction )

    return FunctionList































