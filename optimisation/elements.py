from numpy import *
from numpy.random import *
from matplotlib import pyplot

## -----------------------------------------------
## Function definition, derivatives and error function
## -----------------------------------------------

def g(x,a):
    return exp(-x*a)

def f(t,data,a):
	s =0
	for x,y in zip(t,data):
		s += 0.5*(y-g(x,a))**2
	return s

def dg(x,a):
    return -x*exp(-x*a)

def gradf(t,data,a):
	s=0
	for x,y in zip(t,data):
		s -= (y-g(x,a))*dg(x,a)
	return s

def gradgradf(t,data,a):
	s=0
	for x,y in zip(t,data):
		s += dg(x,a)**2
	return s

## -----------------------------------------------
## Levenberg
## -----------------------------------------------

def methode_levenberg(nb_iter_max,a_init) :
	l=0.001
	a=a_init
	fmin= f(t,data,a)
	for i in range(nb_iter_max):
		print("iteration nb = ",i,"; f = ", fmin,"; lambda = ", l, "; a = ", a)
		grad2=gradf(t,data,a)
		gradgrad2=gradgradf(t,data,a)
		dlm=-grad2/(gradgrad2*(1+l))
		newf=f(t,data,a+dlm)
		if newf<fmin:
			a += dlm
			fmin=newf
			l *= 0.1
		else:
			l *=10
		if l>1e10:
			break
