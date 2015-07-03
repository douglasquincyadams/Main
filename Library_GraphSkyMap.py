"""
DESCRIPTION:

    Graph a list of objects in the sky into a single image

    Plots each point in a single graph

    If a z-dimension value is not provided 
        Color will be assigned
    

ARGS:
    Latitude
        Type: decimal degrees
        Description:
    Longitude
        Type: decimal degrees
        Description:
    Zvalue
        Type: decimal
        Description:

    ShapeFunction (OPTIONAL) 
        Type: ???(not sure how to do this)
        Default:
            Circles scaled by Zvalues
        Provided:
            Elipses...
                http://matplotlib.org/examples/pylab_examples/ellipse_demo.html

            FunkyShapes...

    Projection:
        Type: String
        Descprtion: Any of the following choices:
            None
            "Mollweide"
                http://stackoverflow.com/questions/16018243/pylab-contour-plot-using-mollweide-projection-create-artefacts
            "Hammer"        


RETURNS:
    None

"""

import numpy
import matplotlib
import matplotlib.pyplot
from mpl_toolkits.basemap import Basemap

import os
import Const_RegTestDir
#------------------------------------------------------------------------------
import Library_DateStringNowGMT
import Library_DatasetGetMaximumDatapoint
import Library_DatasetGetMinimumDatapoint
import Library_PrintDatasetStatistics


