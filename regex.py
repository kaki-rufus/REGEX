# REGULAR EXPRESSION/PATTERN IS A SEQUENCE OF CHARACTERS THAT DEFINE A SEARCH PATTERN
# used to specify set of strings required for a particular purpose
# /file\d/ - file matches any digit
# \d\d\d -> any 3 characters
# file\d? ---> digits and can repeat the cycle
# /file\d+\.txt/
# (file >> literal, \d >> metacharacter to match any digit, 
# + >> metacharacter to match repetition of preceding character,
# \. >> literal (escaped metacharacter), txt >> literal)

# USES OF REGULAR EXPRESSIONS:
# 1. CHECK IF AN INPUT HONORS A GIVEN PATTERN
# 2. LOOK FOR A PATTERN APPEARANCE IN A PIECE OF TEXT 
# 3. EXTRACT SPECIFIC PORTIONS OF A TEXT: postal code of an address
# 4. REPLACE PORTIONS OF TEXT: change any appearance of color or colour with red
# 5. SPLIT A LARGER TEXT INTO SMALLER PIECES

# COMPONENTS OF OF REGULAR EXPRESSIONS:
#  ---> literals(ordinary characters): these characters carry no special meaning and are processed as it is
#  ---> metacharacters(special characters): characters that carry a special meaning and processed in a special way
#  MEtacharacters are 12 : use \ if you want to treat them as literal 
# (Backslash(\), Caret(^), Dollar sign($), Dot(.), Pipe Symbol(|), Question Mark(?), 
# Asterisk(*), Plus sign(+), Open and Close parenthis (), Opening square brackets([), The opening Curly brace({))

# a) COMPILING REGULAR EXPRESSIONS:
# re.compile(pattern, flags=0)

# b) PERFORMING MATCHES:
# match() -> determine if the RE matches at the beginning of the string
# search() -> Scan through a string, looking for any location where this RE matches
# findall() -> Find all substrings where the RE matches and returns them as a list
# finditer() -> Find all substrings where the RE matches and returns them as an iterator
import re

# a)
# pattern = re.compile("Hello")
# print(pattern) # re.compile(r'Hello', re.UNICODE)

# b)
# match(string[, pos[, endpos]]) : returns an object if a match is found, otherwise None: starts from index 0
pattern = re.compile("hello")
match = pattern.match("hello") #a match, returns an object
no_match = pattern.match("ello hello world") #No match, returns NoneType
yes_match = pattern.match("ello hello world", pos=5)
no_match = pattern.match("ello hello world", pos=5, endpos=9) # theres a match once a position is given 
# print(type(yes_match))
# print(yes_match)

# c) 
# search(string[, pos[, endpos]]): a match is checked throughout the string. same behaviour of pos and endpos
# Returns None if no match found. if a match is found, a Match object is returned

search = pattern.search("say hello")
# print(search) #span = (4, 9) match='hello'

# d) 
# findall(string[, pos[, endpos]]): find all non-overlapping substrings where the match is found
# and returns them as list.
# Same behaviour of pos and endpos as the match() and search() function

findall = pattern.findall("say kaki kaki")
# print(findall)
find_c = re.compile('\d')
find_a = find_c.findall('1, 2, 3 , 9, 10')
# print(find_a)

# finditer (string[, pos[, endpos]]): finds all non-overlapping substrings where the match is found
# and returns them as an iterator of the Match objects.
# Same behaviour of pos and endpos as the match(), findall() and search() function

iter_ptn = re.compile("hello")
matches = iter_ptn.finditer("say hello hello")

for match in matches: #next(matches)
    # print(match)


# match(), search() and finditer() return Match object(s)
# findall() returns list of strings

# YOU CAN DO THE ABOVE USING MODULE LEVEL FUNCTIONS:
    mlf = re.findall("hello", "say hello hello") #pattern then the text in which you want to do searching

# IMPORTANT EXAMPLE:
    txt = "This book costs $15."  #search for the pattern $15
pattern = re.compile('$15')
pattern.search(txt) == None # returns True since $ is a metacharacter (needs to be escaped)

# pattern = re.compile('\$15')

# CHARACTER CLASS:
# from utils import highlight_regex_matches
txt = """"
Yesterday, I was driving my car without a driving licence. The traffic police stopped me and license
.I told them that i forgot my licence at home.
"""

pattern = re.compile("licen[cs]e")
# print(pattern.match(txt)==None) #starts finding match from the index 0. returns NonType if none is found
# print(pattern.search(txt)==None) #starts finding match irregardless of position/index
# print(pattern.search(txt))
# print(pattern.findall("hey licence license licence licence"))

