*******************************
Collaborative workflow with Git
*******************************

.. contents::


In groups, [1]_ I want you to spend about 5 minutes on each of the
following questions. For most of the questions, you will need to use Git
and GitHub.

While you are discussing things, I will circulate among the groups to
answer questions and observe. After working on each question for 5
minutes in groups, we will have a class discussion for about 5 minutes.

Review (read and discuss in small groups)
-----------------------------------------

So far you’ve only needed to use Git in the most basic way. As you
begin using Git in more advanced ways, you will increasingly need to
have a clear understanding of the underlying model. Otherwise things
will be confusing.

In the (9/7/2014) section on Git, I introduced several concepts.
Before actually doing anything new with Git, take some time to recall
the definition of the following concepts:

#. Working tree

#. Commit

#. Repository

#. Remotes

#. Branch

#. Tag

#. Merge

#. Staging area

#. Pushing and pulling

How do these things relate to the DAG (i.e., directed acyclic graph)
that we talked about in section? Where does hashing come into play?
Why does Git hash? How do the Git commands that you’ve been using
(e.g., status, log, clone, add, commit, push, pull, rm, mv) relate to
these concepts?

Collaboration: remotes and merging (work in pairs)
--------------------------------------------------

Work in pairs for the following. You should each be on your own
computer, but take turns watching each other type and talking through
what you are doing as you work through the questions together.

#. Clone my example stats repository. Change into your local
   repository and view your remotes.

#. Create a new public repository on GitHub called ``stats``. (Make
   sure not to initialize it. Explain why?)

#. Add your GitHub repository as a remote.

#. Push your local repository to your GitHub repository. First,
   verify the status of your repository. Now push the master branch
   of your local repository to your empty repository on GitHub. The
   ``-u`` option will set your master branch of your local repository
   to track remote branch master from my.

   Now check the status of your repository. Did anything change? If
   so, can you explain why?

#. Add your partner’s GitHub repository as a remote.

#. Verify that you can execute the ``stats.R`` file.

#. At this point randomly choose one of you to be person A and the
   other to be person B.

#. Now both of you will edit ``stats.R``.

   You will see ``#!/bin/Rscript`` at the top of your file. I removed
   it above because ``knitr`` wasn’t correctly rendering it.

   -  **(Person A).** Change the following lines from to Then add and
      commit your changes to your local repository. Push your changes
      to GitHub. What remote did you push to? Did you have to
      specify? Why or why not?

   -  **(Person B).** After your partner has completed the above
      steps, change the following line from to Now add and commit
      your changes to your local repository. Push your changes to
      GitHub. What remote did you push to? Did it conflict with what
      Person A did previously? Why or why not?

      Next merge your partner’s changes into your local repository.
      To make the two-steps taken by ``git pull`` explicit, you will
      type ``git fetch`` and ``git merge`` separately. Why did you
      need to specify ``their/master``? What happened to the status?
      What was the most recent commit before and after you did the
      pull (i.e., fetch+merge)?

   -  **(Person A).** Merge your partner’s changes into your local
      repository.

      Why did you need to specify ``their/master``? How come both you
      and Person B typed ``their/master``? Where you referring to the
      same repository/branch? What happened to the status? What was
      the most recent commit before and after you did the pull (i.e.,
      fetch+merge)?

