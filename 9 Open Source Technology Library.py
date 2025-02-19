# install : pip install library

# pandas for example
data=[
    ['s001','Tom',89],
    ['s002','Amy',70],
    ['s003','Alex',34]
]
import pandas as pd
df = pd.DataFrame(data,
                  columns=['student_number','name','grade'])
df.to_excel('grades.xlsx')

