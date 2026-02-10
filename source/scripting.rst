.. meta::
   :description: A description of the scripting capabilities of LabPlot
   :keywords: LabPlot, documentation, user manual, scripting, automation, batch processing

.. metadata-placeholder

   :authors: - LabPlot Team

.. _scripting:

Scripting
===================

Introduction
----------------------------------------

Scripting within the application allows users to create scripts that can perform repetitive tasks, manipulate data, and generate plots without manual intervention.
It provides access to the application's functionalities and to the current application runtime through a well-defined API.
This is particularly useful for batch processing of data sets and for automating complex or repetitive workflows. Currently, the only supported scripting language in LabPlot is Python.

.. note::
    Although there are similarities and overlaps in the functionality provided by the :ref:`computational_notebooks` and the :ref:`sdk_python`, where Python can be used to combine LabPlot's functionality with the power of Python and other external modules, they are distinct and serve different purposes. **Computation Notebooks** are primarily designed for interactive data analysis and visualisation within a REPL interface (read-evaluate-print loop), while the **Python SDK** enables LabPlot's functionality to be used in external Python applications. In contrast, **Python Scripting** within the application focuses on automating tasks and workflows within the running LabPlot application itself.


Getting Started
----------------------------------------
To create a new script, select `File → Add New → Script → Python` from the main menu. This opens a new window containing a script editor and the output console.
You can write your script in this editor and execute it by clicking the `Run Script` button in the toolbar of the script editor.

The bindings are imported into the current script runtime via

.. code-block:: python

   from pylabplot import *

The next step in such a script depends on obtaining a reference to the current project, which is done via the call.

.. code-block:: python

   project = project()

After this, you have full access to the project structure and can navigate through it to access or modify its components.
A simple working example that creates a new worksheet in the current project is:

.. code-block:: python

   from pylabplot import *

   # Get the current project
   project = project()

   # Create a new worksheet
   worksheet = Worksheet("My Worksheet")

   # Add the worksheet to the project
   project.addChild(worksheet)

A more realistic example importing multiple files from a folder and creating plots in separate worksheets for each imported data set is shown below:

.. code-block:: python

   import os
   from pylabplot import *

   # Get the current project
   project = project()

   # Define the folder containing the data files
   data_folder = "/path/to/data/folder"

   # Iterate over all files in the folder
   for filename in os.listdir(data_folder):
       if filename.endswith(".txt"):  # Assuming text files
           file_path = os.path.join(data_folder, filename)

           # Create a new spreadsheet and import data
           spreadsheet = Spreadsheet(filename)
           project.addChild(spreadsheet)
           filter = AsciiFilter()
           filter.readDataFromFile(file_path, spreadsheet)

           # Create a new worksheet
           worksheet = Worksheet(f"Worksheet for {filename}")
           project.addChild(worksheet)

           # Create a plot for the imported data
           plot_area = CartesianPlot(f"Plot for {filename}")
           plot_area.setType(CartesianPlot.Type.FourAxes)
           plot_area.addLegend()
           worksheet.addChild(plot_area)

           # Create a line plot for the first two columns
           line_plot = XYCurve(f"Line Plot for {filename}")
           line_plot.setXColumn(spreadsheet.column(0))
           line_plot.setYColumn(spreadsheet.column(1))
           plot_area.addChild(line_plot)


The Python API documentation can be found in the :ref:`sdk_python` section which is part of the :ref:`sdk` documentation.

Usage of Python Packages
----------------------------------------

The Python scripting environment in LabPlot allows you to use external Python packages in your scripts. To use an external package, you need to ensure that it is installed in the Python environment that LabPlot uses for scripting. You can check the path to this environment and the installed packages by running the following code in the script editor:

.. code-block:: python

   import sys
   print(sys.executable)  # Path to the Python interpreter used by LabPlot
   print(sys.path)        # List of paths where Python looks for packages

To check the location of a specific package, you can use the following code:

.. code-block:: python

   import <package-name>
   print(<package-name>.__file__)  # Path to the package

Additional attention needs to be paid for Linux package formats like AppImage and Flatpak, where the Python environment is sandboxed and does not have access to the system-wide installed packages. In this case, you need to point the sandbox to the already installed packages or to install the required packages within the sandboxed environment

For example, to make AppImage use the system-wide installed packages, you can set the environment variable `PYTHONPATH` to include the path to the system's site-packages directory before launching the AppImage:

.. code-block:: bash

   export PYTHONPATH=/path/to/site-packages:$PYTHONPATH
   ./labplot-<version>.AppImage

For Flatpak, you can use

.. code-block:: bash

   flatpak override --filesystem=/path/to/site-packages org.kde.LabPlot

to give the Flatpak access to the system's site-packages directory.

Alternatively, you can use

.. code-block:: bash

   flatpak run --command=pip3 org.kde.LabPlot install <package-name>

to install packages in the Flatpak environment. For AppImage, you can use

.. code-block:: bash

   ./labplot-<version>.AppImage --appimage-extract

to extract the AppImage, then navigate to the extracted directory and use the included Python environment to install packages.