#. Now let’s see what happens when there is a merge conflict. both of
   you will edit ``stats.R``.

   You will see ``#!/bin/Rscript`` at the top of your file. I removed
   it above because ``knitr`` wasn’t correctly rendering it.

   -  **(Person A).** Change the following lines from to Then add and
      commit your changes to your local repository. Push your changes
      to GitHub. What remote did you push to? Did you have to
      specify? Why or why not?

   -  **(Person B).** After your partner has completed the above
      steps, change the following line from to Add and commit your
      changes to your local repository. Push your changes to your
      repository on GitHub.

   -  **(Person A and Person B).** Merge your partner’s changes into
      your local repository.

      Take a closer look to see what’s happening. Git is telling you
      that you have a merge conflict. In other words, Git does not
      know whether ``x`` should be ``1:50`` or ``1:60``. So it wasn’t
      able to automatically merge the changes that Person A and
      Person B did. Instead it added both changes to ``stats.R`` as
      well as some additional mark up to indicate what happened.
      Let’s look at what happened to ``stats.R``.

      Person A should see something like this: Person B should see
      something like this: Make sure you both see something like
      this. Can you see what happened?

      A curious, but common mistake for new users is to just commit
      the file with the text that Git inserted. Why is this a
      mistake?

      Rather than trying to commit the invalid code, you will need to
      resolve the conflict and then commit the resolved code. To
      resolve this merge conflict, you will need to decided what the
      correct code should be. For example, you might want to edit
      your file (using whatever text editor you wish) as follows:

      Once you’ve corrected the file as you wish, [2]_ you can check
      the status to help remind you what you need to do.

      Now use ``git add`` to let Git know you’ve resolved the
      conflict and ``git commit`` to finish the merge.

      Now you should both be able to push your local repository to
      your GitHub remote.

Collaboration: using branches (read and discuss in small groups)
----------------------------------------------------------------

Recall that branches [3]_ are movable labels to a commit. The labels
move forward as you make new commits. When you create a Git
repository, the default branch is given the name ``master``. This is
just a convention (i.e., you can change that name, if you have a good
reason to—you probably don’t).

Why would you use more than one branch? Typically, people use their
``master`` branch to point to the current, bug-vetted, feature
complete version of their project. New features, bug fixes, and
experimental exploration are all done on other branches. Once a
feature is implemented, a bug is fix, or an experimental exploration
pans out, the branch where this work was performed is merged back
into the master branch. The advantage of this is that the ``master``
branch remains in a known, good state. Why might such a pattern of
use be helpful? Would this slow you down? Why or why not?

Now that you’ve recalled what a branch is and started thinking about
what you might use them for, let’s see how you list, create, and
merge branches.

First, to see what branches you have you can type: Imagine you create
a ``testing`` branch. Now you will have two branches. The asterik
``*`` beside the label ``master`` indicates that ``master`` is the
current branch. What does that mean? What will happen if you make a
new commit while on the ``master`` branch?

Before discussing how you change what branch you are currently
working on or learning how to merge branches, it is helpful to
understand a bit about how Git keeps track of what branch you are on.
In Figure [fig:1], you can see a schematic representation of the
situation you are currently in (i.e., you just added your second
branch ``testing`` and now both ``master`` and ``testing`` point to
the same commit).

.. figure:: ../figs/two-branches.png
      :width: 90%
      :alt: Credit: ProGit book, by Scott Chacon, CC License.

      Credit: ProGit book, by Scott Chacon, CC License.

In Figure [fig:2], you will see that ``master`` is
pointed to by ``HEAD``.

.. figure:: ../figs/head-to-master.png
      :width: 90%
      :alt: Credit: ProGit book, by Scott Chacon, CC License.

      Credit: ProGit book, by Scott Chacon, CC License.


To switch to the ``testing`` branch, you type: Does it make sense
that you switch branches by using ``git checkout``? What other
situations would you use ``git checkout``? In particular, can you use
it to switch to commits that are unlabeled? For example, if you had
the repository represented in Figure [fig:2], how would the DAG
change if you typed: How would you use ``git checkout`` to switch to
the ``testing`` branch? What would happen to the DAG if you did that?

If you had the above repository and issued the ``git checkout 34ac2``
command, you would see something like this: Does this message make
sense given what you’ve learned? What do you think it means to be in
a **detached HEAD** state?

Collaboration: using branches (work in pairs)
---------------------------------------------

Work in pairs for the following. You should each be on your own
computer, but take turns watching each other type and talking through
what you are doing as you work through the questions together.

