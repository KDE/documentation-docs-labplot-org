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

The Python scripting environment in LabPlot allows you to use external Python packages in your scripts. The Python environment used depends on how LabPlot was installed:

- **Bundled Python distributions** (macOS, Windows, AppImage, Flatpak): LabPlot includes its own Python interpreter
- **System installations** (Linux package managers like apt, dnf, pacman): LabPlot uses the system's Python interpreter

Checking Your Python Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can check which Python interpreter LabPlot is using and what packages are installed by running the following code in the script editor:

.. code-block:: python

   import sys
   print(sys.executable)  # Path to the Python interpreter used by LabPlot
   print(sys.path)        # List of paths where Python looks for packages

To check the location of a specific package:

.. code-block:: python

   import <package-name>
   print(<package-name>.__file__)  # Path to the package

Installing Additional Packages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The installation method depends on whether LabPlot uses a bundled Python or the system Python.

**For Bundled Python Distributions (macOS, Windows, AppImage, Flatpak)**

You have two main approaches for installing additional Python packages:

**Option 1: Install into User Site-Packages (Recommended)**

The simplest method is to install packages directly from within LabPlot's Python scripting environment using pip. This works on all platforms with bundled Python:

.. code-block:: python

   import pip
   pip.main(['install', 'numpy', '--user'])

The ``--user`` flag installs packages to your user's Python directory, making them available to LabPlot while keeping them separate from the bundled Python installation:

- **Linux:** ``~/.local/lib/python3.x/site-packages/``
- **macOS:** ``~/Library/Python/3.x/site-packages/``
- **Windows:** ``%APPDATA%\Python\Python3x\site-packages\``

After installation, you can import and use the package:

.. code-block:: python

   import numpy as np
   print(np.__version__)

You can install multiple packages in one script:

.. code-block:: python

   import pip

   # Install common scientific packages
   packages = ['numpy', 'scipy', 'pandas', 'scikit-learn']

   for package in packages:
       pip.main(['install', package, '--user'])
       print(f"Installed {package}")

**Option 2: Use a Virtual Environment**

For more control over package versions or complete environment isolation, you can configure LabPlot to use a Python virtual environment. This is particularly useful for:

- Managing different package versions for different projects
- Isolating dependencies between projects
- Testing packages before installing them globally

To set up and use a virtual environment:

1. Create a virtual environment and install packages (using your system's Python or the bundled Python):

   .. code-block:: bash

      # Linux/macOS
      python3 -m venv ~/labplot-env
      source ~/labplot-env/bin/activate
      pip install numpy scipy pandas

      # Windows (Command Prompt)
      python -m venv %USERPROFILE%\labplot-env
      %USERPROFILE%\labplot-env\Scripts\activate.bat
      pip install numpy scipy pandas

2. In LabPlot, go to **Settings → Configure LabPlot → Scripting**

3. Under **Python Environment**, browse to select your virtual environment's Python executable:

   - **Linux/macOS:** ``~/labplot-env/bin/python`` or ``~/labplot-env/bin/python3``
   - **Windows:** ``%USERPROFILE%\labplot-env\Scripts\python.exe``

4. Click **Apply** and restart LabPlot for the changes to take effect

The configured virtual environment will be used for all Python scripting in LabPlot until you change the setting back to the default (empty path uses the bundled Python).

**For System Python Installations (Linux Package Managers)**

When LabPlot is installed via a Linux distribution's package manager (zypper, apt, dnf, pacman, etc.), it typically uses the system's Python interpreter. In this case, Python packages should be installed using your distribution's package manager rather than pip directly:

.. code-block:: bash

   # openSUSE/SUSE
   sudo zypper install python3-numpy python3-scipy python3-pandas

   # Debian/Ubuntu
   sudo apt install python3-numpy python3-scipy python3-pandas

   # Fedora/RHEL
   sudo dnf install python3-numpy python3-scipy python3-pandas

   # Arch Linux
   sudo pacman -S python-numpy python-scipy python-pandas

This approach ensures:

- **Compatibility:** Packages are tested and compatible with your distribution
- **System integration:** Packages are managed alongside other system updates
- **No conflicts:** Avoids mixing pip and system package manager installations

If you prefer to use pip with the system Python (for packages not available in your distribution's repositories), use the ``--user`` flag to install into your user directory without requiring root privileges:

.. code-block:: bash

   pip3 install --user <package-name>

.. warning::
   Avoid using ``pip.main(['install', 'package', '--user'])`` from within LabPlot when using system Python, as it may cause conflicts with system-managed packages. Instead, install packages from the terminal using your distribution's package manager or ``pip3 install --user`` before running LabPlot.

Alternatively, you can configure LabPlot to use a virtual environment (see Option 2 above) to keep your LabPlot Python packages completely separate from the system Python.

Checking Installed Packages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To verify which packages are available in your current Python environment, you can run:

.. code-block:: python

   import sys
   import pkg_resources

   print("Python executable:", sys.executable)
   print("\nInstalled packages:")

   for package in sorted(pkg_resources.working_set, key=lambda x: x.key):
       print(f"  {package.key} ({package.version})")

To check if a specific package is installed and its location:

.. code-block:: python

   try:
       import numpy
       print("NumPy version:", numpy.__version__)
       print("NumPy location:", numpy.__file__)
   except ImportError:
       print("NumPy is not installed")

Platform-Specific Notes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Summary by Installation Type**

The installation method varies based on how LabPlot was installed:

- **Bundled Python** (macOS, Windows, AppImage, Flatpak): Use ``pip.main(['install', 'package', '--user'])`` from within LabPlot
- **System Python** (Linux package managers): Use your distribution's package manager or ``pip3 install --user`` from the terminal

**Using System-Wide Packages (AppImage and Flatpak with Bundled Python)**

Linux package formats like AppImage and Flatpak have sandboxed Python environments that don't automatically access system-wide installed packages. If you prefer to use packages already installed on your system rather than installing them into the bundled environment, you have several options:

*For AppImage:*

Set the ``PYTHONPATH`` environment variable to include your system's site-packages directory before launching:

.. code-block:: bash

   export PYTHONPATH=/path/to/site-packages:$PYTHONPATH
   ./labplot-<version>.AppImage

Alternatively, extract the AppImage and use its included Python environment:

.. code-block:: bash

   ./labplot-<version>.AppImage --appimage-extract
   # Then navigate to the extracted directory to access the Python environment

*For Flatpak:*

Grant LabPlot access to your system's site-packages directory:

.. code-block:: bash

   flatpak override --filesystem=/path/to/site-packages org.kde.LabPlot

Or use the graphical tool **Flatseal** for a user-friendly interface:

1. Open Flatseal
2. Select **org.kde.LabPlot** from the list of applications
3. Navigate to the **Filesystem** section
4. Under **Other Files**, click the **+** button
5. Enter the path to your system's site-packages directory (e.g., ``/usr/lib/python3.x/site-packages``)
6. The changes are automatically saved

You can also install packages directly into the Flatpak environment:

.. code-block:: bash

   flatpak run --command=pip3 org.kde.LabPlot install <package-name>

.. note::
   After installing new packages or changing the Python environment setting, it is recommended to restart LabPlot to ensure the packages are properly recognized in the Python scripting environment.
