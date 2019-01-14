m1 = 1		
m2 = 100000000

# Mass of object initially at rest : m1
# Mass of object moving initially : m2

initvector = [0 ,1]
# [Velocity of m1, Velocity of m2)

currentvector = initvector[:]

def mulA(vec):
	msum = (m1 + m2)
	a11 = (m1 - m2)/float(msum)
	a12 = 2*m2/float(msum)
	a21 = 2*m1/float(msum)
	a22 = (m2 - m1)/float(msum)


	v1 = a11*vec[0] + a12*vec[1]
	v2 = a21*vec[0] + a22*vec[1]

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

while(checkspeeds(currentvector[0], currentvector[1])):
	
	if (mtype == 'A'):
		nvec = mulA(currentvector)
		currentvector = nvec[:]
		collisioncount = collisioncount + 1
		mtype = 'W'
	elif (mtype == 'W'):
		nvec = mulW(currentvector)
		currentvector = nvec[:]
		collisioncount = collisioncount + 1
		mtype = 'A'

print("Mass at rest initally : %d" % m1)
print("Mass at moving initally : %d" % m2)
print("Total number of collisions of the masses : %f" % collisioncount)