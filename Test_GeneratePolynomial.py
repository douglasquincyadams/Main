import Library_GeneratePolynomial


#Creates the terms with the highest degree first
PolynomialTerms = Library_GeneratePolynomial.Main(Degree = 3)

TestResult1 = ( PolynomialTerms[1](2) == 4)
print 'TestResult1', TestResult1

TestResult2 = ( PolynomialTerms[0](2) == 8)
print 'TestResult2', TestResult2
