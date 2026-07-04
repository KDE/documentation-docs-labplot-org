.. _data_containers_spreadsheet_formulas:

Column Formulas
===================

.. contents::

Overview
------------------

Column formulas allow you to generate column values dynamically based on mathematical expressions. Formulas can reference other columns, use built-in functions, and automatically update when source data changes. The formula system provides over 600 functions from the GNU Scientific Library (GSL), including mathematical, statistical, logical, and special functions.

Basic Syntax
------------------

Creating a Formula
~~~~~~~~~~~~~~~~~~

To create a formula column:

1. Right-click on a column header → **Formula**
2. Enter your formula expression
3. Map variable names to actual columns
4. Enable **Auto Update** to recalculate automatically

.. note::
   Columns can be referenced from any spreadsheet in the project, not just the current one. When mapping variables, you can select columns from different spreadsheets.

Syntax Rules
~~~~~~~~~~~~

* **Variables**: Reference other columns (e.g., ``x``, ``y``, ``data``)
* **Operators**: ``+``, ``-``, ``*``, ``/``, ``^`` (power)
* **Functions**: Use semicolon ``;`` to separate arguments (not comma)
* **Constants**: ``pi``, ``e``, and others from GSL
* **Cross-spreadsheet**: Variables can reference columns from any spreadsheet in the project

Examples
~~~~~~~~~~~~~~

**Basic arithmetic:**

.. code-block:: none

   x * 2 + y

**Distance calculation:**

.. code-block:: none

   sqrt(x^2 + y^2)

**Conditional logic:**

.. code-block:: none

   if(temperature > 0; 1; 0)

**Normalization (z-score):**

.. code-block:: none

   (x - mean(x)) / stdev(x)

**Moving average:**

.. code-block:: none

   sma(10; temperature)

**Date extraction:**

.. code-block:: none

   year(date_column)

**Trigonometry with degree conversion:**

.. code-block:: none

   sin(angle_degrees * pi / 180)

**Cross-spreadsheet reference:**

.. code-block:: none

   # Variables can reference columns from different spreadsheets
   # Example: temperature from Spreadsheet1 minus baseline from Spreadsheet2
   temp - baseline

   # Where 'temp' is mapped to: Project/Spreadsheet1/Temperature
   # And 'baseline' is mapped to: Project/Spreadsheet2/Baseline

Available Functions
--------------------

Standard Mathematical Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 50 30

   * - Function
     - Description
     - Example
   * - ``sqrt(x)``
     - Square root
     - ``sqrt(16)`` → 4
   * - ``pow(x; y)``
     - Power x\ :sup:`y`
     - ``pow(2; 8)`` → 256
   * - ``exp(x)``
     - Exponential e\ :sup:`x`
     - ``exp(1)`` → 2.718...
   * - ``log(x)``
     - Natural logarithm
     - ``log(e)`` → 1
   * - ``log10(x)``
     - Base-10 logarithm
     - ``log10(100)`` → 2
   * - ``abs(x)``, ``fabs(x)``
     - Absolute value
     - ``fabs(-5)`` → 5
   * - ``ceil(x)``
     - Round up
     - ``ceil(3.2)`` → 4
   * - ``floor(x)``
     - Round down
     - ``floor(3.8)`` → 3
   * - ``round(x)``
     - Round to nearest
     - ``round(3.5)`` → 4
   * - ``roundn(x; n)``
     - Round to n decimals
     - ``roundn(3.14159; 2)`` → 3.14
   * - ``sgn(x)``
     - Sign (-1, 0, 1)
     - ``sgn(-5)`` → -1

Comparison and Logical Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 25 50 25

   * - Function
     - Description
     - Returns
   * - ``if(cond; true_val; false_val)``
     - Conditional expression
     - Value based on condition
   * - ``and(a; b)``
     - Logical AND
     - 1.0 or 0.0
   * - ``or(a; b)``
     - Logical OR
     - 1.0 or 0.0
   * - ``not(a)``
     - Logical NOT
     - 1.0 or 0.0
   * - ``equal(a; b)``
     - Equality test
     - 1.0 or 0.0
   * - ``greaterThan(a; b)``
     - Greater than
     - 1.0 or 0.0
   * - ``lessThan(a; b)``
     - Less than
     - 1.0 or 0.0
   * - ``between(x; min; max)``
     - In range (exclusive)
     - 1.0 or 0.0
   * - ``between_inc(x; min; max)``
     - In range (inclusive)
     - 1.0 or 0.0

