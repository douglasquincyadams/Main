

"""

DESCRIPTION:
    


"""
import numpy
import matplotlib
import matplotlib.pylab
import pprint
import scipy
import scipy.interpolate 

import Library_LocalStorageLoadVariable
import Library_ComponentExtract
import Library_TableSortRowsByColumn
import Library_IterableSelect
import Library_ChiSquaredConfidenceLevelToDeltaLogLikelihoodMaximum
import Library_PrintDatasetStatistics

def Main(
    PossibleWimpMasses = None,
    PossibleAnnihilationCrossSections = None,
    DirectoryGeneratedGraphsCurrentRun = None,
    ):

    #size the graphs
    #   Default to common monitor size:  
    #   1920pixels by 1080 pixels
    print 'Sizing the graphs...'
    Inch_in_Pixels = 80.0
    MonitorSize = (1920.0/Inch_in_Pixels,1080.0/Inch_in_Pixels)


    #Search in temporary data storage for the profiled out likelihoods 
    #   based on mass and cross section:
    WimpMultiMassMultiAnnihilationCrossSectionLikelihoodCube = [] 
    for PossibleWimpMass in PossibleWimpMasses:
        WimpMassMultiAnnihilationCrossSectionLikelihoodCubeStorageName = 'WimpMassMultiAnnihilationCrossSectionLikelihoodCube_' + str(PossibleWimpMass)
        WimpMassMultiAnnihilationCrossSectionLikelihoodCube = Library_LocalStorageLoadVariable.Main(
            VariableName = WimpMassMultiAnnihilationCrossSectionLikelihoodCubeStorageName,
            )
        if (WimpMassMultiAnnihilationCrossSectionLikelihoodCube == None):
            ErrMsg = 'WimpMassMultiAnnihilationCrossSectionLikelihoodCube not found \n'
            ErrMsg += '  for Mass == ' + str(PossibleWimpMass)
            raise Exception( ErrMsg )

        WimpMultiMassMultiAnnihilationCrossSectionLikelihoodCube.append(WimpMassMultiAnnihilationCrossSectionLikelihoodCube)

    #--------------------
    #Find CrossSections Per ConfidenceLevel Per Mass


    MultiMassMultiCrossSectionConfidenceInfo = []

    print "Finding confidence levels per mass..."
    NumberSigmas = 5

    PossibleWimpMassIndex = 0
    for WimpMassLikelihoodInfos in WimpMultiMassMultiAnnihilationCrossSectionLikelihoodCube:
        PossibleWimpMass = WimpMassLikelihoodInfos[0]["PossibleWimpMass"] 
        print 'Working on PossibleWimpMass', PossibleWimpMass

        #Get possible cross sections for the given mass:  
        CrossSectionInputs = []
        for InfoObject in WimpMassLikelihoodInfos:
            CrossSectionInput = Library_ComponentExtract.Main(
                Object            = InfoObject,
                Key               = "PossibleAnnihilationCrossSection",
                DefaultValue      = 0 ,
                )
            CrossSectionInputs.append(CrossSectionInput)
        CrossSectionInputs = numpy.array(CrossSectionInputs)
        CrossSectionDomainRange = (numpy.min(CrossSectionInputs), numpy.max(CrossSectionInputs) )
        #print 'numpy.min(CrossSectionInputs)', numpy.min(CrossSectionInputs)
        print '  CrossSectionDomainRange', CrossSectionDomainRange
        
        #Get the assocated log likelihood values 
        #   ( each has a different set of associated maximal nuisance parameter(s) 
        #   which we have profiled out ):
        LogLikelihoodOutputs = []
        for InfoObject in WimpMassLikelihoodInfos:
            LogLikelihoodOutput = float( Library_ComponentExtract.Main(
                Key               = "MaximalLogLikelihoodValue",
                Object            = InfoObject,
                DefaultValue      = 0 ,
                ) )
            LogLikelihoodOutputs.append(LogLikelihoodOutput)
        LogLikelihoodOutputs = numpy.array(LogLikelihoodOutputs)

        #Concatonate the cross sections and the LogLikelihoods into a Dataset
        CrossSectionsLogLikelihoodsDataset = numpy.array( Library_TableSortRowsByColumn.Main( numpy.vstack((CrossSectionInputs, LogLikelihoodOutputs)).T.tolist(), 0 ) )
        CrossSectionInputsOrdered   = CrossSectionsLogLikelihoodsDataset.T[0]
        LogLikelihoodOutputsOrdered        = CrossSectionsLogLikelihoodsDataset.T[1]

        print 'CrossSectionInputsOrdered', CrossSectionInputsOrdered
        print 'LogLikelihoodOutputsOrdered', LogLikelihoodOutputsOrdered


        #Find a function which fits the LogLikelihoods && CrossSections:
        SplineSuccess = True
        LogLikelihoodFitFunctionCallable = None
        try:
            #LogLikelihoodFitFunctionCallable = scipy.interpolate.UnivariateSpline(
            LogLikelihoodFitFunctionCallable = scipy.interpolate.InterpolatedUnivariateSpline(
                    CrossSectionInputsOrdered, 
                    LogLikelihoodOutputsOrdered,
                    k = 4,
                    ext = 0,
                    )

            def NegativeLogLikelihoodFitFunctionCallable(Point):
                return -1.*LogLikelihoodFitFunctionCallable(Point)
            print '  NegativeLogLikelihoodFitFunctionCallable(10**(-28))',  NegativeLogLikelihoodFitFunctionCallable(numpy.array([ 4*10.**(-29.)]))


            #Find the maximum log likelihood of the fit function:
            #   Find the zero's of the fit function derivative and find the edges of the window
            PossibleWindowMaximumLogLikelihoodCrossSections = list( LogLikelihoodFitFunctionCallable.derivative().roots() ) + numpy.array(CrossSectionDomainRange).tolist()
            print '  PossibleWindowMaximumLogLikelihoodCrossSections', PossibleWindowMaximumLogLikelihoodCrossSections

            #   Select only the cross sections which are greater than zero
            def NumbersGreaterThanZero(Num):
                if (Num >= 0):
                    return True
                return False    
            PossibleWindowMaximumLogLikelihoodCrossSectionsGreaterThanZero = Library_IterableSelect.Main(
                Iterable = PossibleWindowMaximumLogLikelihoodCrossSections,
                ConditionFunction = NumbersGreaterThanZero,
                )
            print '  PossibleWindowMaximumLogLikelihoodCrossSectionsGreaterThanZero', PossibleWindowMaximumLogLikelihoodCrossSectionsGreaterThanZero

            #   Plug in our possible values and pick the best choice to be our `MaximalLoglikelihoodValue`
            MaximalCrossSectionIndex = 0
            MaximalLoglikelihoodValue = -1.*numpy.inf
            k = 0 
            for CrossSection in PossibleWindowMaximumLogLikelihoodCrossSectionsGreaterThanZero:
                CrossSectionLogLikelihood = LogLikelihoodFitFunctionCallable(CrossSection)
                if ( CrossSectionLogLikelihood > MaximalLoglikelihoodValue ):
                    MaximalCrossSectionIndex = k
                    MaximalLoglikelihoodValue = CrossSectionLogLikelihood
                k = k + 1
            MaximalCrossSection = PossibleWindowMaximumLogLikelihoodCrossSectionsGreaterThanZero[MaximalCrossSectionIndex]
            print '  MaximalCrossSection', MaximalCrossSection
            print '  MaximalLoglikelihoodValue', MaximalLoglikelihoodValue



            def MinusTwoDeltaLogLikelihoodFitFunctionCallable(Point):
                return -2 * ( LogLikelihoodFitFunctionCallable(Point) - MaximalLoglikelihoodValue )

            #Convert the LogLikelihoods to -2*deltaloglikelihoods:
            DeltaLogLikelihoods = LogLikelihoodOutputs - MaximalLoglikelihoodValue
            MinusTwoDeltaLogLikelihoods = -2.*( DeltaLogLikelihoods )

            #Find the values on our fit which correspond to certain confidence levels
            #   Confidence level 
            SigmasToAquire =  numpy.arange(NumberSigmas + 1)[1:]
            ConfidenceLevelsOfWhichToObtainCrossSectionValues = scipy.special.erfc( SigmasToAquire / numpy.sqrt(2.) )
            print '  ConfidenceLevelsOfWhichToObtainCrossSectionValues', ConfidenceLevelsOfWhichToObtainCrossSectionValues

            #Find the associated distance of the chi-squared cumulative distribution function to the confidence level
            NumDimensions = 1 #Degrees of freedom
            TwoDeltaLogLikelihoodConfidenceLevelChiSquaredDistances = []
            for ConfidenceLevel in ConfidenceLevelsOfWhichToObtainCrossSectionValues:
                ChiSquaredDistance = Library_ChiSquaredConfidenceLevelToDeltaLogLikelihoodMaximum.Main(NumDimensions, ConfidenceLevel)
                TwoDeltaLogLikelihoodConfidenceLevelChiSquaredDistances.append(ChiSquaredDistance)
            TwoDeltaLogLikelihoodConfidenceLevelChiSquaredDistances = numpy.array(TwoDeltaLogLikelihoodConfidenceLevelChiSquaredDistances)
            print '  TwoDeltaLogLikelihoodConfidenceLevelChiSquaredDistances', TwoDeltaLogLikelihoodConfidenceLevelChiSquaredDistances

            #Find the -2 deltaloglikelihood values associated with the ConfidenceLevelChiSquaredDistances
            #MinimalMinusTwoDeltaLogLikelihoodValue = MinusTwoDeltaLogLikelihoodFitFunctionCallable( MaximalCrossSection ) #This should be zero
            #ConfidenceLevelMinusTwoDeltaLogLikelihoodValues = MinimalMinusTwoDeltaLogLikelihoodValue + ConfidenceLevelChiSquaredDistances
            #print '  ConfidenceLevelMinusTwoDeltaLogLikelihoodValues', ConfidenceLevelMinusTwoDeltaLogLikelihoodValues
            LogLikelihoodChiSquaredConfidenceLevelDistances = TwoDeltaLogLikelihoodConfidenceLevelChiSquaredDistances/2.
            print '  LogLikelihoodChiSquaredConfidenceLevelDistances', LogLikelihoodChiSquaredConfidenceLevelDistances

            ConfidenceLevelLogLikelihoodValues = LogLikelihoodFitFunctionCallable( MaximalCrossSection ) - LogLikelihoodChiSquaredConfidenceLevelDistances
            print '  ConfidenceLevelLogLikelihoodValues', ConfidenceLevelLogLikelihoodValues

            #Find the CrossSections associated with the ConfidenceLevelLogLikelihoodValues 
            #   http://stats.stackexchange.com/questions/126251/how-do-i-force-the-l-bfgs-b-to-not-stop-early-projected-gradient-is-zero
            #   Ways to do this:
            #           DesiredValue = InverseLogLikelihoodFitFunctionCallable( ConfidenceLevelLogLikelihoodValue )
            #       OR
            #           DesiredValue = scipy.optimize.minimize( ( LogLikeFn( DesiredValue ) - LogLikeFn( ConfidenceLevelLogLikelihoodValue) **2 )
            #       OR
            #           DesiredValue = roots(LogLikeFn(data - ConfidenceLevel) )
            ConfidenceLevelCrossSectionValues = []
            for ConfidenceLevel in ConfidenceLevelLogLikelihoodValues:
                #AdjustedLogLikelihoodFitFunction = scipy.interpolate.UnivariateSpline(
                AdjustedLogLikelihoodFitFunction = scipy.interpolate.InterpolatedUnivariateSpline(
                    CrossSectionInputsOrdered, 
                    LogLikelihoodOutputsOrdered - ConfidenceLevel,
                    k = 3 )
                CrossSectionValues = AdjustedLogLikelihoodFitFunction.roots()
                CrossSectionValuesCount = len(CrossSectionValues)
                if (CrossSectionValuesCount == 0):
                    CrossSectionValues = [0.0, numpy.inf]
                elif(CrossSectionValuesCount == 1):
                    OnlyCrossSectionValue = CrossSectionValues[0]
                    if (OnlyCrossSectionValue < MaximalCrossSection):
                        CrossSectionValues = [OnlyCrossSectionValue, numpy.inf]
                    else:
                        CrossSectionValues = [0.0, OnlyCrossSectionValue]
                elif(CrossSectionValuesCount == 2):
                    pass
                else:
                    print 'INVESTIGATE!!\n\n '
                    print '  There is a very bad fit to the datapoints -> does not look like upside down parabola'
                    print CrossSectionValues
                    CrossSectionValues = CrossSectionValues[0:2].tolist()
                    errmsg = 'More than two results for cross sections associated with a confidence level '
                    print errmsg
                    #raise Exception(errmsg)
                ConfidenceLevelCrossSectionValues.append( CrossSectionValues )


            print '  ConfidenceLevelCrossSectionValues'
            pprint.pprint(ConfidenceLevelCrossSectionValues, indent = 3)

            SigmaConfidenceInfos = []
            k = 0
            for Sigma in SigmasToAquire:
                SigmaConfidenceInfo = {
                "Sigma" : Sigma, 
                "CrossSectionValues" : ConfidenceLevelCrossSectionValues[k],
                "ConfidenceLevelLogLikelihoodValue" : ConfidenceLevelLogLikelihoodValues[k],
                }
                SigmaConfidenceInfos.append(SigmaConfidenceInfo)
                k = k + 1

            ConfidenceInfoObject = {
                "PossibleWimpMass" : PossibleWimpMass,
                "MaximalCrossSection": MaximalCrossSection,
                "MaximalLoglikelihoodValue": MaximalLoglikelihoodValue,
                "SigmaConfidenceInfos": SigmaConfidenceInfos,
            }

            MultiMassMultiCrossSectionConfidenceInfo.append(ConfidenceInfoObject)




            #Evaluate the fitfunction at various cross sections:
            #   Curve Fit
            CrossSectionEvalPoints = numpy.linspace( numpy.min( CrossSectionInputs ), numpy.max( CrossSectionInputs ) )
            LogLikelihoodFitFunctionEvaluationValues = []
            for EvalPoint in CrossSectionEvalPoints:
                EvaluationValue = LogLikelihoodFitFunctionCallable(EvalPoint)
                LogLikelihoodFitFunctionEvaluationValues.append(EvaluationValue)
            LogLikelihoodFitFunctionEvaluationValues = numpy.array(LogLikelihoodFitFunctionEvaluationValues)

        except Exception, e:
            SplineSuccess = False
            print str(e)
            print 'Profiling the maximums failed'

        #GRAPH:
        #   the loglikelihoods 
        #   the polynomial fit
        #   the maximal loglikelihood value
        SingleMassMultiLogLikelihoodsFigureName = "Mass" + str(PossibleWimpMass) + "AnnihilationMinusTwoDeltaLogLikelihoods"
        matplotlib.pylab.figure(SingleMassMultiLogLikelihoodsFigureName, figsize = MonitorSize)


        #   Observed Maximal Likelihoods:
        matplotlib.pylab.semilogx(
            CrossSectionInputs, 
            LogLikelihoodOutputs, 
            'o' 
            )
        matplotlib.pylab.semilogx(
            CrossSectionInputs, 
            LogLikelihoodOutputs, 
            '+',
            markersize = 40, 
            )


        if (SplineSuccess):
            #   Fit:
            matplotlib.pylab.semilogx(
                CrossSectionEvalPoints, 
                LogLikelihoodFitFunctionEvaluationValues, 
                linewidth = 2, 
                label = 'CurveFit'
                )
            #   Maximum Likelihood
            matplotlib.pylab.semilogx(
                MaximalCrossSection,
                MaximalLoglikelihoodValue,
                'o',
                markersize = 10,
                )

            #   SigmaCrossSections:
            FlattenedConfidenceLevelCrossSectionValues = numpy.array(ConfidenceLevelCrossSectionValues).flatten()
            print 'FlattenedConfidenceLevelCrossSectionValues', FlattenedConfidenceLevelCrossSectionValues

            FlattenedConfidenceLevelLogLikelihoodValues = numpy.vstack((ConfidenceLevelLogLikelihoodValues, ConfidenceLevelLogLikelihoodValues)).T.flatten()
            print 'FlattenedConfidenceLevelLogLikelihoodValues', FlattenedConfidenceLevelLogLikelihoodValues

            matplotlib.pylab.plot(
                FlattenedConfidenceLevelCrossSectionValues,
                FlattenedConfidenceLevelLogLikelihoodValues,
                'o',
                markersize = 10,
                
                )
        matplotlib.pylab.xlabel('PossibleAnnihilationCrossSections (cm^3/s) ')
        matplotlib.pylab.ylabel('LogLikelihood ')
        matplotlib.pylab.savefig(  DirectoryGeneratedGraphsCurrentRun  + '/' + SingleMassMultiLogLikelihoodsFigureName +'.png')
        matplotlib.pylab.close(SingleMassMultiLogLikelihoodsFigureName)
            

        #if (PossibleWimpMassIndex > 1):
        #    break
        PossibleWimpMassIndex += 1 



    #Make single graph of the confidence data per mass all at once:
    print '  Graphing Nsigma CrossSections for each Mass'
    matplotlib.pylab.figure("MassCrossSectionsConfidence", figsize = MonitorSize)

    PossibleWimpMasses = []
    MaximalCrossSections = []
    MultiMassNSigmaCrossSections = []
    for SingleMassMultiCrossSectionInfo in MultiMassMultiCrossSectionConfidenceInfo:
        MaximalCrossSections.append( SingleMassMultiCrossSectionInfo["MaximalCrossSection"] )
        PossibleWimpMasses.append(SingleMassMultiCrossSectionInfo["PossibleWimpMass"])

        NSigmaCrossSections = []    
        for SigmaInfo in SingleMassMultiCrossSectionInfo["SigmaConfidenceInfos"]:
            SigmaCrossSectionValues = SigmaInfo["CrossSectionValues"]
            SigmaUpper = SigmaCrossSectionValues[0]
            SigmaLower = SigmaCrossSectionValues[1]
            NSigmaCrossSections.append(SigmaUpper)
            NSigmaCrossSections.append(SigmaLower)

        MultiMassNSigmaCrossSections.append(sorted(NSigmaCrossSections))


    MaximalCrossSections = numpy.array(MaximalCrossSections)
    print 'MaximalCrossSections'
    pprint.pprint( MaximalCrossSections )

    MultiMassNSigmaCrossSections = numpy.array(MultiMassNSigmaCrossSections)
    print 'MultiMassNSigmaCrossSections'    , 
    pprint.pprint(MultiMassNSigmaCrossSections)

    MultiMassNSigmaCrossSectionsTranspose = MultiMassNSigmaCrossSections.T
    print 'MultiMassNSigmaCrossSectionsTranspose'
    pprint.pprint(MultiMassNSigmaCrossSectionsTranspose)

    #   Maximum Likelihood Cross Section:
    matplotlib.pylab.plot(
        numpy.array(PossibleWimpMasses)/1000.       ,
        numpy.array(MaximalCrossSections)           ,
        'o-'                                        ,
        markersize = 10                             ,
        )


    for SigmaCrossSections in MultiMassNSigmaCrossSectionsTranspose:
        #   Maximum Likelihood Cross Section:
        matplotlib.pylab.plot(
            numpy.array(PossibleWimpMasses)/1000.   ,
            numpy.array(SigmaCrossSections)         ,
            '-'                                     ,
            markersize = 10                         ,
            )


    matplotlib.pylab.xlabel('PossibleWimpMasses (GeV) ')
    matplotlib.pylab.ylabel('PossibleAnnihilationCrossSections (cm^3/s) ')
    matplotlib.pylab.savefig(  DirectoryGeneratedGraphsCurrentRun  + '/MassCrossSectionsConfidence.png')
    print DirectoryGeneratedGraphsCurrentRun
    print 'PossibleWimpMasses', PossibleWimpMasses



