# -*- coding: utf-8 -*-
from math import *
diamatter = 12000
a = 384400
r = diamatter/2
delta_rad = 2*atan(r/(a*sqrt(1-(r/a)**2)))
unit= "km"
type = 1

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

def print_params():
   delta_deg = delta_rad * 180 / pi
   delta_degTaple = decdeg2dms(delta_deg)
   print("Size:r={0:,.2f}{1}".format(r * 2,unit))
   print("Distance:a={0:,.2f}{1}".format(a,unit))
   print("Angular diameter:{0:.0f}°{1:.0f}'{2:.2f}''".format(delta_degTaple[0],delta_degTaple[1],delta_degTaple[2]))

print_params()

while type != "0":
   print("[0]uit [1]Size [2]Distance\n[3]Diameter keep target size\n[4]Diameter keep distance\n[5]Unit")
   type=input("Enter Number [0]-[5] > ")
   if type == "1":
      rI=input("Enter radius of target >> ")
      r=float(rI)
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
      a  = sqrt((r/tan(delta_rad)/2)**2+(r**2))
      print_params()
   elif type == "4":
      dI=input("Enter Delta in D,M,S >> ").split(',')
      delta_rad = dms2decdeg(dI) / 180 * pi
      r = (a*tan(delta_rad/2))/sqrt(tan(delta_rad/2)**2 + 1)
      print_params()
   elif type == "5":
      unit = input("Enter Unit >> ")
      print_params()

print("Quit")