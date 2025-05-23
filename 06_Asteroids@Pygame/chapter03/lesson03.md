Bullets:
<ul>
  <li>
    
Are small circles
  </li>
  <li>
    
Move at a constant speed in a straight line
  </li>
  <li>
    
Split up asteroids when they collide with them
  </li>
  <li>
Are spawned by player input (spacebar) and move in the direction the player is facing
    
  </li>
</ul>

Create a new Shot class to represent a bullet. It should also inherit from CircleShape so that it can use our collision detection code. <br /> 
It should look very similar to our Asteroid class in that it will be drawn and have its position updated. <br /> 
Use a new SHOT_RADIUS constant and set it to 5. <br />
Set up a new group in your initialization code that contains all of your shots. <br />
Add PLAYER_SHOOT_SPEED to your constants file, with a value of 500. <br /><br />

In your Player class, add a new method called shoot. This method should:
<ol>
  <li>
    
Create a new shot at the position of the player
  </li>
  <li>
Set the shot's velocity: <br />
Start with a pygame.Vector2 of (0, 1) <br />
.rotate() it in the direction the player is facing <br />
Scale it up (multiply by PLAYER_SHOOT_SPEED) to make it move faster <br />
Inside your Player class, handle the spacebar (pygame.K_SPACE) and call the shoot method when it is pressed. <br />
    
  </li>
</ol>
