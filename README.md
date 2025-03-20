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

Constructing a *N x N* flow matrix that contains the flow part for every possible combination of states today (i.e., ***W***) and states tomorrow (i.e., ***W'***)

### Code


## References
De la Fuente, A. (2000). <a href="https://books.google.de/books?hl=en&lr=&id=YyW6V_bNHh4C&oi=fnd&pg=PR11&dq=de+la+fuente+dynamic+programing&ots=FE0SDoXJDk&sig=9k8WMA53WFYE3Vd-n7qQpNs5CO8#v=onepage&q=de%20la%20fuente%20dynamic%20programing&f=false" target="_blank" rel="noopener noreferrer">Mathematical Methods and Models for Economists</a>. Cambridge University Press.
