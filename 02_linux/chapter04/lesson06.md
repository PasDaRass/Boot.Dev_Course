You can view all of the environment variables that are currently set in your shell with the env command.

To set a variable in your shell, use the export command:
```
export NAME="Lane"
```
To remove the variable from your environment, use the unset command:
```
unset NAME
```
You can then use the variable in your shell, just as before:
```
echo $NAME
# Lane
```

The interesting part is that programs and scripts you run in your shell can also use that variable:

For example, we can create a file called introduce.sh with the following contents:
```
#!/bin/sh
echo "Hi I'm $NAME"
```
Then we run it:
```
chmod +x ./introduce.sh

./introduce.sh
# Hi I'm Lane
```
