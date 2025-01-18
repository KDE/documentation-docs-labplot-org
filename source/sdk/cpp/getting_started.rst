Getting Started
===================

############
Installation
############

The LabPlot C++ SDK is included with a LabPlot installation. Please refer to the official LabPlot `website <https://labplot.org/download/>`_ for how to get a LabPlot installation for your respective system.

#####
CMake
#####

The LabPlot C++ SDK provides a shared library CMake target. After installation, the CMake target can be accessed from your CMakeLists.txt file as shown below:

.. code-block:: cmake

    find_package(LabPlot REQUIRED COMPONENTS SDK)
    target_link_libraries(<your-target> LabPlot::SDK)
