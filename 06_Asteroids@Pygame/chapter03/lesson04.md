# Rate Limit
You probably noticed that the weapon on the ship is currently as overpowered as the original Zerg rush. Let's fix that.
<br />
<ol>
  <li>
    
Create a new variable on the Player object to act as a timer. It should start with a value of 0
  </li>
  <li>
    
When the player shoots, set the timer equal to a new constant. I called mine PLAYER_SHOOT_COOLDOWN and used 0.3
  </li>
  <li>
    
Prevent the player from shooting if the timer is greater than 0
  </li>
  <li>
    
Decrease the timer by dt every time update is called on the player
  </li>
</ol>
