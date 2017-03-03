"""
SOURCE:
    Mind of Douglas Adams
DESCRIPTION:
    Sorts a list of values by assuming 
        the final sort result 
        can be thought of as a function of indices
    The obvious thing to do first is assume that the results are linear:
        First find min, max, len, values in the list and fit a straight line from min to max:
            y = ( list_len / (max - min) )  x 
            Where y is the list values
            and   x is the list indices
            y(value) = index
            ----------------
            y(min)  = 0
            y(max)  = len - 1
            y(othervalue) = some fractional index -> which is rounded to the nearest 1
        Takes the mx + b fit, 
            and for each value -> 
            round to the nearest index
        Now -> you will have stuff more sorted that what you started with. 
        This first pass-> only takes n time. 
        You can then run the same sort on each group of items which had the same index
        The quickness of the algorithm depends on the closeness to linearity of the data.
        For a linear set of items - this sort would take only N time.    
    The better that your ogiginal guess is to the fit function:
        The faster the sort will be.
        Clearly if the items are all sampled from an exponetinal function:
        y(value) = exp(index)
        a linear fit -> won't work as well
        an exponential fit to the indices will work perfectly -> and again take n time
    The speed of the sort can be reduced to O(N) if you know how to represent all the values in the list
        as a function of indices
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
    List
        Type:
            <type 'NoneType'>
        Description:
RETURNS:
    Result
        Type:
        Description:
"""
#import Library_PrettyPrintNestedObject
def Main(
    List= None,
    #Function ?  FunctionName?   SympyFunctionExpression?   Variables?   Fit Algorithm...?
    CheckArguments = True,
    PrintExtra = False,
    ):

    Result = None

    DoLinear = True

    if (CheckArguments):
        ArgumentErrorMessage = ""

        if (len(ArgumentErrorMessage) > 0 ):
            if(PrintExtra):
                print "ArgumentErrorMessage:\n", ArgumentErrorMessage
            raise Exception(ArgumentErrorMessage)

    if PrintExtra:
        print '----Start Sort ---- '
        print  List
        print '.'
    #Get information which takes O(n) time or less:
    MaxElement = max(List)    
    MinElement = min(List)
    ListLength = len(List)
    RangeElements = (float(MaxElement) - float(MinElement))
    LinearSlope = (float(ListLength) - 1 ) /  RangeElements 


    #Create a helper function to remove none's from a list:
    def RemoveNones(List):
        List = [x for x in List if x != None]
        return List
    #Create an object to store out sorted result:
    SortedResult = [None]*ListLength


    if DoLinear:
        #Fit the indices to the values as though they were linear:
        #print 'LinearSlope', LinearSlope
        def FitFunction(Value):
            IndexApproximation = LinearSlope * float( Value ) - MinElement
            #print 'Value', Value,',IndexApproximation float' , IndexApproximation
            IndexApproximation = int(IndexApproximation)
            return str(IndexApproximation)

        IndexValueMap = {}

        for Element in List:
            ApproximateIndex = FitFunction(Element)
            #print  'Element: ', Element, ', ApproximateIndex: ', ApproximateIndex
            

            if not ( ApproximateIndex in IndexValueMap ):
                IndexValueMap[ApproximateIndex] = []

            #print IndexValueMap[ApproximateIndex]

            IndexValueMap[ApproximateIndex].append(Element)

        if PrintExtra:
            print 'IndexValueMap'
            #Library_PrettyPrintNestedObject.Main( IndexValueMap )
            print IndexValueMap

        #Assign all the non-coliding indexes into thte final result:
        ApproximateIndexShift = 0
        for ApproximateIndex, Grouping in IndexValueMap.iteritems():
            GroupInsertLocation = int(ApproximateIndex) + ApproximateIndexShift
            if len(Grouping) == 1:
                SortedResult[GroupInsertLocation] = Grouping[0]
            else:
                SortedGrouping = Main(Grouping)
                if PrintExtra: print 'SortedGrouping', SortedGrouping
                SortedResult[GroupInsertLocation:GroupInsertLocation ] = SortedGrouping
                ApproximateIndexShift += len(Grouping) - 1

        SortedResult = RemoveNones( SortedResult )




    if PrintExtra:
        print '.'
        print SortedResult
        print '--EndSort--'

    Result = SortedResult
    return Result 













