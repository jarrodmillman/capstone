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

************
Introduction
************

* General pattern of work: explore; write tests; write code; have code
  reviewed and merged; repeat.
* Dividing into groups;
* Revision on git, github, pull requests.
* Editors;
* Getting help:

    * Python docs at https://docs.python.org;
    * IPython tab completion, `something?`, `something??`;
    * `np.lookfor`;
    * your search engine (sigh).

*********
Exercises
*********

#. Installing Python 3, pip;

   * install Python 3 / pip as necessary.

#. Working with forks and remotes; making feature branches; making pull
   requests;

   * forking the repo; cloning the repo; adding the remotes; make feature
     branch ``edit-readme``; edit the README, make a pull request.

#. Introduction to `Restructured Text
   <http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html>`_.
   ReST in `Sphinx <http://www.sphinx-doc.org/>`_;

   * make feature branch ``rst-readme``; edit ``README.rst``; install
     ``docutils``; check rendering with ``rst2html.py``; add; commit.  Check
     rendering on github.  Do pull request (PR).

#. Starting from ``origin/master``;

   * get merged changes from github; make new feature branch
     ``add-requirements`` starting at the merged state.

#. Introduction to virtualenvs and virtualenvwrapper;

   * install virtualenvwrapper; create ``ols`` virtualenv.

#. Pip installs, requirements files:

   * install numpy; feature branch (FB) ``add-requirements``; specify in
     requirements file, add ``requirements.txt`` file, commit, do PR.

#. The Python path; Python packages;

   * create package structure for ``ols`` package.  Show you can ``import
     ols``.  Add some explanatory text in init file.  Import ``ols`` again to
     show docstring.  Change into another directory and try import.  Fix.
     Make FB ``package-structure``; add and commit; do PR.

#. The ``.gitignore`` file;

   * add ``.gitignore`` file to FB ``add-gitignore``;  Commit, PR.

#. The `setup.py <https://docs.python.org/3/distutils/setupscript.html>`_
   file; installing in pip develop mode:

   * create ``setup.py`` for ``ols``, pip install in develop mode.  Show that
     you can now import from anywhere.  Make FB ``add-setup``. Commit; do PR.

#. The explore phase. Reminder about ordinary least squares fitting for model
   $Y = X B + E$. See `GLM intro
   <http://www.jarrodmillman.com/rcsds/lectures/glm_intro.html>`_;

   * in IPython, recreate psychopathy $Y$, clamminess $\vec{x}$.  Create $X$.
     Fit model and find coefficients $B$.

#. Test first development; `pytest <http://pytest.org>`_; comparing arrays;
   typical imports such as ``import numpy as np``:

   * FB ``add-test-fit``. Install pytest with pip.  Add to requirements.  Make
     a test for a new function ``ols.model.fit`` testing that that you can
     reconstruct parameters from the `GLM intro`_.  Run the test and make sure
     it fails.  Write the function ``fit`` in ``ols/model.py``.  Commit, do
     PR.

#. Floating point, almost equal

   * FB ``close-tests``. Test that results are close to expected.  Do PR.

#. Numpy and almost equal;

   * FB ``np-testing``; use ``np.testing`` to do the almost equal test.  Document your
     testing procedure in the README.

#. Importing from the top level:

   * FB: ``top-level-imports``.  How do you import ``fit`` directly from
     ``ols``?  As in ``from ols import fit``?  Do PR.

#. Remember the README:

   * FB ``document-testing``. Document the testing procedure so someone else
     can reproduce it.

#. Check collaboration / replication.

   * Start in a new directory; make a new virtualenv, and follow the
     instructions in the README exactly, to run the tests.  Fix any problems;
     do a PR.

#. Testing edge cases; reminder on reshape and introduction to ``newaxis``:

   * what happens if you pass a list into the ``fit`` function?  Or a 1D
     array?  FB ``extend-tests``; Make test cases.  Run the tests.  Fix.  What
     happens if the design is rank deficient?  Test.  Fix if necessary.  Do
     PR.

#. Dealing with errors.  Try / except / finally.

   * use try / except to test / confirm that error arises from passing design
     and data of different number of rows.

#. More advanced pytests:

   * see if you can find a neater way to test for errors being raised using
     pytest.

#. Rethinking the design as objects.   The ``Model`` and ``Results`` objects.
   Thinking about the design.

   * write tests for the Model and Results objects.  Run tests and fail.
     Write Model and results objects.

#. Loading text files with numpy.  Working out which directory your test is
   running in.

   * I will add a random X and Y to the repository, and save the expected
     coefficients out as another text file.  Make a feature branch; in the
     tests, load the X and Y, fit the model, test the coefficients against the
     result I got.  Do a PR.

#. Testing against other packages:

   * Load text files from R.  Find model coefficients using ``lm``.  Save from
     R session.  Make test from saved R results. Clue: R command for writing a
     simple text file of numeric values is ``write.table(var, row.names=FALSE,
     col.names=FALSE, file='filename.txt')``.

#. Decorators and properties.

   * write tests for residuals as a property.  Fix tests.
