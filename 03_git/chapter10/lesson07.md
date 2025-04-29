# My Solo Workflow
When I'm working by myself, I usually stick to a single branch, main. I mostly use Git on solo projects to keep a backup remotely and to keep a history of my changes. I only rarely use separate branches.

<ul>
  <li>
    
Make changes to files
  </li>
  <li>
    
git add . (or git add <files> if I only want to add specific files)
  </li>
  <li>
    
git commit -m "a message describing the changes"
  </li>
  <li>
git push origin main
    
  </li>
</ul>
It really is that simple for most solo work. git log, git reset, and some others are, of course, useful from time to time, but the above is the core of what I do day-to-day.

# My Team Workflow
When you're working with a team, Git gets a bit more involved (and we'll cover more of this in part 2 of this course). Here's what I do:
<ul>
  <li>
    
Update my local main branch with git pull origin main
  </li>
  <li>
Checkout a new branch for the changes I want to make with git switch -c <branchname>
    
  </li>
  <li>
    
Make changes to files
  </li>
  <li>
    
git add .
  </li>
  <li>
    
git commit -m "a message describing the changes"
  </li>
  <li>
    
git push origin <branchname> (I push to the new branch name, not main)
  </li>
  <li>
    
Open a pull request on GitHub to merge my changes into main
  </li>
  <li>
    
Ask a team member to review my pull request
  </li>
  <li>
    
Once approved, click the "Merge" button on GitHub to merge my changes into main
  </li>
  <li>
    
Delete my feature branch, and repeat with a new branch for the next set of changes
  </li>
</ul>
