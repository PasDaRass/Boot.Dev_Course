# Two Ways to Create a Branch
```
git branch my_new_branch
```
This creates a new branch called my_new_branch. The thing is, I rarely use this command because usually I want to create a branch and switch to it immediately. 
So use this command instead:
```
git switch -c my_new_branch
```
<p>
  
The switch command allows you to switch branches, and the -c flag tells Git to create a new branch if it doesn't already exist.
</p>

When you create a new branch, it uses the current commit you are on as the branch base.
