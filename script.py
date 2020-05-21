import codecademylib3_seaborn
import pandas as pd
from students import students

print(students)

# 1.Print out the columns of the students DataFrame.
print(students.columns)

# 2.The column gender_age sounds like it contains both gender and age!

#Print out the .head() of the column to see what kind of data it contains.
print(students.head())


# 3.It looks like the first character of the values in gender_age contains the gender, while the rest of the string contains the age. Let’s separate out the gender data into a new column called gender.
students['gender'] = students.gender_age.str[0]


# 4.Now, separate out the age data into a new column called age.
students['age'] = students.gender_age.str[-2:]


# 5.Good job! Let’s print the .head() of students to see how the DataFrame looks after our creation of new columns.
print(students.head())


# 6.Now, we don’t need that gender_age column anymore.

#Let’s set the students DataFrame to be the students DataFrame with all columns except gender_age.
students = students[['full_name','gender','age','grade','exam','score']]

print(students.head())
