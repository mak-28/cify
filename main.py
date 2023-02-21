import cify
from cify.pso.algorithm import InertiaWeightPSO

# 1. Set internal seed for stochastic operations.
set_seed(0)

# 2. Call or define an objective function.
obj_func = ci.get_objective_function('rosenbrock', ci.Optimization.Min)

# 3. Create swarm and algorithm.
pso = InertiaWeightPSO(obj_func, swarms=[ci.get_swarm(10, obj_func=obj_func)])

# 4. Execute
pso.execute(n_iterations=100)

# Examine results
pso.statistics.tail(5)