Getting Started
===================

############
Installation
############

The LabPlot Python SDK is included with a LabPlot installation. Please refer to the official LabPlot `website <https://labplot.org/download/>`_ for how to get a LabPlot installation for your respective system.

#####
Usage
#####

The LabPlot Python SDK provides a Python module `pylabplot` which is wrapper to the internal C++ classes that are made available as part of the public API in the SDK. This module needs to be imported in your Python scripts to get the access to LabPlot's functionality. The snippet below imports all components from this module:

 .. code-block:: python

    from pylabplot import *

Alternatively, separate components can be imported as needed:

 .. code-block:: python

    from pylabplot import Worksheet, Spreadsheet, CartesianPlot
    # etc.

