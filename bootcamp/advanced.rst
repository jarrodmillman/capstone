#######################
Advanced track bootcamp
#######################

Bootcamp to cover more advanced topics in scientific Python.

*******
Program
*******

We are going to start up using a typical development workflow in Python, using
the example of making a package for ordinary least squares fitting.

To make things clear to our future selves, and other collaborators, we will
document what we are doing as we go.

#. Your working environment; editor, git, IPython; pip;

   * install pip; create ``ols`` repo; note github advice;

#. Introduction to Restructured Text;
#. The fundament is your README;

    * create ``README.rst``; add, commit.

#. Introduction to virtualenvs and virtualenvwrapper;

   * create ``ols`` virtualenv

#. Pip installs, requirements files:

   * install numpy; specify in requirements file, add ``requirements.txt``
     file, commit.

#. The Python path; Python packages;

   * create package structure for ``ols`` package.  Show you can ``import
     ols``.  Add some explanatory text in init file.  Import ``ols`` again to
     show docstring.  Change into another directory and try import.  Fix.

#. The ``.gitignore`` file;

    * add ``.gitignore`` file.  Commit.

#. The ``setup.py`` file; installing in pip develop mode:

   * create ``setup.py`` for ``ols``, pip install in develop mode.  Show that
     you can now import from anywhere.

#. Reminder about ordinary least squares fitting for model $Y = X B + E$.

   * in IPython, recreate psychopathy $Y$, clamminess $\vec{x}$.  Create $X$.
     Fit model and find coefficients $B$.

#. Test first development; pytest; comparing arrays; typical imports such as
   ``import numpy as np``:

    * install pytest with pip.  Add to requirements.  Make a test for a new
      function ``ols.model.fit`` testing that that you can reconstruct
      parameters from
      http://www.jarrodmillman.com/rcsds/lectures/glm_intro.html. Run the test
      and make sure it fails.  Write the function ``fit``` in
      ``ols/model.py``.

#. Floating point, almost equal, numpy testing;

   * test that results are close to expected; use ``np.testing`` to do that
     test.  Document your testing procedure in the README.

#. Collaboration and replication.

   * each group takes the repository of another group.  Make a new virtualenv,
     and follow the instructions in the README exactly, to run the tests on
     the other group's repository.

#. Testing edge cases; reminder on reshape and introduction to ``newaxis``:

   * what happens if you pass a list into the ``fit`` function?  Or a 1D
     array?  Make test cases.  Run the tests.  Fix.  What happens if the
     design is rank deficient?  Test.  Fix if necessary.

#. Dealing with errors.  Try / except / finally.

   * use try / except to test / confirm that error arises from passing design
     and data of different number of rows (see ``pytest.raises`` for a better
     way).

#. Rethinking the design as objects.   The ``Model`` and ``Results`` objects.
   Thinking about the design.

   * write tests for the Model and Results objects.  Run tests and fail.
     Write Model and results objects.

#. Decorators and properties.

    * write tests for residuals as a property.  Fix tests.
