<h3>stdin</h3>
"Standard Input", usually called "standard in" or "stdin", is the default place where programs read their input. It's just a stream of data that programs can read from as they run.
<p>
  
All major programming languages provide a simple way to read from stdin. In Python, it's the input function:
</p>

```
# execution stops until the user types
# something (in this case "Lane") and presses enter
name = input("What is your name? ")

print("Hello,", name)
# Hello, Lane!
```
