from django import template

register = template.Library()

@register.filter(name="samplefunc")
def sampleFunc(value):
     return value

def getNo(s):
      if s=="sadness":
              return 0
      elif s=="anger":
              return 1
      elif s=="fear":
              return 2
      elif s=="trust":
              return 3
      elif s=="disgust":
              return 4
      elif s=="anticipation":
              return 5
      elif s=="joy":
              return 6
      elif s=="surprise":
              return 7
      elif s=="negative":
              return 8
      else:
       return 9
          


@register.filter(name="posinegi")
def posinegi(value,args):
         ans = value
         su = 0
         
         su = ans[9] + ans[8]

         if args=="up":
             return ans[9]*100/su
         elif args=="down":
             return ans[8]*100/su


@register.filter(name="percen")
def percen(value,args):
      ans = value
      
      su = 0
      for a in ans:
           su = su + a

      if args=="sadness":
             return ans[0]*100.0/su
      elif args=="anger":
             return ans[1]*100.0/su
      elif args=="fear":
             return ans[2]*100.0/su
      elif args=="trust":
             return ans[3]*100.0/su
      elif args=="disgust":
             return ans[4]*100.0/su
      elif args=="anticipation":
             return ans[5]*100.0/su
      elif args=="joy":
             return ans[6]*100.0/su
      elif args=="surprise":
             return ans[7]*100.0/su

