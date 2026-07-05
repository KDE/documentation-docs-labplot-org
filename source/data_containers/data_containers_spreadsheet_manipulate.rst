.. _data_containers_spreadsheet_manipulate:

Manipulate Data
===============

.. contents::

Overview
--------

LabPlot provides a comprehensive set of tools for manipulating column data through the **Manipulate Data** context menu. These operations modify column values in-place, transforming data for analysis and visualization. All operations support undo/redo and work on multiple selected columns simultaneously.

**Usage:** Select column(s) → Right-click → **Manipulate Data** → Choose operation

Basic Arithmetic Operations
----------------------------

Apply arithmetic operations to all values in selected columns. These operations support both numeric values and time differences.

Add Value
~~~~~~~~~

Add a constant value or computed value to all entries in selected columns.

**Options:**

* **Custom Value** - Add a user-specified constant
* **Difference** - Add the difference between start and end values (linear trend)

**Use cases:**

* Add offset to measurements
* Shift baseline to zero
* Apply calibration corrections

**Example:**

.. code-block:: none

   Original: [10, 20, 30, 40]
   Add 5 → [15, 25, 35, 45]

Subtract Value
~~~~~~~~~~~~~~

Subtract values from all entries in selected columns. Includes statistical subtraction options.

**Options:**

* **Custom Value** - Subtract a constant
* **Minimum** - Subtract the column's minimum value (shifts minimum to 0)
* **Maximum** - Subtract the column's maximum value
* **Median** - Subtract the median (centers around 0)
* **Mean** - Subtract the mean (centers around 0, removes DC offset)
* **Difference** - Subtract linear trend
* **Baseline (arPLS Algorithm)** - Advanced baseline subtraction using Asymmetric Reweighted Penalized Least Squares

**Use cases:**

* Center data around zero
* Remove baseline drift
* Subtract background signal
* Normalize to starting value

**Example - Remove DC offset:**

.. code-block:: none

   Original: [15, 25, 35, 45]
   Subtract Mean (30) → [-15, -5, 5, 15]

Subtract Baseline
^^^^^^^^^^^^^^^^^

Advanced baseline subtraction using the arPLS (Asymmetrically Reweighted Penalized Least Squares) algorithm. This is particularly useful for spectroscopy, chromatography, and signal processing where baseline drift needs to be removed.

**Parameters:**

* **Lambda (λ)** - Smoothness parameter (default: 10⁶)

  * Larger values → smoother baseline
  * Smaller values → baseline follows data more closely
  * Typical range: 10² to 10⁹

* **Ratio** - Weighting termination ratio (0 to 1, default: 0.01)

  * Controls how much negative values are allowed
  * Smaller values → less tolerant of negative deviations
  * 0.01 is suitable for most cases

* **Iterations** - Number of iterations (default: 10)

  * More iterations → better convergence
  * 10-20 is usually sufficient

**Use cases:**

* Remove baseline drift in spectra
* Subtract background in chromatography peaks
* Eliminate low-frequency trends in time series

**Preview:** The dialog includes a live preview showing the original data, estimated baseline, and result after subtraction.

Multiply by Value
~~~~~~~~~~~~~~~~~

Multiply all entries by a constant factor.

**Use cases:**

* Unit conversion (e.g., meters to kilometers)
* Apply scaling factor
* Amplify or attenuate signal

**Example:**

.. code-block:: none

   Original: [1, 2, 3, 4]
   Multiply by 10 → [10, 20, 30, 40]

Divide by Value
~~~~~~~~~~~~~~~

Divide all entries by a constant value.

**Use cases:**

* Unit conversion (e.g., millimeters to meters)
* Normalize by reference value
* Scale down large values

**Example:**

.. code-block:: none

   Original: [100, 200, 300, 400]
   Divide by 100 → [1, 2, 3, 4]

.. warning::
   Division by zero will result in NaN (Not a Number) values.

Data Reordering
---------------

Reverse
~~~~~~~

