import numpy as np
import matplot.lib 
'''
dv2(t)/R = dv2(t)/dt C
v2 = 0
v2(h) = (v1-v2(0))/RC*h + v2(0)
v(2h) = (v1-v2(h))/RC*h + v2(h)

Init Conditions=>
v2(0) = 0 ; t = [0, 0.5] ; v1 = 1
v2(0.5) = 1 ; t = [0.5, 1] ; v1=0
RC= 0.1
'''
RC = 0.1
t1 = np.linspace(0,0.5,1000)
t2 = np.linspace(0.5, 1, 1000)
v1 = [1, 0]
v2 = [0, 0.5]
v2_output = []
step_value = [0, 1] #Random step value I think
for i in rangeof(5): #wip later
  v2_output.append(((v1[index] - v2[index])/RC*8)v2[index])
fig.

fig.plot(t1,v2_output)
  
