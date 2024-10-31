import numpy as np
import matplotlib.pyplot as plt
# data
Pi1=2000
Pi2=1500
Pi3=1000




n=20




# part 1
Ji1=5*10**-4

q1=np.zeros(n)
Pwf1=np.linspace(Pi1,0,n)

for i in range(n):
    q1[i]=Ji1*(Pi1**2-Pwf1[i]**2)


# part2
q2=np.zeros(n)
Pwf2=np.linspace(Pi2,0,n)
Ji2=Ji1*(Pi2/Pi1)

for i in range(n):
    q2[i]=Ji2*(Pi2**2-Pwf2[i]**2)

# part3

q3 = np.zeros(n)
Pwf3=np.linspace(Pi3,0,n)
Ji3=Ji1*(Pi3/Pi1)
for i in range(n):
    q3[i]=Ji3*(Pi3**2-Pwf3[i]**2)




plt.title("future IPR")
plt.plot(q1,Pwf1)
plt.plot(q2,Pwf2)
plt.plot(q3,Pwf3)
plt.xlabel("Q(stb/day)")
plt.ylabel("Pwf(psig)")
plt.legend(["P=2000", "P=1500","P=1000"], loc="lower right")
plt.savefig('future IPR.png')
plt.show()
