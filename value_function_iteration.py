#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import matplotlib.pyplot as plt

# Parameters
beta = 0.95  # Discount factor
r = 0.03     # Interest rate
grid_size = 100  # Number of grid points

# Discretized state space
W = np.linspace(0.1, 10, grid_size)  # Wealth grid from 0.1 to 10

# Utility function: Log utility (with infeasible values set to -inf)
def utility(c):
    return np.log(c) if c > 0 else -np.inf

# Flow matrix computation
Flow = np.zeros((grid_size, grid_size))  # Matrix for flow values

for i in range(grid_size):  # Current wealth
    for j in range(grid_size):  # Future wealth
        c = W[i] * (1 + r) - W[j]  # Consumption formula
        Flow[i, j] = utility(c)  # Compute utility

# Value function iteration
V = np.zeros(grid_size)  # Initial guess for value function
tolerance = 1e-6
max_iterations = 1000
iteration = 0

# Set up the plot
plt.figure(figsize=(8, 5))
plt.xlabel("State Variable [W]")
plt.ylabel("Value Function [V(W)]")
plt.title("Value Function Iteration Progress")

while True:
    iteration += 1
    V_new = np.zeros(grid_size)
    
    for i in range(grid_size):
        V_new[i] = np.max(Flow[i, :] + beta * V)  # Apply Bellman update

    # Plot the current value function without a legend
    plt.plot(W, V_new, alpha=0.5)  # Alpha makes earlier iterations more transparent

    # Check convergence
    if np.max(np.abs(V_new - V)) < tolerance or iteration > max_iterations:
        break
    
    V = V_new  # Update value function

print(f"Converged in {iteration} iterations")

# Finalizing the plot without a legend
plt.show()


# In[ ]:




