In the original game, part of the challenge comes from the fact that larger asteroids split into smaller, faster asteroids when you shoot them. Let's support it!
<p>
  
Instead of calling asteroid.kill() in our game loop, let's call asteroid.split(). This is a new method we'll be writing on the Asteroid class. To start, let's just have the split method call self.kill() like before. This should keep the behavior the same as before, but give us the room to add our splitting logic.
</p>


Add a new .split() method to the Asteroid class. It should:
<ul>
  <li>
    
Immediately .kill() itself (think about it: this asteroid is always destroyed, and maybe we'll spawn new ones)
  </li>
  <li>
    
If the radius of the asteroid is less than or equal to ASTEROID_MIN_RADIUS, just return, this was a small asteroid and we're done <br />
Otherwise, we need to spawn 2 new asteroids... instructions below
  </li>
</ul>
<h5>Spawning New Asteroids</h5>
We want new asteroids to move in new random directions.
<br />
Trajectory of new asteroids, after split.The red arrow is our current velocity, and the dotted white arrows are the trajectories of the new asteroids.
<ol>
  <li>
Import the random module.
    
  </li>
  <li>
    
Use random.uniform to generate a random angle between 20 and 50 degrees. This will be the blue angle on the diagram above.
  </li>
  <li>
    
Use the rotate method on the asteroid's velocity vector to create 2 new vectors, that are rotated by random_angle and -random_angle respectively (they should split in opposite directions).
  </li>
  <li>
    
Compute the new radius of the smaller asteroids using the formula old_radius - ASTEROID_MIN_RADIUS
  </li>
  <li>
Create two new Asteroid objects at the current asteroid position with the new radius.
    
  </li>
  <li>
    
Set the first's velocity to the first new vector, but make it move faster by scaling it up (multiplying) by 1.2
  </li>
  <li>
Do the same for the second asteroid, but with the second new vector.
    
  </li>
</ol>
