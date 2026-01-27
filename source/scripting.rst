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
A simple working example that creates a new worksheet in the current project is shown below:

.. code-block:: python

   from pylabplot import *

   # Get the current project
   project = project()

   # Create a new worksheet
   worksheet = Worksheet("My Worksheet")

   # Add the worksheet to the project
   project.addChild(worksheet)

The Python API documentation can be found in the :ref:`sdk_python` section.