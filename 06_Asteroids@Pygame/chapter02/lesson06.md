We want the spaceship to be able to move; but what does that mean specifically? Let's break it down:
<ul>
  <li>
    
If we press the move-left key, the ship should rotate to the left.
  </li>
  <li>
    
If we press the move-right key, the ship should rotate to the right.
  </li>
  <li>
    
If we press the move-forward key, the ship should move forward.
  </li>
  <li>
    
If we press the move-backward key, the ship should move backward.
  </li>
</ul>

Create a new constant in constants.py to represent the player's turn speed. I named mine PLAYER_TURN_SPEED, and gave it a value of 300. <br />
Add a new method to the Player class called rotate. It's going to take one argument: dt (I told you we'd use it!). <br />
When it's called, it should add PLAYER_TURN_SPEED * dt to the player's current rotation.<br />
Paste in the following update method to the Player class:
```
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            # ?
        if keys[pygame.K_d]:
            # ?
```
            

If you're using a non-QWERTY keyboard, you may want to change the keybindings in the code to something other than the W, A, S and D keys.

Update the missing lines to call the rotate method with the dt argument. To go left instead of right when a is pressed, you'll need to reverse dt... how can you do that...?
Hook the update method into the game loop by calling it on the player object each frame before rendering.
