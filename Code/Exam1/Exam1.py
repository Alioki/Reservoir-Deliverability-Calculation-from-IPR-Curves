import numpy as np
import matplotlib.pyplot as plt
# data
phi=0.19
t=1
t=t*30*24
k=8.2
h=53
Pe=5651
Pb=50
Bo=1.1
mu=1.7
Ct= 0.0000129
A=640
re=2980
rw=0.328
s=0


n=20




# part 1
q1=np.zeros(n)
Pwf1=np.linspace(Pe,Pb,n)
J1=k*h/(162.6*mu*Bo*(np.log10(t)+np.log10(k/(phi*mu*Ct*(rw**2)))-3.23))
for i in range(n):
    q1[i]=J1*(Pe-Pwf1[i])

print(J1)

plt.title("IPR1 (transient flow)")
plt.plot(q1,Pwf1)
plt.xlabel("Q")
plt.ylabel("Pwf")
plt.savefig('transient flow.png')
plt.show()

# part2
q2=np.zeros(n)
Pwf2=np.linspace(Pe,Pb,n)

J2=k*h/(141.2*Bo*mu*(np.log(re/rw)+s))

for i in range(n):
    q2[i]=J2*(Pe-Pwf2[i])

print(J2)
plt.title("IPR2(steady state flow)")
plt.plot(q2,Pwf2)
plt.xlabel("Q")
plt.ylabel("Pwf")
plt.savefig('steady state flow.png')
plt.show()
# part3
q3=np.zeros(n)
Pwf3=np.linspace(Pe,Pb,n)

J3=k*h/(141.2*Bo*mu*(np.log(re/rw)+s-0.75))
for i in range(n):
    q3[i]=J3*(Pe-Pwf3[i])


print(J3)

plt.title("IPR3(pseudosteady state flow)")
plt.plot(q3,Pwf3)
plt.xlabel("Q")
plt.ylabel("Pwf")
plt.savefig('pseudosteady state flow.png')
plt.show()
