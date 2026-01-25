.. meta::
   :description: A description of LabPlot's SDK.
   :keywords: LabPlot, documentation, user manual, data analysis, data visualization, curve fitting, open source, free, help, learn, c++, cpp, sdk
   :authors: - LabPlot Team

.. _sdk:

SDK
===================

The objective of LabPlot's Software Development Kit (SDK) is to enable the utilization of LabPlot's core functionalities in external projects. This SDK can be employed to integrate LabPlot's algorithms into one's own projects or to automate tasks such as batch importing multiple files, processing and visualizing them, and exporting them as vector graphics. The SDK comprises a shared library, Python wrappers and this documentation.

.. important::
   Note, this part of LabPlot is still considered experimental. Consequently, there is no assurance regarding the stability of the API or the ABI at present.

Below is a small demo to get an impression about what is possible showing how to import a text file, how to visualize the imported data in a histogram, how to perform a distribution fit and how to export the final result to PDF:

.. tabs::

   .. tab:: C++

      .. code-block:: cpp

         #include <QApplication>
         #include <labplot.h>

         int main(int argc, char** argv) {
            QApplication app(argc, argv);

            // create a spreadsheet and import the data into it
            auto* spreadsheet = new Spreadsheet(QStringLiteral("data"));
            AsciiFilter filter;
            filter.readDataFromFile(QStringLiteral("data.txt"), spreadsheet);

            // create a worksheet
            auto* worksheet = new Worksheet(QStringLiteral("worksheet"));

            // create a plot area and add it to the worksheet
            auto* plotArea = new CartesianPlot(QStringLiteral("plot area"));
            plotArea->setType(CartesianPlot::Type::FourAxes);
            plotArea->addLegend();
            worksheet->addChild(plotArea);

            // create a histogram for the imported data and add it to the plot area
            auto* histogram = new Histogram(QStringLiteral("histogram"));
            histogram->setNormalization(Histogram::Normalization::ProbabilityDensity);
            histogram->setDataColumn(spreadsheet->column(0));
            plotArea->addChild(histogram);

            // perform a fit to the raw data and show it
            auto* fitCurve = new XYFitCurve(QStringLiteral("fit"));
            fitCurve->setDataSourceType(XYAnalysisCurve::DataSourceType::Histogram);
            fitCurve->setDataSourceHistogram(histogram);
            plotArea->addChild(fitCurve);

            // initialize the fit
            auto fitData = fitCurve->fitData();
            fitData.modelCategory = nsl_fit_model_distribution;
            fitData.modelType = nsl_sf_stats_gaussian;
            fitData.algorithm = nsl_fit_algorithm_ml; // ML distribution fit
            XYFitCurve::initFitData(fitData);
            fitCurve->setFitData(fitData);

            // perform the actual fit
            fitCurve->recalculate();

            // apply the theme "Dracula"
            worksheet->setTheme(QStringLiteral("Dracula"));

            // export the worksheet to PDF
            worksheet->exportToFile(QStringLiteral("result.pdf"), Worksheet::ExportFormat::PDF);
         }

   .. tab:: Python

      .. code-block:: python

         from labplot import *

         # create a spreadsheet and import the data into it
         spreadsheet = Spreadsheet("data")
         filter = AsciiFilter()
         filter.readDataFromFile("data.txt", spreadsheet)

         # create a worksheet
         worksheet = Worksheet("worksheet")

         # create a plot area and add it to the worksheet
         plot_area = CartesianPlot("plot area")
         plot_area.setType(CartesianPlot.Type.FourAxes)
         plot_area.addLegend()
         worksheet.addChild(plot_area)

         # create a histogram for the imported data and add it to the plot area
         histogram = Histogram("histogram")
         histogram.setNormalization(Histogram.Normalization.ProbabilityDensity)
         histogram.setDataColumn(spreadsheet.column(0))
         plot_area.addChild(histogram)

         # perform a fit to the raw data and show it
         fit_curve = XYFitCurve("fit")
         fit_curve.setDataSourceType(XYAnalysisCurve.DataSourceType.Histogram)
         fit_curve.setDataSourceHistogram(histogram)
         plot_area.addChild(fit_curve)

         # initialize the fit
         fit_data = fit_curve.fitData()
         fit_data.modelCategory = nsl_fit_model_distribution
         fit_data.modelType = nsl_sf_stats_gaussian
         fit_data.algorithm = nsl_fit_algorithm_ml  # ML distribution fit
         XYFitCurve.initFitData(fit_data)
         fit_curve.setFitData(fit_data)

         # perform the actual fit
         fit_curve.recalculate()

         # apply the theme "Dracula"
         worksheet.setTheme("Dracula")

         # export the worksheet to PDF
         worksheet.exportToFile("result.pdf", Worksheet.ExportFormat.PDF)

.. figure:: sdk/images/SDKSamplePlot.png
    :align: center
    :width: 450px

The section :ref:`sdk_concepts` provides an overview of the main concepts and components of the SDK. The details on the installation and the documentatio of the API for C++ and Python can be found under the :ref:`sdk_cpp` and :ref:`sdk_python` sections, respectively. The section :ref:`sdk_examples` contains numerous illustrative examples that demonstrate the application of the SDK.

.. toctree::
   :maxdepth: 1
   :caption: Contents:
   :glob:

   sdk/concepts
   sdk/cpp
   sdk/python
   sdk/examples