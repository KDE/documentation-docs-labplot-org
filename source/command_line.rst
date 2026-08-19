.. _command_line:

############################
Command-Line Interface (CLI)
############################

LabPlot can be run from the command line for automation, batch processing, and integration with CI/CD pipelines. This enables headless operation without the GUI, making it ideal for scripting and server environments.

************************
Command-Line Parameters
************************

Input/Output Options
=====================

.. option:: --input <file>

   Input data file (CSV, HDF5, FITS, etc.) or project file (.lml). Can also be provided as a positional argument.

.. option:: --output <file>

   Output file for export. Auto-exports the first worksheet in the project. File extension determines format unless ``--format`` is specified.

.. option:: --export-worksheet <name>

   Export a specific worksheet by name (useful when a project contains multiple worksheets).

.. option:: --export-all

   Export all worksheets in the project. Requires ``--output-dir`` to specify where to save files.

.. option:: --output-dir <directory>

   Output directory for multiple exported files (used with ``--export-all``).

Format Control
===============

.. option:: --format <type>

   Output format: ``pdf``, ``png``, ``svg``, or ``eps``. Auto-detected from output file extension if not specified.

.. option:: --dpi <value>

   Output resolution in DPI for raster formats (PNG). Default: 300.

Plot Customization
===================

.. option:: --template <file>

   Apply a plot style template (``.labplot_template`` file). Templates define colors, line styles, axis formatting, grids, legend position, and other styling. When used with CSV import, data curves are automatically added to the template plot.

.. option:: --title <text>

   Set the plot title.

.. option:: --xlabel <text>

   Set the X-axis label.

.. option:: --ylabel <text>

   Set the Y-axis label.

Execution Mode
===============

.. option:: --no-gui

   Run in headless mode without GUI. The application exits after operations complete. Required for automation and scripting.

.. option:: --no-splash

   Disable splash screen (GUI mode only).

.. option:: --presenter

   Start in presenter mode (GUI mode only).

*******************
Usage Examples
*******************

Quick CSV to Plot Export
=========================

Import a CSV file, auto-create a plot, and export to PNG:

.. code-block:: bash

   labplot data.csv --output plot.png --no-gui

LabPlot automatically uses the first column as X-axis data and creates curves for all remaining columns.

Custom Labels and High-Resolution Export
=========================================

Export a plot with custom labels and high DPI for publication:

.. code-block:: bash

   labplot data.csv --output figure1.pdf \
     --title "Temperature vs Time" \
     --xlabel "Time (s)" \
     --ylabel "Temperature (°C)" \
     --dpi 600 --no-gui

Apply Template Styling
=======================

Load a style template and apply it to imported data:

.. code-block:: bash

   labplot data.csv --template ~/publication_style.labplot_template \
     --output plot.pdf --no-gui

Templates allow consistent styling across multiple figures. They can be created in the GUI via **Plot Area** → **New from Template** → **Save Template**.

Batch Export from Project
==========================

Export all worksheets from a project file to individual SVG files:

.. code-block:: bash

   labplot analysis.lml --export-all --output-dir ./exports \
     --format svg --no-gui

This creates one SVG file per worksheet in the ``./exports`` directory.

Export Specific Worksheet
==========================

Export a specific worksheet from a project:

.. code-block:: bash

   labplot project.lml --export-worksheet "Results Plot" \
     --output results.png --dpi 150 --no-gui

Template with Custom Labels
============================

Combine template styling with runtime label customization:

.. code-block:: bash

   labplot data.csv --template corporate_theme.labplot_template \
     --title "Q4 Sales Data" --xlabel "Month" --ylabel "Revenue ($)" \
     --output report.pdf --no-gui

********************
Automation Workflows
********************

CI/CD Integration
=================

Generate plots during continuous integration or deployment:

.. code-block:: bash

   #!/bin/bash
   # Generate test result plots in CI pipeline

   for datafile in test_results/*.csv; do
       basename=$(basename "$datafile" .csv)
       labplot "$datafile" \
         --template ci_template.labplot_template \
         --title "Test Run: $basename" \
         --output "plots/${basename}.png" \
         --no-gui || exit 1
   done

Batch Processing
================

Process multiple data files with consistent styling:

.. code-block:: bash

   #!/bin/bash
   # Process all CSV files in a directory

   for file in data/*.csv; do
       output="results/$(basename "$file" .csv).pdf"
       labplot "$file" \
         --template style.labplot_template \
         --output "$output" --dpi 300 --no-gui
       echo "Processed: $file → $output"
   done

Automated Reporting
====================

Generate daily reports from sensor data:

.. code-block:: bash

   #!/bin/bash
   # Daily temperature monitoring report

   DATE=$(date +%Y-%m-%d)

   labplot "sensor_data_${DATE}.csv" \
     --title "Temperature Monitoring - ${DATE}" \
     --xlabel "Time (hours)" \
     --ylabel "Temperature (°C)" \
     --template monitoring_template.labplot_template \
     --output "reports/temp_${DATE}.pdf" \
     --dpi 300 --no-gui

*******************
Exit Codes
*******************

LabPlot returns specific exit codes for scripting integration:

.. list-table::
   :header-rows: 1
   :widths: 10 30

   * - Code
     - Meaning
   * - 0
     - Success
   * - 1
     - General error
   * - 2
     - Invalid command-line argument
   * - 3
     - File not found
   * - 4
     - Export failed
   * - 5
     - Project load failed
   * - 6
     - Template application failed
   * - 8
     - Worksheet not found

Example script with error handling:

.. code-block:: bash

   #!/bin/bash

   labplot data.csv --output plot.png --no-gui
   EXIT_CODE=$?

   if [ $EXIT_CODE -eq 0 ]; then
       echo "Success!"
   elif [ $EXIT_CODE -eq 3 ]; then
       echo "Error: Input file not found"
   elif [ $EXIT_CODE -eq 4 ]; then
       echo "Error: Export failed"
   else
       echo "Error: Operation failed with code $EXIT_CODE"
   fi

   exit $EXIT_CODE

*******************
File Formats
*******************

Supported Input Formats
========================

- **Data files**: CSV, TSV, HDF5, NetCDF, FITS, ROOT, Apache Arrow/Parquet, ORC, Matlab MAT, Excel (XLSX), JSON, and more
- **Project files**: ``.lml`` (LabPlot native format)

Supported Output Formats
=========================

- **PDF**: Vector format, ideal for publications and printing
- **SVG**: Vector format, editable in Inkscape/Illustrator
- **PNG**: Raster format with transparency support
- **EPS**: Not directly supported; use PDF or SVG instead

*********************
Notes and Limitations
*********************

- **Auto-plot behavior**: When importing CSV files, LabPlot automatically creates a plot using the first column as X-axis and all remaining columns as Y-axis curves.
- **Template compatibility**: When using ``--template``, the auto-plot is skipped and data curves are added directly to the template plot.
- **Headless requirement**: The ``--no-gui`` flag is required when using ``--output``, ``--export-worksheet``, or ``--export-all`` for automation scenarios.
- **Project structure**: LabPlot projects can contain multiple worksheets, spreadsheets, and matrices. Use ``--export-worksheet`` or ``--export-all`` to control which worksheets are exported.
