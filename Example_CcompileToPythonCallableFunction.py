import Library_CcompileToPythonCallableFunction



CfunctionHeader = "int Main( double x, double y);"
CfunctionSource = r"""
static int Main( double x, double y)
{
    /* some algorithm that is seriously faster in C than in Python */

    return 100*x + y;

}
"""
CfunctionName = 'Main'

ResultFunction = Library_CcompileToPythonCallableFunction.Main(
    CfunctionHeader= CfunctionHeader,
    CfunctionSource= CfunctionSource,
    CfunctionName   = CfunctionName,
    )

for x in range(3):
    for y in range(10):
        SinglePlugAndChugResult = ResultFunction(x, y)
        print SinglePlugAndChugResult



SympyCcode = "1.17647058823529*(-1.0L/3.0L*pow(-pow(x, 2) + 1, 1.0L/3.0L) + 1)*exp(4.70588235294118*I*M_PI*x)/sqrt(-pow(x, 2) + 1)"
#TODO -> FML:     
#    To read sympy source, need complex numbers standard library
#       http://stackoverflow.com/questions/6418807/how-to-work-with-complex-numbers-in-c
#   To include standard library -> cffi breaks... and #include<asdf.h> does NOT WORK

SympyCheader = "int Main(double x);"
SympyCsource =  r" static int Main( double x ) {"
SympyCsource += r"return " + SympyCcode +  ";"
SympyCsource += r"}" 

SympyResultFunction = Library_CcompileToPythonCallableFunction.Main(
    CfunctionHeader= SympyCheader,
    CfunctionSource= SympyCsource,
    )


print SympyResultFunction(.5)







































