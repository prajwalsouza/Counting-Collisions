from matplotlib import pyplot as plt
import math

m1 = 1		
m2 = 10000
# Mass of object initially at rest : m1
# Mass of object moving initially : m2

initvector = [0, 0.1] # in units of speed of light (ex. 0.02c)
# [Velocity of m1, Velocity of m2) 

currentvector = initvector[:]

velocityvalues = []

def mulA(vec):
	msum = (m1 + m2)
	a11 = (m1 - m2)/float(msum)
	a12 = 2*m2/float(msum)
	a21 = 2*m1/float(msum)
	a22 = (m2 - m1)/float(msum)


	v1 = a11*vec[0] + a12*vec[1]
	v2 = a21*vec[0] + a22*vec[1]

	return [v1, v2]


# Calculation for Special Relativity

def mulASR(vec):
	u1 = vec[0]
	u2 = vec[1]
	c = 1

	# The following equations were taken from https://en.wikipedia.org/wiki/Elastic_collision#One-dimensional_relativistic 

	Z = math.sqrt((1 - ((u1/c)**2))*(1 - ((u2/c)**2)))

	a1N = (2*m1*m2*(c**2)*u2*Z) + (2*(m2**2)*(c**2)*u2) - (((m1**2) + (m2**2))*u1*(u2**2)) + (((m1**2) - (m2**2))*u1*(c**2)) 
	a2N = (2*m1*m2*(c**2)*u1*Z) + (2*(m1**2)*(c**2)*u1) - (((m1**2) + (m2**2))*u2*(u1**2)) + (((m2**2) - (m1**2))*u2*(c**2))

	a1D = (2*m1*m2*(c**2)*Z) - (2*(m2**2)*(u1)*u2) - (((m1**2) - (m2**2))*(u2**2)) + (((m1**2) + (m2**2))*(c**2)) 
	a2D = (2*m1*m2*(c**2)*Z) - (2*(m1**2)*(u1)*u2) - (((m2**2) - (m1**2))*(u1**2)) + (((m1**2) + (m2**2))*(c**2)) 
	

	v1 = a1N/float(a1D)
	v2 = a2N/float(a2D)

	return [v1, v2]

def mulW(vec):
	v1 = (-1)*vec[0]
	v2 = vec[1]
	return [v1, v2]

def checkspeeds(speed1, speed2):
	ret = True
	if (speed1 <= 0 and speed2 <=0):
		if(abs(speed2) >= abs(speed1)):
			ret = False

	return ret

collisioncount = 0

mtype = 'A'

velocityvalues.append(currentvector)

while(checkspeeds(currentvector[0], currentvector[1])):
	if (mtype == 'A'):
		nvec = mulASR(currentvector)
		currentvector = nvec[:]
		collisioncount = collisioncount + 1
		mtype = 'W'
	elif (mtype == 'W'):
		nvec = mulW(currentvector)
		currentvector = nvec[:]
		collisioncount = collisioncount + 1
		mtype = 'A'
	velocityvalues.append(currentvector)


print("Mass at rest initally : %d" % m1)
print("Mass moving initally : %d" % m2)
print("Total number of collisions of the masses : %d" % collisioncount)


plt.plot([velocityvalue[0] for velocityvalue in velocityvalues] ,[velocityvalue[1] for velocityvalue in velocityvalues],'.')
plt.plot([velocityvalue[0] for velocityvalue in velocityvalues] ,[velocityvalue[1] for velocityvalue in velocityvalues])

plt.show()