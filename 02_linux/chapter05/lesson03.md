<h4>Flags</h4>
Flags are options that you can pass to a command to change its behavior.

```
ls -l
```
Or the -a flag to show "all" files, including hidden files:
```
ls -a
```
You can also combine flags:
```
ls -al
```
<h5>Conventions</h5>
Whether or not a command takes flags, and what those flags are, is up to the developer of the command. 
<p>That said there are some common conventions:</p>
<ul>
  <li>
    
Single-character flags are prefixed with a single dash (.e.g -a)
  </li>
  <li>
    
Multi-character flags are prefixed with two dashes (e.g. --help)
  </li>
  <li>
    
Sometimes the same flag can be used with a single dash or two dashes (e.g. -h or --help)
  </li>
</ul>
