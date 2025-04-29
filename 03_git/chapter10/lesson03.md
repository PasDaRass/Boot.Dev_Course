<h3>Git Push</h3>
The git push command pushes (sends) local changes to any "remote" - in our case, GitHub. For example, to push our local main branch's commits to the remote origin's main branch we would run:

```
git push origin main
```
You need to be authenticated with the remote to push changes, which you should have done in the last lesson.

<h3>Alternative Options</h3>
You can also push a local branch to a remote with a different name:
```
git push origin <localbranch>:<remotebranch>
```
It's less common to do this, but nice to know.

You can also delete a remote branch by pushing an empty branch to it:
```
git push origin :<remotebranch>
```
