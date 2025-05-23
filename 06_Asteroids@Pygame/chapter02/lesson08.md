# Creating and Using Groups

You can create a new empty group like this:
```
my_group = pygame.sprite.Group()
```
To add all instances of a Player to two groups, group_a and group_b in this example, we add a class variable (or static field) <br />
called containers to the class just like so (with literally this one line, you don't need to bother with adding this field to the class declaration): <br />

```
Player.containers = (group_a, group_b)
```

After changing a static field like containers, make sure to create all Player objects after the change. <br />
This way, they will be correctly added to the groups. <br />

You can iterate over objects in a group just like any other collection in Python:

```
for thing in group:
    thing.do_something(some_value)
```

You may also call the .update() method for every member of a group by calling it on the group itself:
```
group.update(dt)
```

Before the game loop starts: <br />


Create two groups in main.py:
<ul>
  <li>
    
updatable - all the objects that can be updated
  </li>
  <li>
drawable - all the objects that can be drawn
    
  </li>
</ul>
Set both groups as containers for the Player. <br />
Change the game loop to use the new groups instead of the Player object directly. <br />
Call the .update() method on the "updatables" group. <br />
Loop over all "drawables" and .draw() them individually. 
