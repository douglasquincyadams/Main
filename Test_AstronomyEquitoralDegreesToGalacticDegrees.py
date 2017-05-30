"""
REFERECNES:
    http://www.astro.virginia.edu/cgi-bin/utils/eqtogal


"""

import Library_AstronomyEquitoralDegreesToGalacticDegrees




RightAscensionDegrees   = 7.6447  #7, 38, 40.92 | 073840.92
DeclinationDegrees      = 7.6447


Result = Library_AstronomyEquitoralDegreesToGalacticDegrees.Main(    \
    RightAscensionDegrees = RightAscensionDegrees,            \
    DeclinationDegrees = DeclinationDegrees                 \
    )




print Result
