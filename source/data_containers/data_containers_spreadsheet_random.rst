.. _data_containers_spreadsheet_random:

Generate Random Values
======================

.. contents::

Overview
--------

LabPlot can fill columns with random values drawn from various statistical distributions. This feature uses the GNU Scientific Library (GSL) random number generation functions and supports 36 different probability distributions including both continuous and discrete distributions.

Random values can be generated for numeric column types (Double, Integer, BigInt) and the distribution parameters are stored with the column, allowing regeneration with the same settings.

How to Generate Random Values
------------------------------

1. Select one or more columns in the spreadsheet
2. Right-click → **Fill with Random Values** (or from the menu)
3. Choose a distribution from the dropdown list
4. Configure the distribution parameters
5. Optionally set a seed for reproducible results
6. Click **Generate**

.. note::
   If you specify a seed value, the same sequence of random numbers will be generated each time. This is useful for reproducible results. If no seed is specified, the current timestamp is used.

Available Distributions
-----------------------

Continuous Distributions
~~~~~~~~~~~~~~~~~~~~~~~~

Gaussian (Normal)
^^^^^^^^^^^^^^^^^

The normal distribution with mean μ and standard deviation σ.

**Parameters:**

* μ (mu) - Mean/location parameter
* σ (sigma) - Standard deviation (scale parameter)

**Use cases:** Natural phenomena, measurement errors, central limit theorem applications

**Example values:**

* Standard normal: μ = 0, σ = 1
* Custom: μ = 100, σ = 15 (e.g., IQ scores)

Exponential
^^^^^^^^^^^

Models time between events in a Poisson process.

**Parameters:**

* λ (lambda) - Rate parameter (1/mean)
* μ (mu) - Location shift

**Use cases:** Waiting times, decay processes, reliability analysis

Laplace (Double Exponential)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Symmetric exponential distribution around the mean.

**Parameters:**

* μ (mu) - Location parameter
* σ (sigma) - Scale parameter

**Use cases:** Financial returns, signal processing, robust statistics

Cauchy (Lorentz)
^^^^^^^^^^^^^^^^

Heavy-tailed distribution (no defined mean or variance).

**Parameters:**

* γ (gamma) - Scale parameter
* μ (mu) - Location parameter

**Use cases:** Resonance phenomena, statistical outliers

Rayleigh
^^^^^^^^

Models magnitude of a 2D random vector with independent Gaussian components.

**Parameters:**

* σ (sigma) - Scale parameter

**Use cases:** Wind speed, wave heights, communication systems

Gamma
^^^^^

Flexible continuous distribution for positive values.

**Parameters:**

* k - Shape parameter (α)
* θ (theta) - Scale parameter (β)

**Use cases:** Waiting times, rainfall amounts, insurance claims

**Special cases:**

* k = 1: Exponential distribution
* k = n/2, θ = 2: Chi-squared distribution with n degrees of freedom

Weibull
^^^^^^^

Models failure rates and lifetime analysis.

**Parameters:**

* λ (lambda) - Scale parameter
* k - Shape parameter

**Use cases:** Reliability engineering, survival analysis, wind speed modeling

Beta
^^^^

Bounded distribution on [0, 1].

**Parameters:**

* α (alpha) - First shape parameter
* β (beta) - Second shape parameter

**Use cases:** Probabilities, proportions, Bayesian priors

Lognormal
^^^^^^^^^

Distribution of a variable whose logarithm is normally distributed.

**Parameters:**

* μ (mu) - Mean of log(X)
* σ (sigma) - Standard deviation of log(X)

**Use cases:** Income distributions, particle sizes, stock prices

Student's t-distribution
^^^^^^^^^^^^^^^^^^^^^^^^^

Heavy-tailed distribution, reduces to normal as degrees of freedom increase.

**Parameters:**

* ν (nu) - Degrees of freedom

**Use cases:** Small sample statistics, robust inference

Chi-squared
^^^^^^^^^^^

Distribution of sum of squared standard normal variables.

**Parameters:**

