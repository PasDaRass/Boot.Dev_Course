Now instead of rotating, we need the ship to move back and forth with the W and S keys.

<ul>
  <li>
    
Create a new constant in constants.py to represent the player speed. I named mine PLAYER_SPEED, and gave it a value of 200.
  </li>
  <li>
    
Add a new method to the Player class called .move(). It takes one argument: dt. We want to modify the player's position; but first, we need to do a little bit of math.
  </li>
  <li>
    
We start with a unit vector pointing straight up from (0, 0) to (0, 1).
  </li>
  <li>
    
We rotate that vector by the player's rotation, so it's pointing in the direction the player is facing.
  </li>
  <li>
    
We multiply by PLAYER_SPEED * dt. A larger vector means faster movement.
  </li>
  <li>
Add the vector to our position to move the player.
    
  </li>
</ul>

<h5>Vector Math</h5>

This is a course on programming, not vector math, so we've done the math for you. All those words boil down to these two lines of code:
```
forward = pygame.Vector2(0, 1).rotate(self.rotation)
self.position += forward * PLAYER_SPEED * dt
```
Modify the update method in the Player class to call the move method when the W or S keys are pressed.
