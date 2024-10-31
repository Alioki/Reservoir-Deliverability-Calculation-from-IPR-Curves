import numpy as np
import matplotlib.pyplot as plt
# data
phi=0.19
t=1
t=t*30*24
k=8.2
h=53
Pe=5651
Pb=5651
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
qMax1=J1*Pe/1.8
for i in range(n):
    q1[i]=qMax1*(1-0.2*(Pwf1[i]/Pe)-0.8*(Pwf1[i]/Pe)**2)

print(J1)

plt.title("Vogel’s equation IPR1 (transient flow)")
plt.plot(q1,Pwf1)
plt.xlabel("Q")
plt.ylabel("Pwf")
plt.savefig('Vogel’s equation transient flow.png')
plt.show()

# part2
q2=np.zeros(n)
Pwf2=np.linspace(Pe,Pb,n)
J2=k*h/(141.2*Bo*mu*(np.log(re/rw)+s))
qMax2=J2*Pe/1.8

for i in range(n):
    q2[i]=qMax2*(1-0.2*(Pwf2[i]/Pe)-0.8*(Pwf2[i]/Pe)**2)

print(J2)
plt.title("Vogel’s equation IPR2(steady state flow)")
plt.plot(q2,Pwf2)
plt.xlabel("Q")
plt.ylabel("Pwf")
plt.savefig('Vogel’s equation steady state flow.png')
plt.show()
# part3
q3=np.zeros(n)
Pwf3=np.linspace(Pe,Pb,n)
J3=k*h/(141.2*Bo*mu*(np.log(re/rw)+s-0.75))
qMax3=J3*Pe/1.8

for i in range(n):
    q3[i]=qMax3*(1-0.2*(Pwf3[i]/Pe)-0.8*(Pwf3[i]/Pe)**2)


print(J3)

plt.title("Vogel’s equation IPR3(pseudosteady state flow)")
plt.plot(q3,Pwf3)
plt.xlabel("Q")
plt.ylabel("Pwf")
plt.savefig('Vogel’s equation pseudosteady state flow.png')
plt.show()