* k - Degrees of freedom

**Use cases:** Goodness-of-fit tests, variance estimation

F-distribution
^^^^^^^^^^^^^^

Ratio of two chi-squared distributions.

**Parameters:**

* d₁ - Numerator degrees of freedom
* d₂ - Denominator degrees of freedom

**Use cases:** ANOVA, regression analysis

Logistic
^^^^^^^^

S-shaped distribution similar to normal but with heavier tails.

**Parameters:**

* μ (mu) - Location parameter
* s - Scale parameter

**Use cases:** Growth models, neural networks, classification

Pareto
^^^^^^

Power-law distribution.

**Parameters:**

* a - Shape parameter (tail index)
* b - Scale parameter (minimum value)

**Use cases:** Income distribution, city sizes, network degrees

Gumbel (Type I and Type II)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Extreme value distributions.

**Parameters:**

* μ (mu) - Location parameter
* σ (sigma) - Scale parameter

**Use cases:** Maximum/minimum values, flood analysis, material strength

Flat (Uniform)
^^^^^^^^^^^^^^

Constant probability over an interval.

**Parameters:**

* a - Lower bound
* b - Upper bound

**Use cases:** Random sampling, Monte Carlo simulations

Discrete Distributions
~~~~~~~~~~~~~~~~~~~~~~

Poisson
^^^^^^^

Models count of events in fixed interval.

**Parameters:**

* λ (lambda) - Average rate (mean = variance)

**Use cases:** Call arrivals, defect counts, rare events

**Example values:**

* Low rate: λ = 2 (average 2 events)
* High rate: λ = 20 (average 20 events)

Binomial
^^^^^^^^

Number of successes in n independent trials.

**Parameters:**

* p - Success probability (0 < p < 1)
* n - Number of trials

**Use cases:** Quality control, surveys, coin flips

**Example:** n = 10, p = 0.3 (expect ~3 successes)

Bernoulli
^^^^^^^^^

Single trial with two outcomes (special case of binomial with n=1).

**Parameters:**

* p - Success probability

**Use cases:** Yes/no decisions, pass/fail tests

Geometric
^^^^^^^^^

Number of trials until first success.

**Parameters:**

* p - Success probability per trial

**Use cases:** Waiting time for first event

Negative Binomial (Pascal)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Number of failures before r successes.

**Parameters:**

* p - Success probability
* r - Number of successes to wait for

**Use cases:** Overdispersed count data

Hypergeometric
^^^^^^^^^^^^^^

Sampling without replacement.

**Parameters:**

* N - Population size
* K - Number of success states in population
* n - Number of draws

**Use cases:** Quality control sampling, card games

Logarithmic
^^^^^^^^^^^

Logarithmic series distribution.

**Parameters:**

* p - Parameter (0 < p < 1)

**Use cases:** Species abundance, network analysis

Specialized Distributions
~~~~~~~~~~~~~~~~~~~~~~~~~

Landau
^^^^^^

Describes energy loss of charged particles passing through matter.

**Parameters:** None (parameter-free)

**Use cases:** Particle physics

Lévy Alpha-Stable
^^^^^^^^^^^^^^^^^

Generalized central limit theorem distributions.

**Parameters:**

* c - Scale parameter
* α (alpha) - Stability parameter (0 < α ≤ 2)

**Use cases:** Financial modeling, complex systems

Lévy Skew Alpha-Stable
^^^^^^^^^^^^^^^^^^^^^^^

Asymmetric version of Lévy stable distributions.

**Parameters:**

* c - Scale parameter
* α (alpha) - Stability parameter
* β (beta) - Skewness parameter (-1 ≤ β ≤ 1)

Gaussian Tail
^^^^^^^^^^^^^

Truncated Gaussian distribution (only values beyond a threshold).

**Parameters:**

* μ (mu) - Mean
* σ (sigma) - Standard deviation
* a - Lower threshold (tail starts at)

**Use cases:** Extreme value analysis, truncated data

Rayleigh Tail
^^^^^^^^^^^^^

