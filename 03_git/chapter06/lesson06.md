Here's a diagram of a fast-forward merge, the simplest type of merge in git. <br />
Before:
```
      C     other_branch
     /
A - B       main
```
other_branch has all the commits that main has, Git automatically does a fast-forward merge.<br />
It just moves the pointer of the "base" branch to the tip of the "feature" branch:
<p>After git merge other_branch:</p>

```
            other_branch
A - B - C   main
```
No merge commit is created.
