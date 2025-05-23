We need collision detection. Now, this is a fairly deep topic, but we're going to keep things simple: we'll treat everything (including our triangular ship) as a circle when it comes to collisions.
<br />
Detecting a collision between two circles is simple:
<ul>
  <li>
    
We calculate the distance between the center of the two circles, let's call it distance
  </li>
  <li>
    
Let's call the radius of one circle r1, and the radius of the other circle r2
  </li>
  <li>
If distance is less than or equal to r1 + r2, the circles are colliding. If not, they aren't.
    
  </li>
</ul>

Everything that collides inherits from CircleShape, so that seems like a good place to put collision logic.
<br />
<ol>
  <li>
    
Add another method to that class to check for collisions. It should take 1 argument (another CircleShape object) and return True or False.
  </li>
  <li>
    
Each CircleShape's position property is a pygame.Vector2. Use its distance_to method to calculate the distance between the two shapes.
  </li>
  <li>
    
After the update step in your game loop, iterate over all of the objects in your asteroids group. Check if any of them collide with the player. If a collision is detected, the program should print Game over! and immediately exit the program.
  </li>
</ol>
