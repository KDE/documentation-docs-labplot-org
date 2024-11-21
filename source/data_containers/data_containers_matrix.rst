.. _data_containers_matrix:

Matrix
===================

.. contents::

Basic Concepts
------------------

:ref:`data_containers_matrix` is another container for matrix-like data. This container is presented like a table or, alternatively, as a two-dimensional greyscale image. The elements of such a table/matrix can be thought as being the$z$-values, $z=z(x,y)$, with $x$ and $y$ values being the row and column numbers, respectively. The transition from the row and column numbers to the logical coordinates is done via an explicit user-defined mapping of both representations.

The matrix data can either be entered manually or via an import from an external file.
Similar to the data generation for a column in a :ref:`data_containers_spreadsheet`, the :ref:`data_containers_matrix` can be filled with constant values or via a formula, too.
