#!/usr/bin/env python
# coding: utf-8

# ### Conditionals and Loops
# 
# These problems review our ideas about conditionals and loops.

# 1. Print out the numbers 1 through 10.

# In[ ]:





# 2. Print out the odd numbers between 1 and 20 by using the third paramter to the `range()` function.

# In[ ]:





# 3. Print out the odd numbers between 1 and 20 by checking if the number is even before printing.

# In[ ]:





# 4. What is the sum of the first 100 integers? Hint: Create a variable `total` equal to zero, and increment `total` inside a loop.

# In[ ]:





# 5. For each friend in your `friends` list, print `"PERSON IS AWESOME!"` in all caps, where `PERSON` is of course replaced with your friend's name.

# In[1]:


friends = ["Alice", "Bob", "Charlie", "Debbie"]


# In[ ]:





# 6. Similar to the last problem, print `"PERSON IS AWESOME!"` for each friend in your friends list _only if their name ends in a vowel_. Otherwise, print `"person is ok..."` (all lowercase). 

# In[ ]:





# 7. For each number between 1 and 30, if a number is divisible by 3, print `"Fizz"`. Otherwise, just print the number.

# In[ ]:





# 8. For each number between 1 and 30, if a number is divisible by 5, print `"Buzz"`. Otherwise, just print the number.

# In[ ]:





# 9. **FIZZBUZZ!** For each number between 1 and 30,
# * if a number is divisible by 3, print `"Fizz"`
# * if a number is divisible by 5, print `"Buzz"`
# * if a number is divisible by both 3 and 5, instead print `"Fizzbuzz"`,
# * otherwise, just print the number
# 
# This problem is the famous "Fizzbuzz" problem - and is a very common interview coding challenge! If you can do this without help, you're making awesome progress! Well done!

# In[ ]:





# 10. Define some string `sentence`. If you can't think of a good one, feel free to use `fact` from the previous notebook.

# In[ ]:





# 11. Count the number of vowels in `sentence` (no, y is not a vowel).
# * _Hint:_ What happens if you loop through a string?

# In[ ]:





# 12. Define a variable `sentence_rm` that is equal to `sentence` with all vowels removed. 
# * _Hint:_ This is a tough one. Start out with an empty string and concatenate all of the consonants to it inside a loop.

# In[ ]:





# 13. Create a variable `fav_number` equal to whatever is your favorite integer. Write a loop to determine if `fav_number` is prime. Recall that a prime number is any number whose only divisors are 1 and itself. For example, 6 is not prime since it's divisible by 1, 2, 3, and 6. But 7 _is_ prime since it's only divisible by 1 and 7.

# In[ ]:





# 14. A palindromic number reads the same both ways. For example, 1234321 is a palindrome. Write an `if` statement to test whether or not a number is palindromic.

# In[ ]:





# 15. Find the largest palindrome made from the product of two two-digit numbers.
# * _Tip:_ Do not worry about the "efficiency" of your answer! The easiest answer is very inefficient.

# In[ ]:





# 16. Here are more heights below. However, this time, the information is contained in a dictionary. Create a list of the names _and ONLY the names_ of the people who are tall enough to ride the roller coaster.
# 
# * _Hint:_ How can you loop through a dictionary?

# In[2]:


people = {
    "Aaron": 58,
    "Barbara": 66,
    "Clarence": 62,
    "Donovan": 55,
    "Erika": 70,
    "Fernando": 72
}


# In[ ]:





# 17. Below we have some more data on our classmates. This time, the dictionary values are test scores. A student's final grade is their _maximum_ score on these three tests. Create a list of the students' final grades.

# In[3]:


people = {
    "Aaron": [87, 52, 78],
    "Barbara": [92, 79, 85],
    "Clarence": [42, 68, 55],
    "Donovan": [95, 100, 87],
    "Erika": [62, 88, 47],
    "Fernando": [84, 99, 0]
}


# In[ ]:





# 18. Repeat the above problem, except create a _dictionary_ of the final scores, where the dictionary keys are the names, and the dictionary values are the final grade.
# 
# 

# In[ ]:





# 19. Using the two lists defined below, create the following resulting list:
# 
# `["AZ", "BY", "CX", "DW", "EV"]`
# 
# * _Hint:_ Check out the `zip()` function.

# In[4]:


letters_a = ["A", "B", "C", "D", "E"]
letters_z = ["Z", "Y", "X", "W", "V"]


# In[ ]:





# 20. Using `letters_a` defined in the previous problem, create the following list:
# 
# ```
# [
#     "A is letter 1 of the alphabet",
#     "B is letter 2 of the alphabet",
#     ...
# ]
# ```
# 
# * _Hint:_ Checkout the `enumerate()` function.

# In[ ]:





# ### Functions
# In this section, every question gives example(s). You can (but don't need to) name your function accordingly. You _should_ test out the example to make sure your function works properly. If the example doesn't work, your answer is likely incorrect.

# 21. Write a function to compute the area of a triangle. You only need the base and height of a triangle to compute its area.
# 
# * _Example:_ `area_triangle(5, 4) == 10.0`

# In[ ]:





# 22. Write a function that takes in a number `max_num` and returns the sum of the numbers 1 through `max_num` (inclusive).
# * _Example:_ `sum_n(5) == 1 + 2 + 3 + 4 + 5 == 15`

# In[ ]:





# 23. Write a function that takes in a number `max_num` and returns the sum of the square of the numbers 1 through `max_num` (inclusive).
# * `sum_squares(5) == 1 + 4 + 9 + 16 + 25 == 55`

# In[ ]:





# 24. Write a function that takes a number (an amount in euros) and convert it to U.S. dollars. There are 1.1 U.S. dollars per euro.
# * `to_dollar(10) == 11.0`

# In[ ]:





# 25. Write a function that takes a list of numbers (amounts in euros), and returns them converted to dollars. Use your answer to the previous question in your answer to this question.
# * _Example:_ `to_dollar_list([1, 10, 100]) == [1.1, 11.0, 110.0]`
# * _Note:_ You may get some decimal weirdness here.

# In[ ]:





# 26. Write a function that takes a number (a person's height) and returns "Tall enough" if they are at least 5 feet (60 inches) or "Too short" if they are below 5 feet.
# * _Example:_ `is_tall(72) == 'Tall enough'`
# * _Example:_ `is_tall(52) == 'Too short'`

# In[ ]:





# 27. Write a function that takes a list of numbers (peoples' heights) and returns a list of strings "Tall enough" or "Too short" as in the previous problem. Use your answer to the previous problem to help answer this problem.
# * _Example:_ `is_tall_list([58, 70, 60]) == ['Too short', 'Tall enough', 'Tall enough']`

# In[ ]:





# 28. Write a function that takes in a numeric grade (0 to 100) and returns the letter grade (no pluses or minuses). In a traditional rubric, that would be as follows:
# 
# * 90 or above = A
# * 80 - 89 = B
# * 70 - 79 = C
# * 60 - 69 = D
# * 59 or below = F
#     
#     
# * _Example:_ `letter_grade(85) == 'B'`

# In[ ]:





# 29. Write _another_ function that takes a list of numeric grades and returns their letter grades. Use the function written above in your answer.
# 
# * _Example:_ `letter_grades([85, 62, 90]) == ['B', 'D', 'A']`

# In[ ]:





# 30. Head over to [codewars.com](https://www.codewars.com/) and create an account.  You don't need to receive emails or anything like that but be sure to choose the Python language and head over to the practice area.  Find a coding challenge that you feel capable of solving (higher kata is easier and you can sort from easiest to hardest).  After solving the problem, add a markdown cell below with the problem prompt, and add the code below to demonstrate the solution.  We will share these in small groups at the start of next class.

# In[ ]:





# 