Reverse the order of values in selected columns. For numeric columns (Double), trailing NaN values are ignored during reversal.

**Usage:** Select column(s) → Right-click → Manipulate Data → **Reverse**

**Use cases:**

* Reverse time series to analyze from end to start
* Flip spatial data orientation
* Reorder measurements

**Example:**

.. code-block:: none

   Original: [10, 20, 30, 40, 50]
   Reversed: [50, 40, 30, 20, 10]

Data Filtering
--------------

Drop Values
~~~~~~~~~~~

Permanently remove values from columns based on criteria. This is useful for cleaning data by removing outliers, invalid measurements, or unwanted ranges.

**Operators for numeric columns:**

* **Equal to** - Drop values equal to specified value
* **Between (exclusive)** - Drop values in range (min, max)
* **Between (inclusive)** - Drop values in range [min, max]
* **Greater than** - Drop values > threshold
* **Greater than or equal** - Drop values ≥ threshold
* **Less than** - Drop values < threshold
* **Less than or equal** - Drop values ≤ threshold

**Operators for text columns:**

* **Equal to** - Drop exact matches
* **Not equal to** - Drop all except exact matches
* **Starts with** - Drop values starting with pattern
* **Ends with** - Drop values ending with pattern
* **Contains** - Drop values containing pattern

**Operators for datetime columns:**

* Same comparison operators as numeric columns
* Date/time pickers for precise specification

**Use cases:**

* Remove outliers from measurements
* Filter out error codes or invalid values
* Remove specific ranges for focused analysis
* Clean text data by removing unwanted patterns

**Example:**

.. code-block:: none

   Original: [1, 5, 10, 15, 100, 20, 25]
   Drop "Greater than 50" → [1, 5, 10, 15, 20, 25]

Mask Values
~~~~~~~~~~~

Temporarily exclude values from visualization and analysis without deleting them. Masked values remain in the column but are ignored by plots, fits, and statistical calculations. This is preferable to dropping when you want to preserve original data.

**Operators:** Same as Drop Values (see above)

**Use cases:**

* Exclude outliers from fitting without losing data
* Temporarily hide measurement errors
* Focus analysis on specific value ranges
* Compare results with/without certain data points

**Example:**

.. code-block:: none

   Data: [1, 5, 10, 100, 15, 20]
   Mask "Greater than 50"
   Visible in plots: [1, 5, 10, 15, 20]
   Original data preserved: [1, 5, 10, 100*, 15, 20]  (* = masked)

.. tip::
   Masked values can be unmasked later using the context menu for the selected cells in the spreadsheet or for the whole spreadsheet.

.. seealso::
   For more information about masking, see :ref:`data_containers_spreadsheet` → Mask Data section.

Normalization
-------------

Normalize data to make different measurements comparable. LabPlot provides 15 normalization methods organized by category.

Basic Normalization
~~~~~~~~~~~~~~~~~~~

**Divide by Sum**
   Scale values so they sum to 1 (convert to proportions).

   Formula: :math:`x_i' = \frac{x_i}{\sum x_i}`

**Divide by Min**
   Scale minimum value to 1.

   Formula: :math:`x_i' = \frac{x_i}{\min(x)}`

**Divide by Max**
   Scale maximum value to 1 (common in [0,1] normalization).

   Formula: :math:`x_i' = \frac{x_i}{\max(x)}`

**Divide by Count**
   Divide by number of values (compute average contribution).

   Formula: :math:`x_i' = \frac{x_i}{n}`

Central Tendency Normalization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Divide by Mean**
   Express values as ratio to mean.

   Formula: :math:`x_i' = \frac{x_i}{\bar{x}}`

**Divide by Median**
   Express values as ratio to median (robust to outliers).

   Formula: :math:`x_i' = \frac{x_i}{\text{median}(x)}`

**Divide by Mode**
   Express values as ratio to most frequent value.

   Formula: :math:`x_i' = \frac{x_i}{\text{mode}(x)}`