# print(highlight_regex_matches(pattern, txt))
# CHARACTER SET RANGE: [a-z] [a-zA-Z0-9]/[0-9]
txt = """""
  The first season on Indian Premiere League (IPL) was played in 2008.
  The second season was played in 2009 in South Africa.
  Last season was played in 2018 and won by Chennai Super Kings (CSK).
  CSK won the title in 2010 and 2011 as well.
  Mumbai Indians (MI) has also won the title 3 times in 2013, 2015 and 2017.
"""

# find all the years in the above text
pattern = re.compile('[1-9][0-9][0-9][0-9]')#re.compile("[1-9\d\d\d]") #search pattern
# print(pattern.search(txt)) #searches anywhere in the text (can specify pos and endpos)
# print(pattern.findall(txt)) #returns a list of strings
# print(pattern.match(txt) == None) #tries to match characters from the beginning unless specified

# ^ used for negating ranges (it's called a caret) place after the opening square brackets metacharacter ([)
# find all the characters in the text except vowel
vowel_pattern = re.compile("[^AaEeIiOoUu]")
# print(vowel_pattern.findall(txt))
# print(" ".join(vowel_pattern.findall(txt)))

# PREDIFINED CHARACTER CLASSES
# (. >> matches any character except new line)
# (\d >> matches any decimal digit: equivalent to [0-9])
# (\D >> matches any  non-digit character: equivalent to [^0-9])
# (\s >> matches any whitespace character: equivalent to the class[\t\n\r\f\v])
# (\S >> matches any non-whitespace character: equivalent to the class[^\t\n\r\f\v])
# (\w >> matches any alphanumeric character: equivalent to the class[a-zA_Z0-9])
# (\W >> matches any non-alphanumeric character: equivalent to the class[^a-zA_Z0-9])

txt = """""
  The first season on Indian Premiere League (IPL) was played in 2008.
  The second season was played in 2009 in South Africa.
  Last season was played in 2018 and won by Chennai Super Kings (CSK).
  CSK won the title in 2010 and 2011 as well.
  Mumbai Indians (MI) has also won the title 3 times in 2013, 2015 and 2017.
"""
# find all non-alphanumeric and non-white space characters in my text
a_pattern = re.compile("[^a-zA-Z0-9\t\n\r\f\v]")
# b_pattern = re.compile("[\w\s]")
# print(a_pattern.findall(txt))
# print(b_pattern.findall(txt))


# CHARACTER CLASSES: used to match a single character but out of several possible characters
# ALTERATION: used to match a single regular expression out of several possible regular expressions. accomplished
# using the pipe symbol |
# consider a scenario where you want to find all occurences of and, or, the in a given text

txt = """"
the most common conjunctions are and, or and but
"""
# print(re.findall("and|or|the", txt))

# want to search the substrings (What is) (Who is)
txt = """"
What is your name?
Who is that guy?
"""

pattern = re.compile("What|Who|is")
patter_2 = re.compile("(What|Who) is")
# print(pattern.findall(txt))
# print(patter_2.findall(txt))

# QUANTIFIERS: mechanisms to define how a character, metacharacter, or character set can be repeated
# (? >> Optional(0 or 1 repetitions)), (* >> Zero or more times), (+ >> One or more times),
# ({n,m} >> between n and m times both inclusive) -> of preceding characters
# {n} > previous char is repeated exactly n times, {n,} > previous char repeated at least n times
#{,n} > previous char repeated at most n times

# Find all the matches for dog and dogs in the given text
txt = """"
I have 2 dogs. One dog is 1 year old and other one is 2 years old. Both dogs are very cute!
"""
# pattern = re.compile("dogs|dog")
pattern = re.compile("dogs?")
# print(pattern.findall(txt))

# Find all the filenames starting with file and ending with .txt in the given text.
txt = """"
file1.txt
file_one.txt
file.txt
file.txt
file.xml
"""
pattern = re.compile("file\w*\.txt")
# print(pattern.findall(txt))
# print(pattern.match(txt))
# print(pattern.search(txt))
# print(next(pattern.finditer(txt)))


# Find all filenames starting with file followed by 1 or more digits and ending with .txt in the given text
txt = """"
file1.txt
file_one.txt
file09.txt
file.txt
file23.xml
"""

pattern = re.compile("file\d+\.txt")
# print(pattern.findall(txt))


