

import Library_ArrayOfStringsStripTrailingWhiteSpace



array = ['a       ', ' b    ', 'c   ']
expected_result = ['a', ' b', 'c']

result = Library_ArrayOfStringsStripTrailingWhiteSpace.Main(array)

print "result" , result
print "expected_result", expected_result

if result == expected_result:
    print "Test Success"
else:
    print "Test Fail"

