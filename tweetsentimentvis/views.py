from django.http import HttpResponse

from django.shortcuts import render

from src.twitter_handler import TweetFetcher

from src.lexicon_matcher import Matcher

import matplotlib.pyplot as plt
import PIL
import PIL.Image
import StringIO
import datetime


def index(request):
      return render(request,'index.html',{})


def emotion(request):
       q = request.GET['q']
       tweets = TweetFetcher.fetch(q)

       ans = Matcher.match()
       tweetlist = ans[0]
       ana = ans[1]
       topics = ans[2]
       return render(request,'emotion.html',{'tweetlist':tweetlist, 'ana':ana,'topics' :topics , 'q':q })

def sample(request):
       return render(request,'sample_template.html',{})


def charts(request):
       plt.x = [1,2,3]
       plt.y = [4,5,6]

       plt.plot(plt.x,plt.y,linewidth=2)
       plt.grid(True)
       buffer = StringIO.StringIO()
       canvas = plt.get_current_fig_manager().canvas
       canvas.draw()

       graphIMG = PIL.Image.fromstring("RGB", canvas.get_width_height(), canvas.tostring_rgb())
       graphIMG.save(buffer,"PNG")
       plt.close()

       return HttpResponse(buffer.getvalue, mimetype="image/png")




def linechart(request):

    #instantiate a drawing object
    import mycharts
    d = mycharts.MyLineChartDrawing()

    #extract the request params of interest.
    #I suggest having a default for everything.
    

    d.height = 600
    d.chart.height = 600
    

    d.width = 600
    d.chart.width = 600
   
    d.title._text = request.session.get('Tweet Emotion Analysis Through Time')
    


    d.XLabel._text = request.session.get('Time')
    d.YLabel._text = request.session.get('Emotion')
    
     

    d.chart.data = [((1,1.56), (2,2.78), (2.5,1), (3,3), (4,5)),((1,2), (2,3), (2.5,2), (3.5,5), (4,6))]
   

    
    labels =  ["Label One","Label Two"]
    if labels:
        # set colors in the legend
        d.Legend.colorNamePairs = []
        for cnt,label in enumerate(labels):
                d.Legend.colorNamePairs.append((d.chart.lines[cnt].strokeColor,label))


    #get a GIF (or PNG, JPG, or whatever)
    binaryStuff = d.asString('gif')
    return HttpResponse(binaryStuff, 'image/gif')



def piechart(request):
    #instantiate a drawing object
    import mycharts2
    

    #extract the request params of interest.
    #I suggest having a default for everything.
    drawing = mycharts2.BreakdownPieDrawing()  
    # the drawing will be saved as pdf and png below, you could do other things with it obviously.  
    binaryStuff = drawing.asString('gif')

    return HttpResponse(binaryStuff,'image/gif')
