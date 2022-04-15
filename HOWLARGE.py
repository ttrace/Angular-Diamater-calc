# -*- coding: utf-8 -*-
from math import *
diamatter = 3478.8
a = 384400
r = diamatter/2
delta_rad = 2*atan(r/(a*sqrt(1-(r/a)**2)))
unit= "km"
type = 1
delta_deg = 0
hand_size = ''

print("Angular diameter of Moon")

# decdeg2dms(dd) from https://stackoverflow.com/questions/2579535/convert-dd-decimal-degrees-to-dms-degrees-minutes-seconds-in-python
def decdeg2dms(dd):
   is_positive = dd >= 0
   dd = abs(dd)
   minutes,seconds = divmod(dd*3600,60)
   degrees,minutes = divmod(minutes,60)
   degrees = degrees if is_positive else -degrees
   return (degrees,minutes,seconds)

def dms2decdeg(dms):
   decdeg=0.0
   degree = float(dms[0])
   if(degree >= 0):
      is_positive = True
   else:
      is_positive = False
   minutes = float(dms[1])/60
   second = float(dms[2])/3600
   dd = abs(degree)

   decdeg = dd + minutes + second
   if is_positive:
      return decdeg
   else:
      return decdeg * -1

def hand_sizes( deg ):
   if deg <= 1.0:
      return "1 pinkey width or narrower"
   elif deg <= 2.0:
      return "pinkey - thumb witdh"
   elif deg <= 5.0:
      return "thumb - 3 fingers width"
   elif deg <= 10.0:
      return "3 fingers - fist width"
   elif deg <= 15.0:
      return "fist - index-pin span"
   elif deg <= 20.0:
      return "index-pin ~ thumb-pin span"
   else:
      num_of_span = deg / 20
      return "{0:.1f} thumb-pin spans".format(num_of_span)

def print_params():
   delta_deg = delta_rad * 180 / pi
   delta_degTaple = decdeg2dms(delta_deg)
   diamatter = r * 2
   print("Size:{2:,.2f}{1}(r={0:,.2f}{1})".format(r,unit,diamatter))
   print("Distance:a={0:,.2f}{1}".format(a,unit))
   print("Angular diameter:{0:.0f}°{1:.0f}'{2:.2f}''".format(delta_degTaple[0],delta_degTaple[1],delta_degTaple[2]))
   print( hand_sizes(delta_deg) )

print_params()

while type != "0":
   print("[0]uit [1]Size [2]Distance\n[3]Diameter keep target size\n[4]Diameter keep distance\n[5]Unit")
   type=input("Enter Number [0]-[5] > ")
   if type == "1":
      rI=input("Enter size-diamatter of the target >> ")
      r= float(rI) / 2
      delta_rad = 2*atan(r/(a*sqrt(1-(r/a)**2)))
      print_params()
   elif type == "2":
      aI=input("Enter Distance to target >> ")
      a=float(aI)
      delta_rad = 2*atan(r/(a*sqrt(1-(r/a)**2)))
      print_params()
   elif type == "3":
      dI=input("Enter Delta in D,M,S >> ").split(',')
      delta_rad = dms2decdeg(dI) / 180 * pi
      a = r*sqrt(tan(delta_rad/2)**2 + 1)*(1/tan(delta_rad/2))
      print_params()
   elif type == "4":
      dI=input("Enter Delta in D,M,S >> ").split(',')
      delta_rad = dms2decdeg(dI) / 180 * pi
      r = (a*tan(delta_rad/2))/sqrt(tan**2(delta_rad/2) + 1)
      print_params()
   elif type == "5":
      unit = input("Enter Unit >> ")
      print_params()

print("Quit")