Spread Normalization
~~~~~~~~~~~~~~~~~~~~

**Divide by Range**
   Scale to range width.

   Formula: :math:`x_i' = \frac{x_i}{\max(x) - \min(x)}`

**Divide by SD (Standard Deviation)**
   Scale to standard deviation units (without centering).

   Formula: :math:`x_i' = \frac{x_i}{\sigma}`

**Divide by MAD (Median Absolute Deviation)**
   Robust spread normalization.

   Formula: :math:`x_i' = \frac{x_i}{\text{MAD}(x)}`

**Divide by IQR (Interquartile Range)**
   Scale to interquartile range (robust to outliers).

   Formula: :math:`x_i' = \frac{x_i}{Q_3 - Q_1}`

Standardization (Z-Scores)
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Z-Score (SD)** - Standard z-score transformation
   Center at mean and scale to unit variance.

   Formula: :math:`z_i = \frac{x_i - \bar{x}}{\sigma}`

   **Use cases:** Compare distributions, standardize for machine learning, detect outliers

   **Result:** Mean = 0, SD = 1

**Z-Score (MAD)** - Robust z-score using median
   Robust alternative using median and MAD.

   Formula: :math:`z_i = \frac{x_i - \text{median}(x)}{\text{MAD}(x)}`

   **Use cases:** Robust outlier detection, heavy-tailed distributions

**Z-Score (IQR)** - Robust z-score using quartiles
   Another robust alternative using median and IQR.

   Formula: :math:`z_i = \frac{x_i - \text{median}(x)}{Q_3 - Q_1}`

Rescaling
~~~~~~~~~

**Rescale to [a, b]**
   Map values to arbitrary interval [a, b]. A dialog prompts for min and max values.

   Formula: :math:`x_i' = a + \frac{(x_i - \min(x)) \cdot (b - a)}{\max(x) - \min(x)}`

   **Common ranges:**

   * [0, 1] - Unit interval normalization
   * [−1, 1] - Centered range
   * [0, 100] - Percentage scale
   * [0, 255] - Image pixel values

**Use cases:**

* Normalize features for machine learning
* Scale data to plot range
* Convert to percentage or standardized units

Ladder of Powers Transformations
---------------------------------

Apply Tukey's Ladder of Powers transformations to improve normality, stabilize variance, or linearize relationships. These transformations are ordered by increasing power.

Available Transformations
~~~~~~~~~~~~~~~~~~~~~~~~~

**1/x² (Inverse Squared)**
   Strong transformation for highly right-skewed data.

   Formula: :math:`y = \frac{1}{x^2}`

   **Effect:** Strong right-to-left redistribution

   **Note:** Undefined for x = 0

**1/x (Inverse)**
   Strong reciprocal transformation.

   Formula: :math:`y = \frac{1}{x}`

   **Effect:** Reverses scale direction, strong skew correction

   **Use cases:** Rate data, reciprocal relationships

   **Note:** Undefined for x = 0

**1/√x (Inverse Square Root)**
   Moderate inverse transformation.

   Formula: :math:`y = \frac{1}{\sqrt{x}}`

   **Effect:** Moderate right-to-left redistribution

   **Note:** Undefined for x ≤ 0

**log(x) (Logarithm)**
   Common transformation for right-skewed data.

   Formula: :math:`y = \log_{10}(x)`

   **Effect:** Compresses large values, expands small values

   **Use cases:**

   * Data spanning multiple orders of magnitude
   * Multiplicative relationships → additive
   * Right-skewed distributions → more symmetric

   **Note:** Undefined for x ≤ 0

**√x (Square Root)**
   Mild transformation for count data or moderate skew.

   Formula: :math:`y = \sqrt{x}`

   **Effect:** Mild compression of large values

   **Use cases:**

   * Poisson-distributed count data
   * Variance proportional to mean
   * Mild right skew

   **Note:** Undefined for x < 0

