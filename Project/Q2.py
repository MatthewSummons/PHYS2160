##

##

import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as sp
from scipy.misc import derivative

# g is the gravitaional acceleartion, l is the length of the pendulum
g, l = 9.81, 1.0

# Initial angle of the pendulum (radians)
theta_0 = 55 * np.pi /180

STEPS = int(1e5)


def dr_dt(r, t):
  '''The vector function for the set of first oder ODEs for the pendulum'''
  theta, omega = r  # The vector r = <theta, omega>
  # dtheta_dt = omega, domega_dt = -g/l * sin(theta)
  return np.array([omega, (-g/l) * np.sin(theta)])


def theta_a(t, theta_m, delta):
  '''The function for the analytic solution of a linear pendulum under gravity (g) with length (l)'''
  return theta_m * np.cos(np.sqrt(g/l)* t + delta)


def period_function(x, theta_m):
  return 1 / np.sqrt((np.cos(x) - np.cos(theta_m)))


def find_period(theta_m) -> float:
  
  Period = 4 * np.sqrt(l / (2*g)) * sp.quad(period_function, 0, theta_m, args=(theta_m))[0]
  return Period
  

def main():
  # The time interval for which we plot the solution of the ODE
  start, end = 0, 10

  # The time steps for the numerical solution
  t = np.linspace(start, end, STEPS)
  
  # The initial conditions for the ODE (r = <theta, omega> )
  r0 = np.array([theta_0, 0])  # Note that (-2π ≤ theta ≤ 2π) !!!
  
  # Solve the ODE numerically using scipy.integrate.odeint
  sol = sp.odeint(dr_dt,r0, t)

  theta_of_t = sol[:, 0]
  omega_of_t = sol[:, 1]

  # Part (a)
  # Numerical solution of non-linear ODE
  # Plot the function theta(t) for the initial condition theta = 0
  fig1, axs1 = plt.subplots()

  axs1.plot(t, theta_of_t, label="Numerical Non-Linear  $\\theta(t)$")
  axs1.plot(t, theta_a(t, r0[0], 0), label="Analytic Linear Solution $\\theta_a(t)$")
  
  axs1.set_xlabel("Time ($t$)")
  axs1.set_ylabel("Angular Displacement ($\\theta$)")
  
  axs1.legend(loc='best')
  axs1.set_title(f"Solutions for Linear & Non-linear Pendulums \n $\\theta(0) = {r0[0]}$, $\\omega(0) = 0$")


  # Part (b)
  # Phase Plane Diagram
  # Plot the phase diagram for the linear and non-linear pendulum
  fig2, axs2 = plt.subplots()
  
  axs2.plot(theta_of_t, omega_of_t, label="Numerical Non-Linear  $\\omega(t)$")
  
  analytic, dtheta_dt = theta_a(t, r0[0], 0), derivative(theta_a, t, dx=1e-6, args=(r0[0], 0))
  axs2.plot(analytic, dtheta_dt, label="Analytic Linear Solution $\omega_a(t)$")
  
  axs2.set_xlabel("Angular Displacement ($\\theta$)")
  axs2.set_ylabel("Angular Velocity ($\\omega$)")
  axs2.legend(loc='best', frameon=False)
  axs2.set_title(f"Phase Diagram for Linear & Non-Linear Pendulums\n $\\theta(0) = {r0[0]}$, $\\omega(0) = 0$")


  # Part (c)
  # Ration of True Period to Small Angle Period


  Periods_Array = np.zeros(90)
  for theta_m in range(1, 90+1):
    T = find_period(theta_m * np.pi/180)
    Periods_Array[theta_m-1] = T

    print(f"The period for the angle {theta_m} is {T}")
  
  
  small_angle_T = 2 * np.pi * np.sqrt(l / g)
  
  ratio = Periods_Array / small_angle_T

  fig3, axs3 = plt.subplots()

  axs3.plot(np.arange(1, 91), ratio, label="Ratio $T:T_s$")

  axs3.set_xticks(np.arange(0, 91, 10))
  axs3.set_xticklabels(np.arange(0, 91, 10))
  
  axs3.set_xlabel("Oscillation Amplitude ($\\theta^{\\circ}_m$)")
  axs3.set_ylabel("Ratio $T:T_s$")
  axs3.legend(loc='best', frameon=False)
  axs3.set_title("True Period to Small Angle Period Ratios \n for Different Displacement Angles $(T:T_s)$")

  plt.show()


main()