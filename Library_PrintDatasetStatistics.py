"""
DESCRIPTION:
    Prints statistics about a numpy array

ARGS:
    Dataset:
        Type: `Type_NumpyOneDimensionalDataset` OR `Type_NumpyTwoDimensionalDataset`

RETURNS:
    None

"""
import numpy
import Library_DatasetGetMaximumDatapoint
import Library_DatasetGetMinimumDatapoint

def Main(                       
    Dataset = None,             
    PrintLineHeader = "",       
    PrintLineBufferSize = 0,    
    CheckArguments = True,
    PrintExtra = False
    ):

    #Obtain some information about the dataset which can be used for both:
    #   CheckArguments
    #   Printing
    DatasetShape = Dataset.shape
    DatasetShapeLength = len(DatasetShape)
    SpaceBuffer = " "*PrintLineBufferSize
    DatasetSize = DatasetShape[0]

    #CheckArguments:
    if (CheckArguments):
        ArgumentErrorMessage = ""
        if (DatasetShapeLength > 2):
            ArgumentErrorMessage += "PrintDataStatistics only supports datasets of `Type_NumpyOneDimensionalDataset` OR `Type_NumpyTwoDimensionalDataset`"
        if (len(ArgumentErrorMessage) > 0 ):
            if(PrintExtra):
                print "ArgumentErrorMessage:\n", ArgumentErrorMessage
            raise Exception(ArgumentErrorMessage)



    try:
        if (DatasetShapeLength == 1):
            DatasetDataType = "`Type_NumpyOneDimensionalDataset`"
            NumberDimensions = 1
            MinimumDomainPoint = numpy.min(Dataset, axis = 0)
            MaximumDomainPoint = numpy.max(Dataset, axis = 0)
            AverageDomainPoint = numpy.average(Dataset)
            StandardDeviation  = numpy.std(Dataset)
            PointSum           = numpy.sum(Dataset)

        if (DatasetShapeLength == 2):
            DatasetDataType = "`Type_NumpyTwoDimensionalDataset`"
            NumberDimensions = DatasetShape[1]
            MinimumDomainPoint = Library_DatasetGetMinimumDatapoint.Main(Dataset)
            MaximumDomainPoint = Library_DatasetGetMaximumDatapoint.Main(Dataset)
            AverageDomainPoint = numpy.average(Dataset,axis = 0)
            StandardDeviation  = numpy.std(Dataset, axis = 0)
            PointSum           = numpy.sum(Dataset, axis = 0)
    except:
            MinimumDomainPoint = None
            MaximumDomainPoint = None
            AverageDomainPoint = None
            StandardDeviation  = None
            PointSum           = None

    if (len(PrintLineHeader) > 0):
        print PrintLineHeader

    print SpaceBuffer + "DatasetDataType    : ", DatasetDataType
    print SpaceBuffer + "DatasetShape       : ", DatasetShape
    print SpaceBuffer + "DatasetSize        : ", DatasetSize
    print SpaceBuffer + "NumberDimensions   : ", NumberDimensions
    print SpaceBuffer + "MinimumDomainPoint : ", MinimumDomainPoint
    print SpaceBuffer + "MaximumDomainPoint : ", MaximumDomainPoint
    print SpaceBuffer + "AverageDomainPoint : ", AverageDomainPoint
    print SpaceBuffer + "StandardDeviation  : ", StandardDeviation
    print SpaceBuffer + "PointSum           : ", PointSum











