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
    PrintLinePrefix = "",
    WantedStatistics = [],
    CheckArguments = True,
    PrintExtra = False
    ):

    #Obtain some information about the dataset which can be used for both:
    #   CheckArguments
    #   Printing
    DatasetShape = Dataset.shape
    DatasetShapeLength = len(DatasetShape)
    SpaceBuffer = " "*PrintLineBufferSize
    if (PrintLinePrefix == ""):
        Prefix = SpaceBuffer
    else:
        Prefix = PrintLinePrefix + SpaceBuffer

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


    DatasetMemory = Dataset.nbytes


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
        print Prefix + PrintLineHeader

    if (WantedStatistics == []):
        WantedStatistics = [
            "DatasetDataType",
            "DatasetShape",
            "DatasetSize",
            "NumberDimensions",
            "MinimumDomainPoint",
            "MaximumDomainPoint",
            "AverageDomainPoint",
            "StandardDeviation",
            "PointSum",
            "DatasetMemory",
            ]

    if ("DatasetDataType" in WantedStatistics):
        print Prefix + SpaceBuffer + "DatasetDataType    : ", DatasetDataType

    print Prefix + SpaceBuffer + "DatasetShape       : ", DatasetShape
    print Prefix + SpaceBuffer + "DatasetSize        : ", DatasetSize
    print Prefix + SpaceBuffer + "NumberDimensions   : ", NumberDimensions
    print Prefix + SpaceBuffer + "MinimumDomainPoint : ", MinimumDomainPoint
    print Prefix + SpaceBuffer + "MaximumDomainPoint : ", MaximumDomainPoint
    print Prefix + SpaceBuffer + "AverageDomainPoint : ", AverageDomainPoint
    print Prefix + SpaceBuffer + "StandardDeviation  : ", StandardDeviation
    print Prefix + SpaceBuffer + "PointSum           : ", PointSum
    print Prefix + SpaceBuffer + "DatasetMemory      : ", DatasetMemory