.. note::
   You can also use operators: ``>``, ``>=``, ``<``, ``<=``, ``==``, ``!=``

**Example: Nested conditions**

.. code-block:: none

   if(score >= 80; 2; if(score >= 60; 1; 0))

Column Statistics
~~~~~~~~~~~~~~~~~

Compute statistics over entire columns. These return a constant value repeated for all rows.

.. list-table::
   :header-rows: 1
   :widths: 20 50 30

   * - Function
     - Description
     - Example
   * - ``size(col)``
     - Number of values
     - ``size(x)``
   * - ``sum(col)``
     - Sum of values
     - ``sum(x)``
   * - ``min(col)``
     - Minimum value
     - ``min(x)``
   * - ``max(col)``
     - Maximum value
     - ``max(x)``
   * - ``mean(col)``
     - Arithmetic mean
     - ``mean(x)``
   * - ``median(col)``
     - Median
     - ``median(x)``
   * - ``stdev(col)``
     - Standard deviation
     - ``stdev(x)``
   * - ``var(col)``
     - Variance
     - ``var(x)``
   * - ``quartile1(col)``
     - First quartile (Q1)
     - ``quartile1(x)``
   * - ``quartile3(col)``
     - Third quartile (Q3)
     - ``quartile3(x)``
   * - ``iqr(col)``
     - Interquartile range
     - ``iqr(x)``
   * - ``percentile(p; col)``
     - p-th percentile
     - ``percentile(95; x)``
   * - ``skew(col)``
     - Skewness
     - ``skew(x)``
   * - ``kurt(col)``
     - Kurtosis
     - ``kurt(x)``

**Example: Detect outliers**

.. code-block:: none

   if(fabs(x - mean(x)) > 2 * stdev(x); 1; 0)

Moving Statistics
~~~~~~~~~~~~~~~~~

Operate on sliding windows of data.

.. list-table::
   :header-rows: 1
   :widths: 30 50 20

   * - Function
     - Description
     - Example
   * - ``sma(window; col)``
     - Simple moving average
     - ``sma(5; x)``
   * - ``smmin(window; col)``
     - Moving minimum
     - ``smmin(5; x)``
   * - ``smmax(window; col)``
     - Moving maximum
     - ``smmax(5; x)``
   * - ``smr(window; col)``
     - Moving range
     - ``smr(5; x)``

Cell Access Functions
^^^^^^^^^^^^^^^^^^^^^

Access individual cell values for lag/lead operations and custom calculations.

.. list-table::
   :header-rows: 1
   :widths: 35 50 15

   * - Function
     - Description
     - Args
   * - ``cell(index; col)``
     - Access cell at index in another column
     - 2
   * - ``cell_with_default(index; default; col)``
     - Access cell with default if out of range
     - 3
   * - ``cell_curr_column(index)``
     - Access cell in current column
     - 1
   * - ``cell_curr_column_with_default(index; default)``
     - Access cell in current column with default
     - 2

**Examples:**

.. code-block:: none

   # Access previous value (lag 1)
   cell_curr_column_with_default(i-1; 0)

   # Access next value (lead 1)
   cell_curr_column_with_default(i+1; 0)

   # Difference from previous value
   x - cell_curr_column_with_default(i-1; x)

   # Access another column at offset
   cell_with_default(i-2; 0; temperature)

   # Moving difference (current minus 5 rows back)
   x - cell_curr_column_with_default(i-5; x)

Trigonometric Functions
~~~~~~~~~~~~~~~~~~~~~~~

All angles in radians. Available functions: ``sin``, ``cos``, ``tan``, ``asin``, ``acos``, ``atan``, ``atan2``, ``sinh``, ``cosh``, ``tanh``, ``asinh``, ``acosh``, ``atanh``, and many more.

**Example: Convert degrees to radians**

.. code-block:: none

   sin(angle_degrees * pi / 180)

**Example: Hypotenuse**

.. code-block:: none

   hypot(x; y)  # Equivalent to sqrt(x^2 + y^2)

Datetime Functions
~~~~~~~~~~~~~~~~~~

Work with dates and times. Dates are represented as days since 1900-01-01.

Creation Functions
^^^^^^^^^^^^^^^^^^