# 
txt = """""
  The first season on Indian Premiere League (IPL) was played in 2008.
  The second season was played in 2009 in South Africa.
  Last season was played in 2018 and won by Chennai Super Kings (CSK).
  CSK won the title in 2010 and 2011 as well.
  Mumbai Indians (MI) has also won the title 3 times in 2013, 2015 and 2017.
"""

pattern = re.compile("[0-9\d{3}]")

# In the given text, filter out all 4 or more digit numbers
num = """"
123143
432
5657
4435
54
65111
"""
pattern_less = re.compile("\d{4,}")
pattern_most = re.compile("\d{, 4}")
pattern_btn = re.compile("\d{1,4}")
# print(pattern_btn.findall(num))

# write a pattern to validate phone numbers:
# Can be in the form: 555-555-555,  555 555 555, 555555555
txt = """"
555-555-5555 
555 555 5555
5555555555
"""

pattern =  re.compile("\d{3}[\s-]?\d{3}[\s-]?\d{4}")
# print(pattern.findall(txt))

txt = """"
Lorem, ipsum dolor sit amet sand consectetur adipisicing elit. Officia eaque and quas ut, quae tenetur velit laborum possimus quidem impedit. 
Ducimus voluptatem repellat possimus laudantium atque and distinctio standard reprehenderit vel repellendus ut sapiente, hic mollitia doloremque
accusamus qui ea dolores quam odit maiores the more suscipit provident dolore fathere totam architecto. Sequi, quaerat harum!
"""
pattern = re.compile(r"\b(and|or|the)\b")

# print(pattern.findall(txt))


# BOUNDARY MATCHERS (\b) - word boundary metacharacter
# word boundary are those characters which constitute of a word boundary (space, tab, newline etc)
# print(r"\b(and|or|the)\b") #or \\b(and|or|the)\\b
# consider a scenario where you want to find all the occurences of and, or and the in the given text

# BOUNDARY MATCHERS AVAILABLE IN PYTHON: ((^ >> matches at the beginning of a line), ($ >> matches at the end of a line,
# (\b >> matches a word boundary, (\B >> matches the opposite of \b. Anything that is not a word boundary, 
# (\A >> matches the beginning of the input), (\Z >> matches the end of the input))))

# print(pattern.findall(txt))

# CONSIDER A SCENARIO WHERE WE WANT TO FIND ALL THE LINES IN THE GIVEN TEXT WHICH START WITH THE PATTERN Name:
# flag = re.M / re.MULTILINE is a flag which is used to make begin/end (^ $) consider each line
txt = """"
Name:
Age: 0
Roll No.: 15
Grade: S

Name: Ravi
Age: -1
Roll No.: 123 Name: ABC
Grade: K

Name: Ram
Age: N/A
Roll No.: 1
Grade: G
"""
pattern = re.compile(r"^Name:.*", flags=re.M) #match any character except newline(.) and any number of times(*)

# print(pattern.findall(txt))

# FIND ALL THE SENTENCES WHICH DO NOT END WITH A FULL STOP(.) IN THE GIVEN TEXT.

txt = """"
Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s!
It has survived not only five centuries, but also the leap into electronic typesettin, remark!
It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum.
More recently with desktop publishing software like Aldus PageMaker including versions of. 
"""

pattern = re.compile(r"^.*[^.]$", flags=re.M)
# print(pattern.findall(txt))

# SPLIT USING REGEX (split(string[, maxsplit]))
# split() method splits the input string at all positions where a match is found
# maxsplit is an optional argument (default value is 0) which specifies the max no. of splits that can take place.
# 0 means there is no on the no. of splits


# LET US TRY TO SPLIT A STRING TO GET INDIVIDUAL LINES IN IT
txt = """"
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
"""

pattern = re.compile("\n")
# print(pattern.split(txt))

# WHERE YOU WANT TO GET ALL THE WORDS IN THE GIVEN TEXT
pattern = re.compile(" ")
pattern_2 = re.compile(r"\W")
# print(pattern.split(txt))
# print(pattern_2.split(txt))


# SUBSTITUTION (sub(repl, string[, count=0]))
# repl is the replacement string which gets substituted in the place of match 
# string is the input text on which substistution takes place 
# count is an optional argument (default is 0) which specifies the max. number of substitutions that take place. 0 means no limit

# replace all the numbers with dash
txt = """"
100 cats, 23 dogs, 3 rabbits
"""

pattern = re.compile("\d+")

print(pattern.findall(txt))

print(pattern.sub("-", txt))