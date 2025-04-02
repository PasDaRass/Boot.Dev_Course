The ls command has a -l option (lowercase "L") that will print out the permissions of each file and directory in long format.

List the files in the worldbanc/private directory along with their permissions using ls -l so you can see the current state of affairs.
Change the permissions of the private directory and all of its contents so that:

<li>
  <ul>The owner can read, write, and execute</ul>
  <ul>The group can do nothing</ul>  
  <ul>Others can do nothing</ul>
</li>

```
chmod -R u=rwx,g=,o= DIRECTORY
```
