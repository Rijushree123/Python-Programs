#!/usr/bin/env python
# coding: utf-8

# # Using Stack

# In[1]:


# Python3 code to Check for  
# balanced parentheses in an expression 
open_list = ["[","{","("] 
close_list = ["]","}",")"] 
  
# Function to check parentheses 
def check(myStr): 
    stack = [] 
    for i in myStr: 
        if i in open_list: 
            stack.append(i) 
        elif i in close_list: 
            pos = close_list.index(i) 
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])): 
                stack.pop() 
            else: 
                return "Unbalanced"
    if len(stack) == 0: 
        return "Balanced"
    else: 
        return "Unbalanced"
  

# Driver code 
str=input()
print(str,"-", check(str)) 
  
str1=input()
print(str1,"-", check(str1)) 
  
string = "(((}}}})"
print(string,"-",check(string)) 


# # Using Queue

# In[2]:


# Python3 code to Check for  
# balanced parentheses in an expression 
def check(expression): 
      
    open_tup = tuple('({[') 
    close_tup = tuple(')}]') 
    map = dict(zip(open_tup, close_tup)) 
    queue = [] 
  
    for i in expression: 
        if i in open_tup: 
            queue.append(map[i]) 
        elif i in close_tup: 
            if not queue or i != queue.pop(): 
                return "Unbalanced"
    if not queue: 
        return "Balanced"
    else: 
        return "Unbalanced"
  
# Driver code 
string = "{[]{()}}"
print(string, "-", check(string)) 
  
string = "((()"
print(string,"-",check(string)) 


# # Elimination based

# In[4]:


# Python3 code to Check for  
# balanced parentheses in an expression 
def check(my_string): 
    brackets = ['()', '{}', '[]'] 
    while any(x in my_string for x in brackets): 
        for br in brackets: 
            my_string = my_string.replace(br, '') 
    return not my_string 
   
# Driver code 
string = "{[]{()}}"
print(string, "-", "Balanced" 
      if check(string) else "Unbalanced") 


# In[ ]:




