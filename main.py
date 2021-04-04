import numpy as np 
import matplotlib.pyplot as plt 

### In miliseconds # linspace uses sample sizes
lengthSeconds = 120
milisecondsPerSample = 200 # 10 samples per second
t = np.linspace(0, lengthSeconds, int(lengthSeconds * (1000 / milisecondsPerSample))) #end is exclusive ( [start, end) ).
#print(int(lengthSeconds * (1000 / milisecondsPerSample)))

u = 762

## AP Mk8 stats
As = np.pi * ( 16 * 2.54 / 100 ) ** 2
m = 1225
Cd = 0.25
g = 9.81 # for all calculations just do as negative g 
theta0 = ( 45 ) / 180 * np.pi # put in the bracket as degress, calcs to radians for you
rho = 1.225 # km/cbm, sl right now

## Basic calcs
ux = u * np.cos(theta0)
uy = u * np.sin(theta0)
#print(ux, uy)

## dragless projectile motion
#sx = ux * t
#sy = uy * t - 1/2 * g * np.square(t)

sx = np.zeros(1,)
sy = np.zeros(1,)
sx0, sy0 = 0, 0

## THE FUN PART FUN PART
aaaaaa = False

##Will use iteration because well I dont know any other way to do so
for t0 in t:

    ## air pressure code as well

    dt = milisecondsPerSample / 1000
    theta1 = np.arctan( uy / ux )
    
    v = np.sqrt( uy ** 2 + ux ** 2 )
    FD = 0.5 * rho * v ** 2 * As * Cd
    FDx = FD * np.cos(theta1)
    FDy = FD * np.sin(theta1)

    ax = FDx / m
    ay = FDy / m + g

    dsx = ux * dt - 1/2 * ax * dt ** 2
    dsy = uy * dt - 1/2 * ay * dt ** 2
    #print(sy1, uy * dt, 1/2 * g * dt ** 2)

    sx1 = sx0 + dsx
    sy1 = sy0 + dsy

    vx = ux - ax * dt
    vy = uy - ay * dt
    
    if aaaaaa:
        print("""Variables Calculated for {t0}s.
theta1 = {theta1}
ux = {ux}, uy = {uy}
vx = {vx}, vy = {vy}
ax = {ax}, ay = {ay}
sx = {sx1}, sy = {sy1}
dsx = {dsx}, dsy = {dsy}
""".format(t0 = t0, ux = ux, uy = uy, vx = vx, vy = vy, ax = ax, ay = ay, theta1 = theta1 / np.pi * 180, sx1 = sx1, sy1 = sy1, dsx = dsx, dsy = dsy))

    sx = np.append(sx, sx1)
    sy = np.append(sy, sy1)

    sx0, sy0 = sx1, sy1
    #print(sx0, sy0)

    if sy1 < 0:
        break

    ux, uy = vx, vy

## remove negative ys


#sy = sy [sy >= 0]

#print(sy)
t = t[:len(sy)]
#print(len(sy), len(t))


sx = sx[:len(t)]

print("""
Range at {}°: {:.2f}m
Time to land: {:.2f}s
""".format(theta0 / np.pi * 180, sx[-1], t[-1]))

##
#print(sx, sy)

plt.title("Shell trajectory") 
plt.xlabel("X/m") 
plt.ylabel("Y/m") 
plt.plot(sx, sy, color ="red") 
plt.gca().set_aspect("equal")
plt.show()