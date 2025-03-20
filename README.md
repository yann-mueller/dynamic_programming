# Mathematical Optimization: Dynamic Programming
Brief introduction to dynamic programming, which is a mathematical optimization method and used to simplify optimization problems with infinite horizon by breaking it down into a sequence of decisions over time.

<ins>**Table of Content:**</ins>
- [Formulation Optimization Problem](#formulation-optimization-problem)
- [Value Function Iteration](#value-function-iteration)
- [Code](#code)

### Formulation Optimization Problem
For illustrative reasons we use a simplistic T-period (potentially infinite) optimization problem where one has to choose a sequence *{c<sub>1</sub>,...,c<sub>T</sub>}* subject to the period objective function *u(c<sub>t</sub>)* and the constraint *c<sub>t</sub>=y* across all periods:

![grafik](https://github.com/user-attachments/assets/a73ca253-0d8c-44de-9037-aae5a96d2a1a)

*V<sup>T</sup>(y)* is the solution to the given optimization problem and *β* a period discount factor. Such a sequential optimization problem can be re-written into a recursive formulation:

![grafik](https://github.com/user-attachments/assets/63820b7c-1f31-4b74-94b9-000432e418a7)

which is called the **Bellman equation** in which the time indices have been dropped and a new state variable *W'* has been introduced with the law of motion *W'=W-c+y* governing the evolution of the constraint across periods. For a detailed explanation of this derivation and under which assumption it is valid, we refer to [De la Fuente (2000)](#references).
The main purpose of this repository, however, is to show how the Bellman equation can be solved using numerical methods.


### Value Function Iteration
The Value Function Iteration (VFI) is a numerical solution approach based on a discretization of state variables and an iterative maximization process to find an approximate solution close to the true solution.

**Approach:**

<ins>1) Discretization of State Variables:</ins>

Choose a reasonably sized grid for every state variable. In our example, a *1 x N* vector: ***W** ={w<sub>1</sub>,...,w<sub>N</sub>}*

<ins>2) Construction of Flow Matrix:</ins>

Constructing a *N x N* flow matrix that contains the flow part for every possible combination of states today *i* (i.e., ***W***) and states tomorrow *j* (i.e., ***W'***). Each matrix entry is given by:

![grafik](https://github.com/user-attachments/assets/fabbdb8e-01b1-4a38-a644-98c56edf1302)

The resulting flow matrix looks as follows: (Rows: State tomorrow *W′[j]* - Columns: State today *W[i]*)

![grafik](https://github.com/user-attachments/assets/f6c6cdd8-8242-4dd0-867f-ef11bd2b6cc2)

**Note:** Set utility value for all infeasible points (e.g., c < 0) to a high negative number

<ins>3) Iteration Process:</ins>

To initialize our value function iteration (I = 0), we need an arbitrary initial guess for the value function V<sub>nxn</sub> (often the zero matrix, i.e., V<sup>0</sup> = [0]<sub>nxn</sub>). Next, we compute an *n × n* matrix evaluating the inner part of the Bellman function for all possible values:

![grafik](https://github.com/user-attachments/assets/305c6093-b276-4b67-839b-fbc17d25e4ec)

![grafik](https://github.com/user-attachments/assets/d2d3f660-b26e-4ab2-a901-8c50a3ab0d7d)

![grafik](https://github.com/user-attachments/assets/bac748b6-ca54-4eda-84fd-c734f4ea5d38)

Because the **Contraction Mapping Theorem** applies here, for any initial guess on the value function, *V<sup>I</sup>(W)* will converge to the true value function *V(W)* as *I → ∞*.

<ins>*Visualization:*</ins>

![grafik](https://github.com/user-attachments/assets/6731c207-e4d2-430a-9355-ed567d70b532)

### Code

<ins>1) Discretization of State Variables:</ins>
```
# Parameters
beta = 0.95  # Discount factor
r = 0.03     # Interest rate
grid_size = 100  # Number of grid points

# Discretized state space
W = np.linspace(0.1, 10, grid_size)  # Wealth grid from 0.1 to 10
```

<ins>2) Construction of Flow Matrix:</ins>

```
# Utility function: Log utility (with infeasible values set to -inf)
def utility(c):
    return np.log(c) if c > 0 else -np.inf

# Flow matrix computation
Flow = np.zeros((grid_size, grid_size))  # Matrix for flow values

for i in range(grid_size):  # Current wealth
    for j in range(grid_size):  # Future wealth
        c = W[i] * (1 + r) - W[j]  # Consumption formula
        Flow[i, j] = utility(c)  # Compute utility
```

<ins>3) Iteration Process:</ins>


```
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
```

## References
De la Fuente, A. (2000). <a href="https://books.google.de/books?hl=en&lr=&id=YyW6V_bNHh4C&oi=fnd&pg=PR11&dq=de+la+fuente+dynamic+programing&ots=FE0SDoXJDk&sig=9k8WMA53WFYE3Vd-n7qQpNs5CO8#v=onepage&q=de%20la%20fuente%20dynamic%20programing&f=false" target="_blank" rel="noopener noreferrer">Mathematical Methods and Models for Economists</a>. Cambridge University Press.
