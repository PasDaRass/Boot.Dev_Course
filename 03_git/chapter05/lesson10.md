Remember, Git stores all its information in files in the .git subdirectory at the root of your project, even information about branches. <br />
The "heads" (or "tips") of branches are stored in the .git/refs/heads directory. <br />
If you `cat` one of the files in that directory, you should be able to see the commit hash that the branch points to.
