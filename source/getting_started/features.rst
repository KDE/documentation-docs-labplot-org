.. _application_features:

Features
========

.. contents::

General Features
-----------------

- Project based management of data
- Tree-like organization of created objects
- Quick navigation, searching and filtering of objects using the Project Explorer
- Easy customization of objects and methods using the Properties Explorer
- Folders support for a better object management
- Spreadsheet and Matrix – data-container serving as the data source used in data analysis and visualization
- Spreadsheet linking to synchronize the number of rows across multiple spreadsheets
- Worksheet – area for placing different visualization objects (plots, labels, images, etc) supporting different layouts, zooming and navigation mode
- Notes – a text container which can simply be used to write comments into a project
- The undo history dialog
- Locale-sensitive functionality
- Autosave to prevent potential data loss
- Support for CLI parameters (e.g. to start LabPlot directly in the Presenter Mode)
- Support for multiple application color schemes, including dark themes
- Customizable application layouts using a full featured window docking system

Data Visualization
-------------------

- High-quality, interactive and very fast data visualization optimized for large data sets
- Arbitrary number of plots in the plot area
- Highly configurable and publication-quality 2D Plots: scatter plots, line plots, histograms, box plots, bar plots, rug plots, KDE plots, Q-Q plots, Lollipop plots
- Support for multiple, freely positionable axes, inverse axis scales and multiple ranges for plots
- Smooth and fast zooming and navigation modes for plots
- Function plotting with Cartesian, Polar and Parametric equations
- Customizable and positionable plot legends, text labels, info elements, images, reference lines and reference ranges for plots
- Color Maps Browser with an extensive support for scientific and color-vision deficiency friendly color schemes like ColorBrewer, ColorCET, Scientific Colour Maps, cocean, viridis
- Multiple default and user-defined themes for Worksheets and plots, including Edward Tufte’s ‘Maximal Data, Minimal ink’ theme,
- User-defined plot templates that make it easy to create and customize plots that are intended to be used multiple times
- Cursor – tool to measure positions and distances in plots
- Dynamic Presenter Mode for worksheets with the full-screen mode and the navigation panel
- Sparklines in the header of a spreadsheet
- Preview panel for all available worksheets in the project
- Support for Latex syntax in plot labels, plot titles, Computational Notebooks and multiple dialogs
- A possibility to use multiple LaTeX engines (LuaLaTex, pdfLaTex, LaTex)

Data Analysis and Statistics
--------------------------------

- Column statistics spreadsheet – child spreadsheet showing various statistical properties of the parent spreadsheet
- Linear and non-linear regression analysis and curve fitting, support for several predefined and user-defined fit models – Basic Functions like polynomial, power or exponential; Peak Functions like Gaussian, Cauchy-Lorentz, Pseudo-Voigt, hyperbolic secant, logistic; Growth Functions like Gompertz, Hill, Gudermann, inverse tangent, logistic and error functions; Statistical Functions like Gaussian, exponential, power, log-normal, binomial, Poisson, Rayleigh, Landau, Pareto, Weibull and many more
- Maximum Likelihood estimation for fitting statistical distributions like Gaussian Poisson, Exponential, Laplace, Binomial, Cauchy-Lorentz and more
- Baseline subtraction (background correction) with the asymmetrically re-weighted penalized least squares (arPLS) algorithm
- Data reduction by removing data points using multiple algorithms (Douglas-Peucker, Visvalingam-Whyatt, Reumann-Witkam, Opheim, Lang and other algorithms)
- Numerical differentiation (up to the 6th order) and numerical integration (rectangular, trapezoid and Simpson methods)
- Smoothing of data with moving average, Savitzky-Golay and percentile filter methods
- Interpolation of data, support for many methods (linear, polynomial, splines, piecewise cubic Hermite polynomial, etc.)
- Fourier transform of the input data with support for many different window functions (Welch, Hann, Hamming, Blackman, etc.)
- Fourier Filter – low-pass, high-pass, band-pass and band-reject filters of different types (Butterworth, Chebyshev I+II, Legendre, Bessel-Thomson)
- Hilbert Transform including envelope
- Convolution and de-convolution of data sets (sampling interval, linear/circular, normalization, wrap, standard kernel)
- Auto-correlation and cross-correlation of data sets (sampling interval, linear/circular, normalization)
- Quick statistical previews available in spreadsheets that consist of multiple location, dispersion and shape measures for quantitative and categorical data and statistical plots like histograms, KDE plots, Q-Q plots, box plots, Pareto plot
- Extensive parser for mathematical expressions supporting a great number of functions and constants used for data generation in spreadsheets and further data analysis and visualization
- Function values dialog (editor) with the syntax highlighting and support for reference to arbitrary cells of columns and other moving functions

Computational Notebooks
------------------------

- An interactive and animated front-end to powerful mathematics and statistics packages and programming languages like Maxima, Octave, R, Scilab, Sage, KAlgebra, Qalculate!, Python, Julia, Lua
- Support for using multiple notebooks and languages at the same time
- Notebook variables holding array-like data (Maxima lists, Python lists and tuples, etc.) can be used as the source for interactive plots
- Ability to show variable statistics and to plot data from the context menu in the project explorer for variables created in a Notebook
- Extensive edition capability
- Support for plotting
- Markdown and LaTeX syntax
- Ability to read Jupyter and Cantor projects
- Syntax highlighting
- Integrated help for CAS systems and programming languages (downloading, searching, navigating documentation etc.)
- Support for exporting Notebooks to PDF

Plot Digitization
-------------------

- Easy extraction of data from external image files
- Cartesian, polar, logarithmic and ternary coordinate system
- Symmetric and asymmetric error bars
- Manual point-by-point extraction of data points or (semi-)automated extraction of curve segments
- Multiple curves on the image can be read
- Basic image editing capabilities to reduce the image information to the relevant minimum
- Extracted data is added to a spreadsheet and is directly ready to use

Data Generation and Processing
-------------------------------

- Support for Tidy Data in spreadsheets, i.e. variables are stored in columns, each observation is stored in a row and the values for each observation is stored in its respective cell
- Quantitative and categorical data types: Integer, Double, Big Integer (64 bit), Date and Time, Text (Categorical)
- Data sorting
- Extended search and replace with the support for regular expressions
- Data transformation, normalization and standardization
- Random number generation with support for multiple probability distributions
- Data sampling (random and periodic methods)
- Data ‘flattening’ – converting pivoted data to the column-based format
- Support for dropping and masking of data in spreadsheets
- Heatmap formatting with the support for scientific and color-vision deficiency friendly color maps

Documentation and Support
--------------------------

- Extensive user manual and tutorials
- Short, instructional video tutorials
- Project examples and educational data sets available through LabPlot’s dialogs
- Relation type based gallery of plots with downloadable project files
- LabPlot is an open-source project offered in multiple languages
- Available for Windows, macOS, Linux, FreeBSD and Haiku
- LabPlot team offers multiple channels of communication
