<h3>Kill Process</h3>

```
kill PID
```
PID stands for "process ID". Every process that's running on your machine has a unique ID. The ps, "process status" command can be used to list the processes running on your machine, and their IDs:
```
ps aux
```
The "aux" options just mean "show all processes, including those owned by other users, and show extra information about each process".

<p>
  You can find a process ID for a specific program and then kill the process or use the killall command along with the process name.
</p>

```
ps aux | grep [program (relative / absolute path)]
====
kill [PID number]
or
killall [process name]
```

You can also use flags to specify the signal type that you wish to process. Use `kill -l` to view signal types.
