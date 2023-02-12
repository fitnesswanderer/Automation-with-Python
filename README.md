# Automation-with-Python

## Contents
1.Motivation

2.Regular expressions theory
 
3.Regular expressions syntax
 
   
   >3.1 Metacharacters
  
   >3.2 Methods
  
4.Real world scenario examples
 
  >4.1 Strong password detection
  
  >4.2 Find website URLs that begin with http:// or https://.
  
  >4.3 	 Clean up dates in different date formats (such as 7/24/2020, 07-24-2020, 
and 2020/7/24) by replacing them with dates in a single, standard format.

## Motivation
During my freelancing job, there were numerous instances when I had to explain regular expressions to one of my team members to make our work easier.If you are involved in implementing natural language programming, this can be handy as text tokenization using regular expressions. I started to practice simple tasks to get better at it. In addition, I had a data where there was lot of information and I had to extract phone number and email from that data for further processing of data. Regular expressions came to my rescue. Hence, I am sharing my learnings about this topic in a simplified manner.

## Regular expressions theory
Imagine you have an unstructured data from different websites and your job is to find the email and phone number of different businesses and have to share with your boss.Ofcourse, you could do Ctrl+F and keep finding the relevant information but this process sounds quite tedious.In such scenarios, regular expressions are used.A regular expression (RE)allow you to recognize and often extract data from certain patterns of text.RE can be used to check if the string contains the specific pattern of text.

## Regular expressions syntax
Python’s built-in **re** module is responsible for applying regular expressions to strings.

## Metacharacters
![auto](https://user-images.githubusercontent.com/12171326/218261117-57432ebe-d2e0-4b0f-9e5a-f2bb63aeb6a1.JPG)
*Source:https://www.codecademy.com/resources/docs/python/regex/metacharacters*

![auto2](https://user-images.githubusercontent.com/12171326/218261357-40488d32-aaa3-4829-9df1-b1a342ac2aeb.JPG)
*Source:https://www.codecademy.com/resources/docs/python/regex/metacharacters*

Special sequences use \ backslash followed by one of the characters as shown in the image below
![auto3](https://user-images.githubusercontent.com/12171326/218261645-6e9da1bf-07f4-4a13-9db3-713e6a264f69.JPG)
*Source:https://www.codecademy.com/resources/docs/python/regex/metacharacters*

## Methods
![auto4](https://user-images.githubusercontent.com/12171326/218261827-ae929bfb-e41a-4a1a-a255-7541d3b00e97.JPG)

*Source:Python for Data Analysis by Wes Mckinney*



