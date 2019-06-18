## Slicing 🍕🍕🍕

To *slice* a string means to cut it down to a segment of your original. There are different ways to slice your strings. 

1. Use **string_name[#:#]**.

For example, in the following code -

<pre><code>astring = "Sweetner"
print(astring[3:5])</code></pre>

- you will be returned with *et*. Note that this slice is printed starting at index 3 and ending at index 4. This makes math within brackets easier for programmers. Think about it this way. 5-3 = 2 & you are returned with 2 characters.

✨ HACKS 🌟
- Only writing *one number* in the brackets will give you the single character at that index.
- Leaving out the *first number* and *keeping the colon* will give you a slice from the start to the number you left in.
- Leaving out the *second number* will give you a slice from the first number to the end.
- Using *negative numbers* will return slices read from the end of the string. -5 would be read as "fifth character from the end". 

2. Use **string_name[#:#:#]**.

This is also called *extended slice syntax*. The general form, as shown above, is [start:stop:step]. 

Ex: 
<pre><code>a_string = "Hello world!"
print(a_string[3:7:2])</code></pre>

The above will return *l*. This is because this prints the characters of the string from 3 to 7 skipping one character. 

Another ex:
<pre><code>b_string = "Ariana Grande"
print(b_string[2:5:3]</code></pre>

This would return *i*. Let's break this down below:

- The first two numbers, 2:4, tell us the excerpt we're looking at. This is *ian*.
- The third number, 3, tells us how many characters we need to skip. Take 3 and subtract 1. This is the number of characters that we're skipping.
- Because *ian* is three characters, the shell returns *i* and skips over the next two characters.

✨ Note: This means that writing code like b_string[2:5:1] would mean nothing because the 1 would reduce to 0 characters skipped.

3. Use **string_name.split()**

This will split your string into a bunch of strings grouped together in a list. The following example splits at the space character.

<pre><code>split_list = "St. Vincent"
print(split_list.split(" "))</code></pre>

4. Reverse Your 🍕

In Python, there is no function to reverse a string. HOWEVER, with the slice syntax below, you CAN.

<pre><code>reverse_string = "Reverse me!"
print(reverse_string[::-1])</code></pre>

5. Uppercase/Lowercase 🍕🍕

This is simple. Use **.upper()** and **.lower()**.

