"""
DESCRIPTION:


ARGS:


RETURNS:


"""


import numpy
import Library_PrintDatasetStatistics
import Library_Gaussian
import Const_LocalDirectoriesFermiFiles


import DS_ReadingLiveTimeCube
import Library_DataGetFermiInstrumentResponseSkyExposurePass7




def Main(
    GroupSourcesData = None,
    GroupSourcesDataColumnNames = None,
    ReturnNormalizedFunction = False,
    PossibleWimpMass=None,
    ):

    GalaxyGroupCount = len(GroupSourcesData)

    #Jfactor Means for all groups
    BoostFactor=5.
    GalaxyGroupJsmoothMeans = GroupSourcesData[:,[GroupSourcesDataColumnNames.index("Jsmooth")] ] * (1.9e26)*BoostFactor #sec*mev^2 / cm^5

    #Jfactor Variances for all groups
    GalaxyGroupJsmoothVariances = (0.2)**2. * (GalaxyGroupJsmoothMeans**2.)

    #The position of the Clusters on the Sky
    RA=GroupSourcesData[:,[GroupSourcesDataColumnNames.index(  "GalacticLongitudeInDegrees" )] ]
    DEC=GroupSourcesData[:,[GroupSourcesDataColumnNames.index(  "GalacticLatitudeInDegrees" )] ]

    #LiveTimeCube
    directoryofLivetimeCube= Const_LocalDirectoriesFermiFiles.DataFilesLiveTimeCubeDirectory
    FileandDir_livetime=directoryofLivetimeCube+'/exposurecube_filtered_events_10GeV_1TeV_zmax100_GTI_ultraclean.fits'
   
    #Front Effective Area
    filenameEffArea='aeff_P7REP_ULTRACLEAN_V15_back.fits'
    directoryEffectiveArea=Const_LocalDirectoriesFermiFiles.DataFilesInstrumentResponse4UltraEffectiveAreaDirectory
    FileandDir_EA=directoryEffectiveArea+'/'+filenameEffArea
   
    #front Exposure
    SkyExposureBack=Library_DataGetFermiInstrumentResponseSkyExposurePass7.Main(
        FileandDir_EA=FileandDir_EA,
        FileandDir_livetime=FileandDir_livetime,
        EnergyScalelog10=numpy.log10(PossibleWimpMass),
        )
    #back Effective Area
    filenameEffArea='aeff_P7REP_ULTRACLEAN_V15_front.fits'
    directoryEffectiveArea=Const_LocalDirectoriesFermiFiles.DataFilesInstrumentResponse4UltraEffectiveAreaDirectory
    FileandDir_EA=directoryEffectiveArea+'/'+filenameEffArea
   
    #Back Exposure
    SkyExposureFront=Library_DataGetFermiInstrumentResponseSkyExposurePass7.Main(
        FileandDir_EA=FileandDir_EA,
        FileandDir_livetime=FileandDir_livetime,
        EnergyScalelog10=numpy.log10(PossibleWimpMass)
        )
    
    #Back and Front Exposure of the Clusters
    ExposureGalaxy=DS_ReadingLiveTimeCube.Cosine_liveTime(
        CosineLiveTimeData=SkyExposureFront+SkyExposureBack,
        Dec=DEC,
        RA=RA,
        )

    #Signal Proability Density Shape:
    TotalJsmoothExposureAdjustedMean = \
        numpy.sum(GalaxyGroupJsmoothMeans * ExposureGalaxy)
    print 'TotalJsmoothExposureAdjustedMean', TotalJsmoothExposureAdjustedMean

    TotalJsmoothExposureAdjustedVariance = \
        numpy.sum( GalaxyGroupJsmoothVariances * (ExposureGalaxy**2) )
    print 'TotalJsmoothExposureAdjustedVariance', TotalJsmoothExposureAdjustedVariance

    print ''

    #Note: Exposure is accounted for in this density:
    def TotalJsmoothExposureFoldProbabilityDensityFunction( 
            TotalJfactor = None,
            Log = False,
        ):
        
        Result = Library_Gaussian.Main(
                Point = TotalJfactor, 
                MeanPoint = TotalJsmoothExposureAdjustedMean, 
                CovarianceMatrix = TotalJsmoothExposureAdjustedVariance, 
                Log = Log,
            )

        #This could be done with a log normal distribution instead of a normal distribution
        return Result

    return TotalJsmoothExposureFoldProbabilityDensityFunction























