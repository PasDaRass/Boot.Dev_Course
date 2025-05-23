<ol>
  <li>
Add this line to constants.py to define the size of the player's ship:
    
```
PLAYER_RADIUS = 20
```

</li>
  <li>
    
Create a new file called player.py with a Player class that inherits from CircleShape. <br />
  </li>
The Player constructor should take x and y integers as input, then:
  <li>
Call the parent class's constructor, also passing in PLAYER_RADIUS <br />
Create a field called rotation, initialized to 0
    
  </li>
  
Paste this triangle method into your Player class:
  <li>
    
```
# in the player class
def triangle(self):
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
    a = self.position + forward * self.radius
    b = self.position - forward * self.radius - right
    c = self.position - forward * self.radius + right
    return [a, b, c]
```
   
  </li><br />
A player will look like a triangle, even though we'll use a circle to represent its hitbox. The math of drawing a triangle can be a bit fiddly, so we've written the method for you. <br /><br />
<li>
To draw the player, override the draw method of CircleShape. It should take the screen object as a parameter, and call pygame.draw.polygon. It takes: <br />
<br />
<ul>
  <li>
The screen object
    
  </li>
  <li>
    
A color (use "white")
  </li>
  <li>
    
A list of points (use self.triangle() that we provided for you)
  </li>
  <li>
    
A line width (use 2)
  </li>
</ul>    
  
    
  <li>
In your main function, instantiate a Player object. You can pass these values to the constructor to spawn it in the middle of the screen:
    
```
x = SCREEN_WIDTH / 2
y = SCREEN_HEIGHT / 2

```

  </li>
  <li>
Lastly, we need to re-render the player on the screen each frame, meaning inside our game loop. Use the player.draw(screen) method we just added to do so
    
  </li>
</ol>


