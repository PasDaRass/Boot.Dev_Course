The ls command has a -l option (lowercase "L") that will print out the permissions of each file and directory in long format.

List the files in the worldbanc/private directory along with their permissions using ls -l so you can see the current state of affairs.
Change the permissions of the private directory and all of its contents so that:

<ul>
  <li>The owner can read, write, and execute</li>
  <li>The group can do nothing</li>  
  <li>Others can do nothing</li>
</ul>

```
chmod -R u=rwx,g=,o= DIRECTORY
```