* ``today()`` - Current date
* ``now()`` - Current date and time
* ``date(year; month; day)`` - Create date
* ``time(hour; minute; second)`` - Create time

Extraction Functions
^^^^^^^^^^^^^^^^^^^^

* ``year(date)`` - Extract year
* ``month(date)`` - Extract month (1-12)
* ``day(date)`` - Extract day (1-31)
* ``weekday(date)`` - Day of week (1=Monday)
* ``hour(datetime)`` - Extract hour
* ``minute(datetime)`` - Extract minute

Calculation Functions
^^^^^^^^^^^^^^^^^^^^^

* ``datedif(start; end; unit)`` - Date difference
* ``networkdays(start; end)`` - Business days between dates

Examples
^^^^^^^^

**Age calculation:**

.. code-block:: none

   year(today()) - year(birthdate)

**Quarter extraction:**

.. code-block:: none

   ceil(month(date) / 3)

Special Functions
~~~~~~~~~~~~~~~~~

LabPlot provides 600+ specialized functions through GSL:

* **Bessel Functions**: ``J0``, ``J1``, ``Jn``, ``Y0``, ``Y1``, ``Yn``, ``I0``, ``K0``, etc.
* **Gamma and Beta**: ``gamma``, ``lgamma``, ``beta``, ``fact`` (factorial), ``choose`` (binomial)
* **Error Functions**: ``erf``, ``erfc``, ``voigt``
* **Elliptic Integrals**: ``Kc``, ``Ec``, ``F``, ``E``
* **Legendre Polynomials**: ``P1``, ``P2``, ``Pl``
* **Hypergeometric**: ``hyperg_0F1``, ``hyperg_1F1``, ``hyperg_2F1``
* **Probability Distributions**: PDF, CDF, and quantile functions for Gaussian, Student's t, Chi-squared, F, Exponential, Gamma, Beta, Poisson, Binomial, and many more

Random Number Generation
~~~~~~~~~~~~~~~~~~~~~~~~~

Generate random values from various distributions:

* ``rand()`` - Random integer [0, RAND_MAX]
* ``drand()`` - Random float [0, 1]
* ``randflat(a; b)`` - Uniform random [a, b]
* ``randgaussian(sigma)`` - Gaussian random
* ``randpoisson(mu)`` - Poisson random
* ``randbinomial(p; n)`` - Binomial random

**Example: Add noise**

.. code-block:: none

   x + randgaussian(0.1)

Text Columns and Formulas
--------------------------

Formula results are always numeric. For text columns, use numeric codes with value labels:

1. Create a text column for the result
2. Use a numeric formula: ``if(score >= 80; 2; if(score >= 60; 1; 0))``
3. Add value labels to the column:

   * 0 → "Fail"
   * 1 → "Pass"
   * 2 → "Excellent"

4. The spreadsheet displays text while storing numbers internally

This approach works for:

* Conditional text assignment
* Categorical data classification
* Status indicators

Tips and Best Practices
------------------------

Performance
~~~~~~~~~~~

* Disable **Auto Update** during data entry for large datasets
* Re-enable when done editing
* Column statistics are cached and fast to use

Accuracy
~~~~~~~~

* Use ``log1p(x)`` instead of ``log(1+x)`` for small x
* Use ``hypot(x; y)`` instead of ``sqrt(x^2+y^2)`` to avoid overflow
* Use ``equalE(a; b; epsilon)`` for floating-point comparisons

Debugging
~~~~~~~~~

* Test formulas on small datasets first
* Check for division by zero: ``if(equal(x; 0); 0; y/x)``
* Check for negative square roots: ``if(x >= 0; sqrt(x); 0)``

Common Patterns
~~~~~~~~~~~~~~~

**Clamp values to range:**

.. code-block:: none

   if(x < min; min; if(x > max; max; x))

**Distance from mean in standard deviations:**

.. code-block:: none

   fabs(x - mean(x)) / stdev(x)

**Percentage change:**

.. code-block:: none

   (current - previous) / previous * 100

**Running total:**

.. code-block:: none

   sum(x) / size(x) * i  # where i is row index

Additional Resources
--------------------

For a complete reference of all 620 available functions with detailed descriptions and examples, see the `LabPlot source code <https://invent.kde.org/education/labplot/-/blob/master/src/backend/gsl/functions.cpp>`_.
