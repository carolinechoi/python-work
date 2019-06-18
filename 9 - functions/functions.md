## Functions
Using functions, you can divide your code into useful blocks and organize your code. 

### Blocks
<u>block</u>: area of code written in the following format - 

<pre><code>block_head:
    1st block line
    2nd block line
    ...
</code></pre>

Block heads are made of the following format:

<pre><code>block_keyword block_name(argument1, argument2, ...)
</code></pre>

<u>Block keywords:</u> "if", "for", "while"

### Function Blocks

Functions use the block keyword *def* followed with the function's name.

Ex:
<pre><code>def my_function():
    print("Hello world!")
</code></pre>

### Receiving Arguments

Functions can also take and receive arguments.

<pre><code>def my_arguments(username, greeting):
    print("Hello, %s, From My Function!, I wish you %s"%(username, greeting))
</code></pre>

<pre><code>def sum_numbers(a, b, c):
    return a + b + c
</code></pre>

### Calling Functions

<pre><code>def function():
    print("Hello!")
def arguments_function(username, greeting):
    print("Hello %s, you're here, %s"%(username, greeting))
function()
arguments_function("St. Vincent", "yay!")</code></pre>

Just write the function name and the parentheses. 

✨ Note how for the function with arguments, we don't name the arguments until we *call* the function.