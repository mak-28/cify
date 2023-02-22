.. image:: images/cify-main-logo-slogan.png
   :width: 1000
   :alt: CIFY
   :align: center

CIFY is a framework for computational intelligence algorithms written in
Python. The goal of the project is to create a framework that allows users to
easily and reliably implement nature-inspired metaheuristics. The framework
provides a set of very simple abstractions for implementing metaheuristics,
objective functions, running experiments and collecting results.

The guiding principles of the project are: 

- **Low barrier of entry**. Reading the tutorial or looking at the examples is
  all you should need to start working with CIFY.
- **Reproducibility**. Experiments with stochastic operations should be easily
  reproducible.
- **Speed**. Computational time should be kept to a minimum.
- **Tests and documentation**. All code should be thoroughly tested and
  documented.

Quickstart
----------

Install cify using pip

::

   pip install cify

or clone the repo and install cify to your environment using

::

   cd CIFY
   pip install -e .

Using the following example to get started or refer to the documentation for more
details.

::

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


Contributing
------------

CIFY is an open-source project, and it depends its users to continually
improve. We are very pleased that you would like to help!

If you notice a bug, have an idea for a feature, or have a question about the
code, please don't hesitate to open an issue. Many features come about simply
by the asking of a question, or requesting a feature directly.

If you are unsure as to where to start take a look at the existing issues or
reach out directly. Improving documentation, adding examples and adding tests
are all good (and highly appreciated) ways to start contributing to CIFY.

If your contribution has been derived from or inspired by other work, please
state this in its docstring and provide proper attribution. When possible,
include the original authors' names and a link to the original work.

To setup your development environment for CIFY, please follow the commands
below.::

    git clone https://github.com/KyleErwin/cify
    cd cify
    python3 -m venv venv
    source venv/bin/activate
    pip install -r dev-requirements.txt
    pre-commit install

To build the docs, please install `pandoc <https://pandoc.org/installing.html>`_.

Lastly, please run ``pytest`` to ensure all of your changes pass the tests.

Contents
--------

.. toctree::
   :maxdepth: 2

   api
   tutorial
