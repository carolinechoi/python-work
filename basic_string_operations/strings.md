## Counting Characters

The method **len()** counts the characters in the string. 

Ex:
<pre><code>string = "Hello world!"
print(len(string))</code></pre>

The above code would print 12, as "Hello world!" is 12, including punctuation and spaces. ✨ Note how the thing that goes in the **()** is the string name.

Additionally, you can use the function **.count()** to count the number of times a character appears in a string. 

Ex:
<pre><code>string = "Hello world!"
print(string.count("l"))</code></pre>

This code would give you the number 3, as the character "l" appears 3 times within the string <em>string</em>.

## Indexing Strings

Use stringName**.index()** to find the index number of a letter/punctuation mark.

Ex:
<pre><code>myString = "Take your time!"
printedIndex = myString.index("t")
print(printedIndex)</code></pre>

The above code would return 0 as the first time "t" appears is the first character.

## Changing Case in Strings

The method **title()** capitalizes the string. It appears after the variable. 

Ex: 
<pre><code>("Hello world").title()</code></pre>

✨ Methods have parentheses because they require additional information to run. On the other hand, the function title() doesn't need any additional information and is therefore left empty.

Other methods: 
**upper()**
**lower()**

You can probably guess what those do. 

✨ Note that users cannot be trusted to properly case their names/info, hence the need for these functions.

## Concatenating

concatenating - a fancy word for combining strings

Use the plus symbol to combine strings. 