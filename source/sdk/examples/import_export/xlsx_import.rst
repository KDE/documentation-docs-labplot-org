XLSX File Import
===================

An example showing how to import data from an XLSX `file <https://invent.kde.org/education/labplot/-/blob/master/lib/examples/xlsx_import_ex/data.xlsx>`_ into a Spreadsheet.

.. tabs::

   .. tab:: C++

      .. code-block:: cpp

         #include <iostream>
         #include <QApplication>
         #include "labplot.h"

         int main(int argc, char* argv[]) {
             QApplication app(argc, argv);

             XLSXFilter filter;
             filter.setCurrentSheet(QStringLiteral("Sheet1"));
             filter.setCurrentRange(QStringLiteral("A1:D7"));
             filter.setFirstRowAsColumnNames(true);

             Spreadsheet spreadsheet(QStringLiteral("test"), false);

             filter.readDataFromFile(QStringLiteral("data.xlsx"), &spreadsheet, AbstractFileFilter::ImportMode::Replace);

             if (!filter.lastError().isEmpty()) {
                 std::cout << "Import error: " << filter.lastError().toStdString() << std::endl;
                 return -1;
             }

             std::cout << "Number of columns: " << spreadsheet.columnCount() << std::endl;
             std::cout << "Number of rows: " << spreadsheet.rowCount() << std::endl;

             spreadsheet.column(0)->setColumnMode(AbstractColumn::ColumnMode::Text);
             spreadsheet.column(1)->setColumnMode(AbstractColumn::ColumnMode::Integer);
             spreadsheet.column(2)->setColumnMode(AbstractColumn::ColumnMode::Double);
             spreadsheet.column(3)->setColumnMode(AbstractColumn::ColumnMode::Day);

             std::cout << "First Name: " << spreadsheet.column(0)->textAt(1).toStdString() << std::endl;
             std::cout << "Age: " << spreadsheet.column(1)->integerAt(1) << std::endl;
             std::cout << "Height: " << spreadsheet.column(2)->doubleAt(1) << std::endl;
             std::cout << "Date of Birth: " << spreadsheet.column(3)->dateAt(1).toString().toStdString() << std::endl;
         }

   .. tab:: Python

      .. code-block:: python

         from labplot import *

         filter = XLSXFilter()
         filter.setCurrentSheet("Sheet1")
         filter.setCurrentRange("A1:D7")
         filter.setFirstRowAsColumnNames(True)

         spreadsheet = Spreadsheet("test", False)
         filter.readDataFromFile("data.xlsx", spreadsheet, AbstractFileFilter.ImportMode.Replace)

         if filter.lastError():
             print(f"Import error: {filter.lastError()}")
             exit(1)

         print(f"Number of columns: {spreadsheet.columnCount()}")
         print(f"Number of rows: {spreadsheet.rowCount()}")

         spreadsheet.column(0).setColumnMode(AbstractColumn.ColumnMode.Text)
         spreadsheet.column(1).setColumnMode(AbstractColumn.ColumnMode.Integer)
         spreadsheet.column(2).setColumnMode(AbstractColumn.ColumnMode.Double)
         spreadsheet.column(3).setColumnMode(AbstractColumn.ColumnMode.Day)

         print(f"First Name: {spreadsheet.column(0).textAt(1)}")
         print(f"Age: {spreadsheet.column(1).integerAt(1)}")
         print(f"Height: {spreadsheet.column(2).doubleAt(1)}")
         print(f"Date of Birth: {spreadsheet.column(3).dateAt(1)}")