def Main(
    Latitudes                   = None ,
    Longitudes                  = None ,
    Zvalues                     = None ,
    Radii                       = None , 
    Zlabel                      = ""    ,
    Shapes                      = None ,
    Projection                  = "Rectangle" ,
    DirectoryGeneratedGraphs    = None ,
    SaveFigureFilePath          = "",
    DatasetNames                = [] ,
    ):
    

    if (DirectoryGeneratedGraphs == None):
        DirectoryGeneratedGraphs = Const_RegTestDir.Directory

    #print 'DirectoryGeneratedGraphs', DirectoryGeneratedGraphs

    #DIRECTORY DEFINING
    if (SaveFigureFilePath == ""):
        DirectoryDatasetNamesSuffix = "_".join(DatasetNames)
        DirectoryGeneratedGraphsCurrentRun = DirectoryGeneratedGraphs  + "/" + Library_DateStringNowGMT.Main() + "_" + DirectoryDatasetNamesSuffix
        if not os.path.exists(DirectoryGeneratedGraphsCurrentRun):
            os.makedirs(DirectoryGeneratedGraphsCurrentRun)
        GraphFileNamePrefix = Library_DateStringNowGMT.Main()[0:11]

        SaveFigureFilePath = DirectoryGeneratedGraphsCurrentRun + '/' + GraphFileNamePrefix + 'GalacticLongitude_GalacticLatitude_' + Zlabel + 'Projection' + Projection + '.png'


    #Graph image sizing: 
    #   Default to common monitor size:  
    #   1920pixels by 1080 pixels
    Inch_in_Pixels = 80.0
    MonitorSize = (1920.0/Inch_in_Pixels, 1080.0/Inch_in_Pixels)


    fig = matplotlib.pyplot.figure( figsize=MonitorSize )


    if (Projection == "Rectangle"):

        subplot = fig.add_subplot(111, aspect = 'equal' )

    
        #Figure out the number of pixels per degree 
        bbox = subplot.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
        subplotwidth, subplotheight = bbox.width, bbox.height
        subplotwidth    *= fig.dpi
        subplotheight   *= fig.dpi
        PixelsPerDegree = subplotwidth/400.0


        if (not Shapes == None):
            Points = []
            Radii = []

            FaceColors = numpy.ones(shape = (len(Shapes), 3))
            if (Zvalues != None):
                #http://stackoverflow.com/questions/2262100/rgb-int-to-rgb-python
                #Blue =  Zvalues & 255
                #Green = (Zvalues >> 8) & 255
                #Red =   (Zvalues >> 16) & 255

                #Find the max and min:
                Library_PrintDatasetStatistics.Main(Zvalues, 'Zvalues', 4)

                ColorValues = Zvalues - numpy.min(Zvalues)
                Library_PrintDatasetStatistics.Main(ColorValues, 'ColorValues shift', 4)

                #TODO: Make colors correct
                ColorValues = ColorValues * 256**3 / numpy.max(ColorValues)
                Library_PrintDatasetStatistics.Main(ColorValues, 'ColorValues rescale', 4)
                Blue    = (ColorValues % 256)
                Green   = (ColorValues  / 256) % 256 #numpy.zeros(shape = (len(Shapes) ) )#
                Red     = ((ColorValues / 256) / 256) % 256
                FaceColors = numpy.vstack((Red, Green, Blue)).T / 256
                Library_PrintDatasetStatistics.Main(FaceColors, 'FaceColors', 4)

            k = 0
            for Shape in Shapes:
                if (k % 500 == 0):
                    print 'Drawing Shapes ' + str(k) + ' to ' + str( k  + 500 ) 

                Shape.set_alpha(0.5)
                color= FaceColors[k]
                #print 'color', color
                Shape.set_facecolor( color )

                Points.append(list(Shape.center))
                Radii.append(Shape.height)
                Radii.append(Shape.width)
                subplot.add_artist(Shape)
                k = k + 1

        if (Longitudes == None or Latitudes == None):
            Points = numpy.array(Points)
            Radii = numpy.array(Radii)
            Longitudes = Points.T[0]
            Latitudes = Points.T[1]
        else:
            Points = numpy.vstack( (Longitudes, Latitudes) ).T
            Radii = numpy.ones(shape = (len(Points),))

    
    

        #Points = numpy.vstack(Latitudes, Longitudes).T
        scatter = subplot.scatter(
            Longitudes, 
            Latitudes, 
            marker= 'o', 
            s = .01,
            #            s = PixelsPerDegree*Zvalues*2.0, #PixelsPerDegree*1.0 , 
            #c = Zvalues, 
            #edgecolors='none'
            )



        subplot.set_xlabel( 'GalacticLongitude_in_degrees')
        subplot.set_ylabel( 'GalacticLatitude_in_degrees')
        #if (Zvalues != None):
        #    fig.colorbar( scatter, label = Zlabel ) 

        #Setting graph boundaries
        DomainMax = Library_DatasetGetMaximumDatapoint.Main(Points)
        DomainMin = Library_DatasetGetMinimumDatapoint.Main(Points)
        LargestRadius = numpy.max( Radii )
        subplot.set_xlim(DomainMin[0] - LargestRadius, DomainMax[0] + LargestRadius)
        subplot.set_ylim(DomainMin[1] - LargestRadius, DomainMax[1] + LargestRadius)





    elif (Projection == "Mollweide"):
        #http://stackoverflow.com/questions/16018243/pylab-contour-plot-using-mollweide-projection-create-artefacts
        subplot = Basemap(projection='moll', lat_0=0, lon_0=0, resolution='c')

        #Transform the latitudes to center at 0
        Lons = Longitudes - 180.0 #GalacticLongitude_in_degrees_1D - 180.0 
        print 'Lons.shape', Lons.shape
        Library_PrintDatasetStatistics.Main(Lons)

        #Transform the longitudes to center at 0
        Lats = Latitudes #GalacticLatitude_in_degrees_1D
        print 'Lats.shape', Lats.shape
        Library_PrintDatasetStatistics.Main(Lats)


        if (Zvalues == None):
            Zvalues = numpy.ones(shape = (len(Lons), ))


        #Plot the points: TODO
        if (Shapes == None):

            x, y = subplot(Lons, Lats)
            scatter = subplot.scatter(  
                x, 
                y, 
                marker= 'o',  
                c = Zvalues,
                )

            #if (Zvalues != None):
            #    if (Zlabel == None):
            #        Zlabel = 'NoLabelProvided'
            #    fig.colorbar( scatter, label = Zlabel ) 


        else:
            #for shape in Shapes:
            #    shape.set_alpha(0.5)
            #    subplot.add_artist(shape)
            pass



        colorbar = subplot.colorbar( scatter, label = Zlabel ) 


        #Add and lable the grid:
        # draw parallels.
        parallels = numpy.arange(-90.,90,10.)
        subplot.drawparallels(parallels, labels=[1,1,1,1],fontsize=10) # labels = [left,right,top,bottom]

        # draw meridians
        meridians = numpy.arange(0.,360.,10.)
        subplot.drawmeridians(meridians) # labels = [left,right,top,bottom]  -> Cannot put labels on meridians
        #plt.grid(True)


        #plt.savefig( DirectoryGeneratedGraphsCurrentRun + '/' + GraphFileNamePrefix + 'GalacticLongitude_GalacticLatitude_Log10Jsmooths_SquareProjection.png' )


        """

        #s = PixelsPerDegree*VisualAngles_in_degrees_1D, 
        #c = Log10Jsmooths_1D, 
        #edgecolors='none',


        #subplot.set_xlabel('GalacticLongitude_in_degrees_1D')
        #subplot.set_ylabel(' GalacticLatitude_in_degrees_1D')


        #LOCATIONS PLOT:
        #   SkyMap Projection Graphs: "http://matplotlib.org/basemap/users/moll.html"
        #   Screen width(px)     1920.0


        #subplot = fig.add_subplot(111)
        #   Graph Width(px) && Height(px)         
        #bbox = subplot.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
        #subplotwidth, subplotheight = bbox.width, bbox.height
        #subplotwidth    *= fig.dpi
        #subplotheight   *= fig.dpi
        #   How many pixels in 1 degree
        #PixelsPerDegree = subplotwidth/400.0
        """

    #Save the figure:
    matplotlib.pyplot.savefig( SaveFigureFilePath )
    matplotlib.pyplot.grid(True)

    return None












































