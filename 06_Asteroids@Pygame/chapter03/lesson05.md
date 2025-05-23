# Destruction
Okay so bullets are flying, but they don't do anything. Let's kill some asteroids!
<br />
There are three types of asteroids:
<ul>
  <li>
Large
    
  </li>
  <li>
    
Medium
  </li>
  <li>
    
Small
  </li>
</ul>

When a large asteroid is destroyed, it should split into two medium asteroids. <br />
When a medium asteroid is destroyed, it should split into two small asteroids. <br />
When a small asteroid is destroyed, it should disappear.
<br /><br />
For now, we'll just always make the asteroids disappear when they're destroyed. We will handle splitting later.
<ul>
  <li>
Add another collision check to the game loop. Loop over each asteroid, and for each asteroid, loop over each bullet. 
    
  </li>
  <li>
    
If a bullet and an asteroid collide, call the .kill() method on both objects to remove them from the game.
  </li>
  <li>
    
The kill() method is a feature built-in to pygame; it will remove the object from all of its groups, so our game will stop drawing and updating it automatically.
  </li>
</ul>

