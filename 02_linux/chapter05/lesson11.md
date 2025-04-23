<h3>Interrupt</h3>
Sometimes a program will get stuck and you'll want to stop it. Common reasons for this are:
<br />
<ul>
  <li>
You made a typo in the command and it's not doing what you want
    </li>
  <li>
    It's trying to access the internet but you're not connected
  </li>
  <li>
  It's processing too much data and you don't want to wait for it to finish
    </li>
  <li>
  There is a bug in the program causing it to hang
  </li>
  <li>
    In these cases, you can stop the program by pressing ctrl + c. This sends a "SIGINT" signal to the program, which tells it to stop.
  </li>
</ul>
