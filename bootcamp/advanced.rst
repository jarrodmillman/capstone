#######################
Advanced track bootcamp
#######################

Bootcamp to cover more advanced topics in scientific Python.

*******
Program
*******

We are going to start up using a typical development workflow in Python, using
the example of making a package for ordinary least squares fitting.

To practice good documentation, each group will be replicating the work of the
other.

#. Your working environment; editor, git, IPython; pip;

   * exercise; install pip; create ``ols`` repo; note github advice;

#. Introduction to Restructured Text;
#. The fundament is your README;

    * exercise; create ``README.rst``; add, commit.

#. Introduction to virtualenvs and virtualenvwrapper;

   * exercise; create ``ols`` virtualenv

#. Pip installs, requirements files;

   * exercises: install numpy; specify in requirements file, add
     ``requirements.txt`` file, commit.

#. The Python path; Python packages;

   * exercises: create package structure for ``ols`` package.  Show you can
     ``import ols``.  Add some explanatory text in init file.  Import ``ols``
     again to show docstring.  Change into another directory and try import.
     Fix.

#. The ``.gitignore`` file;

    * exercises: add ``.gitignore`` file.  Commit.

#. The ``setup.py`` file; installing in pip develop mode:

   * exercises: create ``setup.py`` for ``ols``, pip install in develop mode.
     Show that you can now import from anywhere.

#. Reminder about ordinary least squares fitting for model $Y = X B + E$.

   * exercise: in IPython, recreate psychopathy $Y$, clamminess $\vec{x}$.
     Create $X$.  Fit model and find coefficients $B$.

#. Test first development; pytest; comparing arrays;

    * exercises: install pytest with pip.  Add to requirements.  Make a test
      for a new function ``ols.model.fit`` testing that that you can
      reconstruct parameters from
      http://www.jarrodmillman.com/rcsds/lectures/glm_intro.html. Run the
      test and make sure it fails.  Write the function ``fit``` in
      ``ols/model.py``.

#. Floating point, almost equal, numpy testing;

   * exercises: test that results are close to expected; use ``np.testing`` to
     do that test.  Document your testing procedure in the README.

#. Collaboration and replication.

   * exercises: each group takes the repository of another group.  Make a new
     virtualenv, and follow the instructions in the README exactly, to run the
     tests on the other group's repository.

#. Testing edge cases; reminder on reshape and introduction to newaxis:

    * what happens if you pass a list into the ``fit`` function?  Or a 1D
      array?  Make test cases.  Run the tests.  Fix.


