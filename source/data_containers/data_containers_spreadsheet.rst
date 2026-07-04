.. _data_containers_spreadsheet:

Spreadsheet
===================

.. contents::


Basic Concepts
--------------------

The :ref:`data_containers_spreadsheet` is the main part of LabPlot when working with data and consists out of columns. ``Column`` is the basic data set in LabPlot used for plotting and data analysis. Every ``column`` of the :ref:`data_containers_spreadsheet` consists of ``cells`` and is specified by its name and the type of the data:

* **Double** - floating-point numbers with double precision for decimal values (range:  ±1.79769 × 10\ :sup:`308`)
* **Integer** - whole numbers, 32-bit signed integers (range: -2,147,483,648 to 2,147,483,647)
* **Big Integer** - large whole numbers, 64-bit signed integers (range: -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807)
* **Text** - alphanumeric strings and text data
* **Date & Time** - date and time values

For each type different representation formats can be assigned like decimal or scientific format for numeric columns etc. In addition to these properties it is also possible to specify the ``plot designation`` that is used in some places to to automatically recognize how to plot the data and which columns to use as X, Y, etc.

Data Structure
--------------------------
There are two commonly used ways to structure the data in the spreadsheet - the "wide" format and the "long" (or "tidy") format. In a wide format, each subject has a single row, and various attributes or time points are spread across multiple columns (e.g., time series data where each time point is a column). For tidy data, each variable is a column and each observation is a row.

For the following example in the wide format for the score obtained by students in three tests

=======  ======  ======  ======
Name     Test 1  Test 2  Test 3
=======  ======  ======  ======
Alice    85      90      88
Bob      70      75      80
=======  ======  ======  ======

"Test Number" and "Score" are the actual variables, while "Name" is an identifier. In the tidy format, the same data would be structured as follows:

=======  ===========  ======
Name     Test Number  Score
=======  ===========  ======
Alice    Test 1       85
Alice    Test 2       90
Alice    Test 3       88
Bob      Test 1       70
Bob      Test 2       75
Bob      Test 3       80
=======  ===========  ======

.. important::
   While both formats are valid and supported in LabPlot, attention needs to be paid to the way how LabPlot operates on the data - namely, for the visualization and analysis, LabPlot always operates on columns and not on rows and therefore different data formats will produce different results.

For example, visualizing the data for both formats in a Bar Plot will produce the following results:

.. image:: images/spreadsheet_bar_plot_wide_format.png
   :align: center
   :alt: Bar Plot for the wide format

.. image:: images/spreadsheet_bar_plot_long_format.png
   :align: center
   :alt: Bar Plot for the long/tidy format

In the first case, the visualization of the three numerical columns with the scores in a bar plot leads to a "grouped" bar plot with three bars  - each bar represents a score and each group represents a student name. In the second case, the visualization of the "Score" column (the only numerical column in the spreadhseet) leads to a bar plot with six separate bars - one bar for the score values for each combination of "Name" and "Test Number".


Import Data
-----------------


Generate Data
------------------

Column Formulas
~~~~~~~~~~~~~~

Columns can be populated with values calculated from formulas. The formula system supports over 600 mathematical, statistical, and scientific functions from the GNU Scientific Library (GSL).

**Quick Example:**

.. code-block:: none

   # Calculate distance from origin
   sqrt(x^2 + y^2)

   # Normalize data (z-score)
   (value - mean(value)) / stdev(value)

   # Conditional logic
   if(temperature > 0; 1; 0)

To create a formula column, right-click on the column header and select **Formula**. Enter your expression, map variables to columns, and enable **Auto Update** for automatic recalculation.

For detailed information about syntax, available functions, and examples, see :ref:`data_containers_spreadsheet_formulas`.


Data Analysis and Visualization
-----------------------------------

Manipulate Data
------------------

Mask Data
~~~~~~~~~~~~~~

Sometimes it is required to ignore some data points in the visualization or when performing some data analysis like fitting etc. To exclude some data points from plotting and data analysis without deleting them, ``masking`` of those data points can be used. You can mask the selected data points in the :ref:`data_containers_spreadsheet` (:menuselection:`Selection` / :menuselection:`Mask Selection` from the :ref:`data_containers_spreadsheet` cell context menu).

In the example below a ``fit`` was performed to the original data containing some obvious measurement errors and a fit where those outliers were masked.

.. .. todo:: add a screenshot with two fits

.. Baseline Subtraction (Correction)  
.. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Statistics
-----------------------------------

Column Statistics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Column Statistics Spreadsheet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