-  **(Person A).** Create a new **feature** branch. [4]_

   Use ``git status`` to see what’s going on. If everything looks
   alright, it’s time to implement your new feature. For this
   feature, you are going to print out the summary information,
   rather than the mean.

   That is, change the line reading so that it reads Now add and
   commit your changes to your local repository.

   Let’s say that you have completed the implementation of your new
   feature and that you’ve fully tested it. Now you will want to
   merge your feature branch back to your master branch. Explain what
   each step does in terms of the underlying DAG. Use
   ``git branch –help`` to see what the option ``-d`` does. How does
   this differ from what ``-D`` does?

   Take a look at the DAG by typing: Finally, push your new changes
   to GitHub.

-  **(Person B).** Create a new **bugfix** branch.

   First pull (i.e., fetch+merge) the work that Person A just pushed
   to their GitHub repository.

   Use git status to see what’s going on. If everything looks
   alright, it’s time to create a bugfix branch and fix the bug.

   First create and checkout a new branch with one command: Verify
   what happened with ``status``. Then replace ``sin`` with ``cos``
   in ``stats.R``. Save your changes, add the changed file to the
   staging area, commit the changes to your repository.

   Next merge your feature branch back to your master branch. Explain
   what each step does in terms of the underlying DAG. Use
   ``git merge –help`` to see what the option ``–no-ff`` does.

   Take a look at the DAG by typing: Can you see a loop that
   represents the work on the feature branch? How does this differ
   from what happened when Person A merged their feature branch?

   If everything looks correct, push your new changes to GitHub.

-  **(Person A).** Make sure you can pull Person B’s changes from
   GitHub. Take a look at the DAG by typing:

-  **(Person A and Person B).** The feature and bugfix above are
   obviously silly. However, in practice, you will often work on new
   features that take a long time to complete. While you are working
   on the feature, you may find that you decide that the feature is
   not as desirable as you first thought. If you work on the feature
   in its own branch, you can discard that work easily without the
   code polluting your main branch of development.

   Similarly, bugfixes themselves may initially seem to require a
   significant amount of new code. However, after thinking about the
   bug longer, you may realize that a much smaller change resolves
   the error. If you were working directly on your main branch, how
   would you simply remove all the unnecessary code changes you made?

   Can you think of other scenarios where isolating code changes to
   separate lines of development would be desirable?

Collaboration: workflow (read and discuss in small groups)
----------------------------------------------------------

At this point, you should have a basic understanding of how to create
and merge branches as well as how to work with collaborators using
multiple remotes. Unlike many older version control systems, Git’s
model is extremely flexible. The inflexibility of older systems
resulted in everyone using the same workflows. The added flexibility
of Git makes it possible to easily use many different types of
workflows. This means that you will have to make a decision about
which workflow you want to use for every project you version control
with Git.

If you are joining an existing project, you will often just adopt the
workflow that that project uses. If you are starting a new project or
working on project where the workflow is being debated, you will need
to understand the benefits and disadvantages of the various
workflows.

This is a complex issue. Often experience will be required in order
to evaluate the merits of different workflows for different projects.
However, there are several basic workflow styles, which you should
understand.

Please read:

-  http://www.git-scm.com/book/en/v2/Git-Branching-Branching-Workflows

-  http://www.git-scm.com/book/en/v2/Distributed-Git-Distributed-Workflows

Once you’ve finished reading the above links, please discuss. Do
these workflows make sense? Can you imagine/explain a scenario where
one workflow might be preferred over another?

For additional information about Git workflows, please see:

-  https://www.atlassian.com/git/tutorials/comparing-workflows

-  https://sandofsky.com/blog/git-workflow.html

-  https://matthew-brett.github.io/pydagogue/gitwash/development_workflow.html

.. [1]
   For two on the questions I will need you to specifically work in
   pairs. Otherwise you are free to work in bigger groups.

.. [2]
   There are also tools to simplify resolving the merge conflict.
   However, for this exercise you should just manually resolve the
   conflict in a text editor.

.. [3]
   | For more information, see
   | http://www.git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell

.. [4]
   You can create and checkout a new branch in one step by typing
   ``git checkout -b feature1``.
