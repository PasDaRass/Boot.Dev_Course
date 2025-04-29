```
git rebase main
```

This will do the following:
<ol>
  <li>
    
Identify the latest commit from main and use it as the temporary new base for the rebase process
  </li>
  <li>
Replay each commit from new_branch one at a time onto this temporary location
    
  </li>
  <li>
    
Update the new_branch branch to point to the last replayed commit in the temporary location, making this the new permanent new_branch.
  </li>
  <li>
The rebase does not affect the main branch; new_branch now includes all changes from main.
    
  </li>
</ol>
