import numpy as np


## -----------------------------------------------
## Function definition, derivatives and error function
## -----------------------------------------------

# fonction f
def f(vect) : # X et Y additionnables entre eux
	X = vect[0]
	Y = vect[1]
	return X**2 -Y**2

def g(vect) :
	X = vect[0]
	Y = vect[1]
	return np.array([2*X, -2*Y])

def h(vect) :
	X = vect[0]
	Y = vect[1]
	return np.array([[2, 0 ],[0, -2]])

def norm1_gradient(vect):
	X = vect[0]
	Y = vect[1]
	return abs(g(vect)[0])+abs(g(vect)[1])


## -----------------------------------------------
## Gradient
## -----------------------------------------------

def methode_gradient(f,g,nb_iter_max,pas,seuil_err,x_init) :
	xcour = x_init
	print("")
	print("--------GRADIENT DESCENT--------")
	erreur = norm1_gradient(xcour)
	tab_parcours_grad = [xcour]
	condition_f = True
	i = 0
	print("iteration ",i , " ; x = ",xcour, " ; norm 1 gradient = ", erreur)
	while (i < nb_iter_max and erreur > seuil_err and condition_f) :
		xsuiv = xcour - pas*g(xcour) #iteration suivante
		erreur = norm1_gradient(xsuiv)
		i = i+1
		tab_parcours_grad.append(xsuiv)
		condition_f = f(xsuiv) < f(xcour)
#		print "condition_f =",condition_f
		xcour = xsuiv
		print("iteration ",i , " ; x = ",xcour, " ; norm 1 gradient = ", erreur)
	print("---------------")
	print("Stopping condition(s):")
	if (i==nb_iter_max) :
		print("Maximum iteration number reached: ", nb_iter_max)

	if (erreur < seuil_err) :
		print("Gradient norm is below defined threshold")
		print("norm 1 gradient = ", erreur, " < ", seuil_err)

	if (condition_f == False) :
		print("Next iteration does not decrease the cost function value")
		print("Current value f(x) = ", f(xcour), " ; Next value f(x+1) = ", f(xsuiv))

	print("---------------")
	
	return tab_parcours_grad


## -----------------------------------------------
## Newton
## -----------------------------------------------

def methode_newton(f,g,h,nb_iter_max,seuil_err,x_init) :
	print("")
	print("--------NEWTON ALGORITHM--------")
	xcour = x_init
	erreur = norm1_gradient(xcour)
	tab_parcours_newton = [xcour]
	condition_f = True
	i=0
	print("iteration ",i , " ; x = ",xcour, " ; norm 1 gradient = ", erreur)
	while (i < nb_iter_max and erreur > seuil_err and condition_f) :
		xsuiv = xcour - np.dot((np.linalg.inv(h(xcour))),g(xcour)) 
		erreur = norm1_gradient(xsuiv)
		i = i+1
		tab_parcours_newton.append(xsuiv)
		condition_f = f(xsuiv) < f(xcour)
		xcour = xsuiv
		print("iteration ",i , " ; x = ",xcour, " ; norm 1 gradient = ", erreur)

	print("---------------")
	print("Stopping condition(s):")
	if (i==nb_iter_max) :
		print("Maximum iteration number reached: ", nb_iter_max)

	if (erreur < seuil_err) :
		print("Gradient norm is below defined threshold")
		print("norm 1 gradient = ", erreur, " < ", seuil_err)

	if (condition_f == False) :
		print("Next iteration does not decrease the cost function value")
		print("Current value f(x) = ", f(xcour), " ; Next value f(x+1) = ", f(xsuiv))

	print("---------------")

	return tab_parcours_newton


