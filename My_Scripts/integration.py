import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.integrate import solve_ivp

a = 3
b = 5
def dvdt(t, v):
    return a*v**2-b
v0 = 0

t = np.linspace(0, 1, 100)
sol_m1 = odeint(dvdt, y0 = v0, t = t, tfirst=True)
print(sol_m1)
v_sol_m1 = sol_m1.T[0]

plt.plot(t, v_sol_m1)
plt.show()