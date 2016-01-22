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

1. Your working environment; editor, git, IPython; pip;

   * exercise; install pip; create ``ols`` repo; note github advice;

1. Introduction to Restructured Text;
1. The fundament is your README;

    * exercise; create ``README.rst``; add, commit.

1. Introduction to virtualenvs and virtualenvwrapper;

   * exercise; create ``ols`` virtualenv

1. Pip installs, requirements files;

   * exercises: install numpy; specify in requirements file, add
     ``requirements.txt`` file, commit.

1. The Python path; Python packages;

   * exercises: create package structure for ``ols`` package.  Show you can
     ``import ols``.  Add some explanatory text in init file.  Import ``ols``
     again to show docstring.  Change into another directory and try import.
     Fix.

1. The ``.gitignore`` file;

    * exercises: add ``.gitignore`` file.  Commit.

1. The ``setup.py`` file; installing in pip develop mode:

   * exercises: create ``setup.py`` for ``ols``, pip install in develop mode.
     Show that you can now import from anywhere.

1. Reminder about ordinary least squares fitting for model $Y = X B + E$.

   * exercise: in IPython, recreate psychopathy $Y$, clamminess $\vec{x}$.
     Create $X$.  Fit model and find coefficients $B$.

1. Test first development; pytest;

    * exercises: install pytest with pip.  Add to requirements.  Make a test
      for a new function ``ols.model.fit`` testing that that you can
      reconstruct parameters from
      http://www.jarrodmillman.com/rcsds/lectures/glm_intro.html. Run the
      test and make sure it fails.  Write the function ``fit``` in
      ``ols/model.py``.


