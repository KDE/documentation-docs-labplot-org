.. meta::
   :description: Guide to creating and interpreting continual improvement plots in LabPlot
   :keywords: LabPlot, 2D plotting, continual improvement plots, process control, quality improvement

.. metadata-placeholder

   :authors: - LabPlot Team

.. _2D_plotting_continual_improvement_plots:

Continual Improvement Plots
============================


Continual Improvement Plots
---------------------------

This section describes the Continual Improvement Plots available in LabPlot. These tools, which include the Run Chart and Process Behavior Charts (Control Charts), allow users to monitor process stability.

.. note::

    In LabPlot, data for these charts is typically entered as a single column of values. Grouping into subgroups is handled via the chart settings, not by rearranging the spreadsheet columns.

Common Applications
-------------------

These charts are widely used in Quality Control, Manufacturing, and Process Improvement methodologies (such as Six Sigma and Lean). They help engineers and analysts:

- Monitor production consistency (e.g., part dimensions).
- Track defect rates in service or manufacturing.
- Detect process shifts or unusual events early.
- Validate whether process changes have led to real improvements.

Available Charts
----------------

LabPlot supports both simple trend analysis and advanced statistical process control. Users can combine multiple charts (e.g., X-bar and R) to create comprehensive views of process performance.

- **Run Chart:** A simple line graph of data plotted over time with a central line, use when analyzing trends without statistical limits.
- **Process Behavior Charts:** These charts use statistical limits to distinguish between Common Cause Variation (Process Noise) and Assignable Cause Variation (Process Signals).

Variable Charts (Continuous Data)
---------------------------------

These charts are for measured data. You often use a Location Chart (for the average) together with a Dispersion Chart (for the variation).

Location Charts (Center)

- **X-bar Chart:** Monitoring the average of subgroups.
- **X Chart (Individuals):** Monitoring individual values (n=1).

Dispersion Charts (Spread)
--------------------------

These are usually added below a Location Chart.

- **R Chart (Range):** Monitoring range in small subgroups (n ≤ 9).
- **S Chart (Standard Deviation):** Monitoring deviation in large subgroups (n > 10).
- **mR Chart (Moving Range):** Monitoring variation between individual consecutive points.

Attribute Charts (Count Data)
-----------------------------

These are standalone charts for counted data.

- **p-Chart:** Percentage of defectives (requires variable sample size column).
- **np-Chart:** Count of defectives (constant sample size).
- **c-Chart:** Count of defects (constant area).
- **u-Chart:** Defects per unit (requires unit size column).

Usage
-----

To create a Continual Improvement Plot in LabPlot:

1. Select the column containing your measurement data in the Spreadsheet.
2. Navigate to the Plot menu or right-click the column selection.
3. Go to Plot Data > Continual Improvement Plots and select your initial chart type (e.g., Process Behavior Chart > X-bar).

Configure the Chart in the Dock Widget:

- Chart Type: You can switch the type here (e.g., from X-bar to R).
- Subgrouping: Define the subgroup size (e.g., "5") to automatically group your single column of data.
- Limits: Choose the type of control limits:

   - Statistical: Calculated from the data itself (default).
   - Specification: User-defined fixed limits.

- Center Line: Choose whether limits are calculated based on the Mean (average) or Median.

Add a Companion Chart:

To see variation (e.g., R Chart) alongside your main chart, right-click the plot area and add a new Process Behavior Chart.

Configure it similarly, ensuring subgroup parameters match.


