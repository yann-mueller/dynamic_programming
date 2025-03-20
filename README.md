# Mathematical Optimization: Dynamic Programming
Brief introduction to dynamic programming, which is a mathematical optimization method and used to simplify optimization problems with infinite horizon by breaking it down into a sequence of decisions over time.

### Formulation Optimization Problem
For illustrative reasons we use a simplistic T-period (potentially infinite) optimization problem where one has to choose a sequence *{c<sub>1</sub>,...,c<sub>T</sub>}* subject to the period objective function *u(c<sub>t</sub>)* and the constraint *c<sub>t</sub>=y* across all periods:

![grafik](https://github.com/user-attachments/assets/a73ca253-0d8c-44de-9037-aae5a96d2a1a)

*V<sup>T</sup>(y)* is the solution to the given optimization problem and *β* a period discount factor. Such a sequential optimization problem can be re-written into a recursive formulation:

![grafik](https://github.com/user-attachments/assets/63820b7c-1f31-4b74-94b9-000432e418a7)

which is called the **Bellman equation** in which the time indices have been dropped and a new variable *W'* has been introduced with the law of motion *W'=W-c+y* governing the evolution of the constraint across periods.




### Value Function Iteration
