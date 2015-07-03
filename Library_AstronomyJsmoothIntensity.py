

#def JsmoothIntensity_From_VisualAngleDegrees_And_Jsmooth(VisualAngleDegrees, Jsmooth):
def Main(VisualAngleDegrees = None, Jsmooth = None):
    JsmoothIntensity = Jsmooth / (VisualAngleDegrees**2) 
    return JsmoothIntensity
