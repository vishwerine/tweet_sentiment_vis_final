#! /usr/env/bin python


from reportlab.graphics.charts.piecharts import Pie  
from reportlab.lib.colors import black, red, purple, green, maroon, brown, pink, white, HexColor  
from reportlab.graphics.charts.legends import Legend  
from reportlab.graphics.shapes import Drawing, _DrawingEditorMixin  
from reportlab.lib.validators import Auto  
from reportlab.lib.colors import HexColor, black  



from tweetsentimentvis.models import MacroObject

  
pdf_chart_colors = [  
        HexColor("#0000e5"),  
        HexColor("#1f1feb"),  
        HexColor("#5757f0"),  
        HexColor("#8f8ff5"),  
        HexColor("#c7c7fa"),  
        HexColor("#f5c2c2"),  
        HexColor("#eb8585"),  
        HexColor("#e04747"),  
        HexColor("#d60a0a"),  
        HexColor("#cc0000"),  
        HexColor("#ff0000"),  
        ]  
  
def setItems(n, obj, attr, values):  
    m = len(values)  
    i = m // n  
    for j in xrange(n):  
        setattr(obj[j],attr,values[j*i % m])  
  
class BreakdownPieDrawing(_DrawingEditorMixin,Drawing):  
    def __init__(self,width=600,height=400,*args,**kw):  
        apply(Drawing.__init__,(self,width,height)+args,kw)  
        # adding a pie chart to the drawing   
        self._add(self,Pie(),name='pie',validate=None,desc=None)  
        self.pie.width                  = 350  
        self.pie.height                 = self.pie.width  
        self.pie.x                      = 20  
        self.pie.y                      = (height-self.pie.height)/2
  
        t = MacroObject.objects.all()
        list1 = []
        list2 = []
        for l in t:
             list1.append(l.valu)
             list2.append(l.text)           
        self.pie.data = list1  
        self.pie.labels = list2
        self.pie.simpleLabels           = 1  
        self.pie.slices.label_visible   = 0  
        self.pie.slices.fontColor       = None  
        self.pie.slices.strokeColor     = white  
        self.pie.slices.strokeWidth     = 1  
        # adding legend  
        self._add(self,Legend(),name='legend',validate=None,desc=None)  
        self.legend.x               = 400  
        self.legend.y               = height/2  
        self.legend.dx              = 40  
        self.legend.dy              = 40 
        self.legend.fontName        = 'Helvetica'  
        self.legend.fontSize        = 7  
        self.legend.boxAnchor       = 'w'  
        self.legend.columnMaximum   = 10  
        self.legend.strokeWidth     = 1  
        self.legend.strokeColor     = black  
        self.legend.deltax          = 85  
        self.legend.deltay          = 20  
        self.legend.autoXPadding    = 5  
        self.legend.yGap            = 0  
        self.legend.dxTextSpace     = 5  
        self.legend.alignment       = 'right'  
        self.legend.dividerLines    = 1|2|4  
        self.legend.dividerOffsY    = 4.5  
        self.legend.subCols.rpad    = 30  
        n = len(self.pie.data)  
        setItems(n,self.pie.slices,'fillColor',pdf_chart_colors)  
        self.legend.colorNamePairs = [(self.pie.slices[i].fillColor, (self.pie.labels[i][0:20], '%0.2f' % self.pie.data[i])) for i in xrange(n)]  
  