**x² (Squared)**
   Expands differences for large values.

   Formula: :math:`y = x^2`

   **Effect:** Amplifies large values, compresses small values

   **Use cases:**

   * Left-skewed distributions
   * Emphasize large deviations
   * Quadratic relationships

**x³ (Cubed)**
   Strong expansion of large values, preserves sign.

   Formula: :math:`y = x^3`

   **Effect:** Strong amplification of large values

   **Use cases:**

   * Cubic relationships
   * Strong left skew correction
   * Preserves negative values (unlike even powers)

Choosing a Transformation
~~~~~~~~~~~~~~~~~~~~~~~~~~

**For right-skewed data (long tail to the right):**
   Move down the ladder: log(x), √x

**For left-skewed data (long tail to the left):**
   Move up the ladder: x², x³

**For variance stabilization:**

* Poisson count data → √x
* Proportions/percentages → arcsin(√x) (not in menu, use formula)
* Variance proportional to mean → log(x)

**Visual guide:**

.. code-block:: none

   ← Stronger left skew correction     Stronger right skew correction →

   x³  →  x²  →  √x  →  log(x)  →  1/√x  →  1/x  →  1/x²

.. tip::
   After transformation, check if the data distribution improved using a histogram or normal probability plot.

.. warning::
   Pay attention to domain restrictions:

   * Square root, log: require x ≥ 0
   * Inverse: undefined at x = 0
   * Even powers: lose sign information

Best Practices
--------------

Arithmetic Operations
~~~~~~~~~~~~~~~~~~~~~

* **Preview before applying** - Use preview feature for baseline subtraction to verify parameters
* **Check for zero** - Division operations can produce NaN values
* **Document operations** - Keep notes on applied transformations for reproducibility

Filtering and Masking
~~~~~~~~~~~~~~~~~~~~~~

* **Prefer masking over dropping** - Masking preserves original data
* **Use masking for exploration** - Test different filtering criteria without data loss
* **Drop for final cleanup** - Use drop when you're certain values should be permanently removed

Normalization
~~~~~~~~~~~~~

* **Choose appropriate method** - Z-score for comparison, rescale for visualization, divide by max for proportions
* **Check for zeros** - Many normalization methods fail with zero denominators
* **Robust methods for outliers** - Use MAD or IQR-based methods when outliers are present

Transformations
~~~~~~~~~~~~~~~

* **Understand the goal** - Are you linearizing, stabilizing variance, or improving normality?
* **Check domain** - Verify data is positive for log/sqrt transformations
* **Visualize results** - Plot before and after to verify improvement
* **Consider back-transformation** - Remember to interpret results in original scale

Common Workflows
----------------

Outlier Detection and Removal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Calculate z-score: Manipulate Data → Normalize → **(x-Mean)/SD**
2. Identify outliers: Values with ``|z| > 3``
3. Mask or drop: Manipulate Data → **Mask Values** (or Drop Values) → "Greater than 3" and "Less than -3"

Baseline Correction
~~~~~~~~~~~~~~~~~~~

1. Select signal column
2. Manipulate Data → **Subtract Baseline**
3. Adjust λ parameter (start with 10⁶)
4. Use preview to verify baseline fit
5. Apply subtraction

Preparing Data for Analysis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. **Remove obvious errors**: Drop or mask invalid values
2. **Transform if needed**: Apply log/sqrt for skewed data
3. **Normalize**: Apply appropriate normalization for comparison
4. **Center if required**: Subtract mean for zero-centered analysis

Unit Conversion
~~~~~~~~~~~~~~~

1. Identify conversion factor (e.g., mm → m: divide by 1000)
2. Select column(s)
3. Manipulate Data → **Multiply** or **Divide by Value**
4. Enter conversion factor

Additional Resources
--------------------

* For formula-based transformations: :ref:`data_containers_spreadsheet_formulas`
* For statistical operations: Column Statistics and Statistics Spreadsheet
* For data generation: :ref:`data_containers_spreadsheet` → Generate Data
