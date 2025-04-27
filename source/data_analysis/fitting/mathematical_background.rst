.. _mathematical_background:

Mathematical Background
=======================

LabPlot calculates several statistical measures that help to estimate the ``goodness of the fit``.


``Sum of squared errors (SSE)`` Also known as residual sum of squares (RSS) or sum of squared residuals (SSR):

.. math::
   SSE = \sum_{i=1}^n (\bar y - y)^2

``Mean squared error (MSE)``

.. math::
   MSE = \frac{1}{n} \sum_{i=1}^n (\bar y - y)^2

``Root-mean squared error (RMSE)``:

.. math::
   RMSE = \sqrt{MSE}

``Mean absolute error (MAE)``

.. math::
   MSE = \frac{1}{n} \sum_{i=1}^n |\bar y - y|

``Residual mean square (RMS)``

.. math::
   RMS = \frac{SSE}{n-p}

``Residual standard deviation (RSD)``

.. math::
   RSD = \sqrt{RMS}

``Coefficient of determination``

.. math::
   R^2 = 1 - \frac{SSE}{TSS}, \text{ where } TSS = \sum_i (y_i - \hat y)^2 \text{ and } \hat y = \frac 1n \sum_{i=1}^n y_i

``Adjusted coefficient of determination``

.. math::
   R^2_{\text{Adj.}} = 1 - \frac{SSE/(n-1)}{TSS/(n-p-1)} =  1 - (1-R^2) \frac{n-1}{n-p-1}


The implementation of the fitting procedure with bounded parameters follows the implementation in `MINUIT <https://web.archive.org/web/20220119142729/http://seal.web.cern.ch/seal/documents/minuit/mnusersguide.pdf>`_. Using hard limits for the parameters directly during the calculation is challenging, especially while calculating the derivatives. Instead, a transformation to internal parameters that are free from any bounds is performed. This transformation is designed to limit the original (external) parameters to the specified bounds while allowing the internal parameters to take any values.

For both the lower (min) and the upper (max) parameter bounds specified, the mapping between the bounded parameters and the parameters used internally in the calculation is given by:

.. math::
   P_{int} = \arcsin \left( 2\frac{P_{ext} - \min}{\max - \min} - 1 \right)

.. math::
   P_{ext} = \min + \frac{\max - \min}{2} \left( \sin P_{int} + 1 \right)

For single sided limits with only the lower limit available:

.. math::
   P_{int} = \pm \sqrt{ (P_{ext} - \min + 1)^2 - 1}

.. math::
   P_{ext} = \min - 1 + \sqrt{P_{int}^2 + 1}

And similarly for parameters with upper limits only:

.. math::
   P_{int} = \pm \sqrt{ (\max - P_{ext} + 1)^2 - 1}

.. math::
   P_{ext} = \max + 1 - \sqrt{P_{int}^2 + 1}

The transformation introduces additional non-linearity and numerical instabilities, even for linear problems. Therefore, it is recommended to impose limits on the parameters only if really required. Furthermore, for more stable error analysis results, the fit should be re-performed again without any limits once a reasonable minimum was found.
