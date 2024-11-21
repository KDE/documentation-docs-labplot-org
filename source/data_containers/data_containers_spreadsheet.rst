.. _data_containers_spreadsheet:

Spreadsheet
===================

.. contents::


Basic Concepts
--------------------

The :ref:`data_containers_spreadsheet` is the main part of LabPlot when working with data and consists out of columns. ``Column`` is the basic data set in LabPlot used for plotting and data analysis. Every ``column`` of the :ref:`data_containers_spreadsheet` consists of ``cells`` and is specified by its name and the type - `numeric`, `text`, `month names`, `day names` and `date and time`. Also, for each type different representation formats can be assigned like decimal or scientific format for numeric columns etc.

In addition to these properties it is also possible to specify the ``plot designation`` - LabPlot is using this property in some places to to automatically recognize how to plot the data and which columns to use as X, Y, etc.


Import Data
-----------------

See the video on how to import e.g. an `SPSS` file and export it to text.

.. youtube:: GmGzv6a_5Jk
   :align: left
   :width: 650px

Generate Data
------------------

See the video on wow to generate and visualize random numbers from the `Uniform`, `Normal (Gaussian)`, `Binomial`, `Poisson`, `Weibull` and many more distributions in LabPlot.

.. youtube:: GmGzv6a_5Jk
   :align: left
   :width: 650px

Data Analysis and Visualization
-----------------------------------

Mask Data
~~~~~~~~~~~~~~

Sometimes it is required to ignore some data points in the visualization or when performing some data analysis like fitting etc. To exclude some data points from plotting and data analysis without deleting them, ``masking`` of those data points can be used. You can mask the selected data points in the :ref:`data_containers_spreadsheet` (:menuselection:`Selection` / :menuselection:`Mask Selection` from the :ref:`data_containers_spreadsheet` cell context menu).

In the example below a ``fit`` was performed to the original data containing some obvious measurement errors and a fit where those outliers were masked.

.. todo:: screenshot with two fits

Manipulate Data
~~~~~~~~~~~~~~~~~~~~~~~

.. todo:: add a description

Descriptive Statistics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See the video on how to quickly get descriptive statistics with visualization.

.. youtube:: 2dJ19VCKRho
   :align: left
   :width: 650px

Baseline Subtraction (Correction)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See the video on how to perform Baseline Subtraction in LabPlot.

.. youtube:: Fl2fACGlYrY
   :align: left
   :width: 650px
