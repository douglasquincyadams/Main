import Library_StringFileNameLastExtension


expected_result = "txt"
result = Library_StringFileNameLastExtension.Main("hello.txt.txt")

print "expected_result: ", expected_result
print "result:          ", result

assert( expected_result == result )

result2 = Library_StringFileNameLastExtension.Main("hello")
print 'result2          ', result2
assert( result2 is None)

result3 = Library_StringFileNameLastExtension.Main("hello.txt.bfe")
print 'result3          ', result3
assert( result3 == 'bfe')

print "\nFull Test Success\n"




