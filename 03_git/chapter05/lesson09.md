# git log flags

The first is --decorate. It can be one of:
<ul>
  <li>
short (the default)
    
  </li>
  <li>
full (shows the full ref name)
    
  </li>
  <li>
    
no (no decoration)
  </li>
</ul>

Run `git log --decorate=full ` You should see that instead of just using your branch name, it will show the full ref name. 
A ref is just a pointer to a commit. All branches are refs, but not all refs are branches.

Run `git log --decorate=no` You should see that the branch names are no longer shown at all.

The second is `--oneline` This flag will show you a more compact view of the log. I use this one all the time, it just makes it so much easier to see what's going on.
```
git log --oneline
```
