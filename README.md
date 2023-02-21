
[![Python](https://img.shields.io/badge/python-3.10-blue.svg)]()
[![License](https://img.shields.io/pypi/l/cify)](https://opensource.org/licenses/MIT)

<img src=docs/images/cify-main-logo-slogan.png alt="logo"/>

The official repository for the Python CI framework, formerly known as CIFY.
This open-source framework provides easy access to static methods and classes that
simplify the process of nature-inspired optimization in Python. For more information,
consult the Documentation_.

Installation
---

First, it is necessary to make sure you have a working Python 3 environment installed.

To install the latest stable release via `pip`:

```bash
pip install cify
```

Example
---

Below is a simple example that first sets a global seed for all stochastic operations,
then defines an objective function to optimize, optimizes this function using a PSO
algorithm, and finally, outputs the results of the last five iterations.

```python
import cify as ci
from cify.si.pso.algorithm import InertiaWeightPSO

# Set internal seed
ci.set_seed(0)

# 1. Define objective function.
obj_func = ci.get_objective_function('rosenbrock', ci.Optimization.Min)

# 2. Create swarm and metaheuristic.
swarm = ci.get_swarm(50, obj_func=obj_func)
pso = InertiaWeightPSO(obj_func, swarms=[swarm])

# 3. Perform 100 iterations and return the statistics of the last 5.
pso.execute(100)
pso.statistics.tail(5)
```

Contributing
---
If you wish to contribute to CIFY, you'll need to clone the repository and install the necessary
dependencies first. The steps are outlined in a tutorial on the Documentation_ website.
