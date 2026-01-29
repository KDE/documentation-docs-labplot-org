.. meta::
   :description: Overview of hypothesis testing available in LabPlot
   :keywords: LabPlot, statistical tests, hypothesis testing, t-test, ANOVA, non-parametric, survival analysis

.. metadata-placeholder

   :authors: - LabPlot Team

.. _hypothesis_testing:

Hypothesis Testing
===================

Hypothesis Tests
-----------------

This section describes the hypothesis tests available in LabPlot. These tools allow users to perform inferential statistics on their data to determine significance, compare groups, and analyze distributions.

Common Applications
-------------------

Hypothesis tests are essential in Research, Quality Assurance, and Data Analysis across various fields (e.g., science, engineering, sociology). They help analysts:

- Determine if an experimental treatment has a real effect (e.g., drug vs. placebo).
- Compare performance between different groups or manufacturing processes.
- Analyze survey data to find associations between categorical variables.
- Assess reliability and survival times in engineering or medical studies.

Available Tests
---------------

LabPlot currently supports a comprehensive suite of tests, categorized into parametric and non-parametric methods.

Parametric Tests
~~~~~~~~~~~~~~~~

Parametric tests assume that the data follows a specific distribution, typically a normal distribution. These tests are generally more powerful than non-parametric tests when their assumptions are met.

- **One-Sample t-Test:** Used to compare the mean of a single sample to a known value or theoretical population mean.
- **Independent Two-Sample t-Test:** Compares the means of two independent groups to determine if there is a statistically significant difference between them. This test assumes equal variances.
- **Paired Two-Sample t-Test:** Compares means from the same group at different times (e.g., before and after an intervention) or matched pairs.
- **Welch's t-Test:** An adaptation of the independent t-test used when the two samples have unequal variances.
- **One-Way ANOVA Test:** A parametric test comparing the means of three or more independent groups to determine if at least one group mean is statistically different from the others.
- **One-Way ANOVA with Repeated Measures Test:** Used when the same subjects are measured multiple times under different conditions to detect changes over time or across treatments.

Non-Parametric Tests
~~~~~~~~~~~~~~~~~~~~

Non-parametric tests do not assume a normal distribution and are useful for ordinal data, ranked data, or when parametric assumptions are violated.

- **Mann-Whitney U Test:** A non-parametric alternative to the independent t-test, used to assess whether two independent samples come from the same distribution.
- **Wilcoxon Signed Rank Test:** The non-parametric equivalent of the paired t-test, used to compare two related samples or repeated measurements on a single sample.
- **Kruskal-Wallis Test:** An extension of the Mann-Whitney U test for more than two groups; it serves as a non-parametric alternative to One-Way ANOVA for independent samples.
- **Friedman Test:** A non-parametric alternative to the One-Way ANOVA with Repeated Measures, used to detect differences in treatments across multiple test attempts.
- **Chi-Square Independence Test:** Used to determine if there is a significant association between two categorical variables.
- **Chi-Square Goodness of Fit Test:** Used to determine if a sample distribution matches a theoretical population distribution.
- **Log-Rank Test:** A hypothesis test to compare the survival distributions of two samples. It is widely used in clinical trials and reliability engineering to analyze time-to-event data.
- **Mann-Kendall Test:** A non-parametric statistical test used to detect the presence of a monotonic trend (increasing or decreasing) in time-series data, without assuming a specific distribution.

Usage
-----

Refer to the LabPlot data analysis UI (Analyze / Statistics dialogs) within the application for step-by-step usage of each test. Each test in LabPlot provides options to select input columns, choose grouping variables, and set test-specific parameters. For details and examples, consult the relevant subsections in this documentation (to be added) or the application help dialogs.

