import numpy as np

from cify import ObjectiveFunction, Optimization, Task, set_seed
from cify.ga import GA

# 1. Set internal seed for stochastic operations.
set_seed(0)

# 2. Define an objective function.
bounds = [0.0, 1.0]
dim = 10
sphere = ObjectiveFunction(lambda vector: np.sum(vector ** 2),
                          bounds,
                          dim,
                          Optimization.Min,
                          "sphere")

# 3. Create an algorithm.
ga = GA(30, sphere)

# 4. Define a performance metric
def metric(ga: GA, f: ObjectiveFunction) -> float:
   return sorted(ga.individuals)[0]

# 5. Create a task to run the algorithm.
task = Task(ga,
           sphere,
           max_iterations=1000,
           log_iterations=100,
           metrics=[("best_of_value", metric)])

# 6. Execute
task.run()
print(task.results["best_of_value"][-1])