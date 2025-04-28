# Rebase - new branch

Use the git switch command to create and switch to a new branch, but branch off of the desired commit. <br />
You can supply the commit hash directly to the git switch command:
```
git switch -c update_dune COMMITHASH
```
Replace COMMITHASH with the hash of the desired commit, which you can get with a git log command.