Truncated Rayleigh distribution.

**Parameters:**

* μ (mu) - Location shift
* σ (sigma) - Scale
* a - Lower threshold

Exponential Power
^^^^^^^^^^^^^^^^^

Generalization of Gaussian and Laplace distributions.

**Parameters:**

* μ (mu) - Location
* σ (sigma) - Scale
* b - Shape (b=2: Gaussian, b=1: Laplace)

Maxwell-Boltzmann
^^^^^^^^^^^^^^^^^

Speed distribution of particles in ideal gas.

**Parameters:**

* a - Temperature-related scale parameter

**Use cases:** Statistical mechanics, molecular dynamics

Triangular
^^^^^^^^^^

Simple distribution with linear increase and decrease.

**Parameters:**

* a - Lower limit
* b - Upper limit
* c - Mode (peak location)

**Use cases:** Rough approximations, risk analysis when little data available

Sech (Hyperbolic Secant)
^^^^^^^^^^^^^^^^^^^^^^^^^

Symmetric distribution with specific tail behavior.

**Parameters:** Scale and location parameters

Lévy
^^^^

Special case of Lévy alpha-stable (α = 0.5).

**Parameters:**

* c - Scale parameter
* μ (mu) - Location

Fréchet
^^^^^^^

Type II extreme value distribution.

**Parameters:**

* α (alpha) - Shape
* s - Scale
* m - Location

Tips and Best Practices
------------------------

Choosing a Distribution
~~~~~~~~~~~~~~~~~~~~~~~

* **Gaussian/Normal**: Default choice for continuous data with symmetric bell shape
* **Uniform**: When all values in a range are equally likely
* **Exponential**: For waiting times or intervals between events
* **Poisson**: For count data (number of events)
* **Binomial**: For success/failure trials with fixed probability

Seed Values
~~~~~~~~~~~

* **Reproducible results**: Use a fixed seed (e.g., 12345)
* **Different sequences**: Change the seed value
* **Random sequences**: Leave seed empty (uses current timestamp)

Parameter Selection
~~~~~~~~~~~~~~~~~~~

* Check the distribution formula and parameter meanings
* Start with standard parameter values (e.g., μ=0, σ=1 for Gaussian)
* Adjust parameters to match your data characteristics
* Use preview/statistics to verify the generated distribution

Common Patterns
~~~~~~~~~~~~~~~

**Simulating measurement errors:**

.. code-block:: none

   Distribution: Gaussian
   μ = 0 (centered)
   σ = 0.1 (small errors)

**Generating test data in a range:**

.. code-block:: none

   Distribution: Flat (Uniform)
   a = 0 (minimum)
   b = 100 (maximum)

**Simulating arrival times:**

.. code-block:: none

   Distribution: Poisson
   λ = 5 (average 5 arrivals per time unit)

**Adding realistic noise:**

.. code-block:: none

   Distribution: Laplace
   μ = 0
   σ = 1 (heavier tails than Gaussian)

Column Mode Compatibility
~~~~~~~~~~~~~~~~~~~~~~~~~

* **Double columns**: Accept all distributions with full precision
* **Integer columns**: Values are rounded to nearest integer
* **BigInt columns**: Values are rounded to nearest integer (wider range)
* **Text/DateTime columns**: Cannot be filled with random values

Multiple Columns
~~~~~~~~~~~~~~~~

When multiple columns are selected, each column receives **independent** random values from the same distribution. The values are not correlated unless you generate them in one column and copy/transform for others.

Regeneration
~~~~~~~~~~~~

The distribution parameters are stored with the column. You can regenerate with the same settings by:

1. Select the column
2. Right-click → **Fill with Random Values**
3. The dialog shows the previous distribution and parameters
4. Click **Generate** to create a new sequence

Additional Resources
--------------------

* `GSL Random Number Distributions Documentation <https://www.gnu.org/software/gsl/doc/html/randist.html>`_
* Distribution formulas and properties are shown in the dialog
* For reproducible research, always document the seed value used
