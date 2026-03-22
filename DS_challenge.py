# CODE STARTS HERE
import json
import pandas as pd

with open('DS_challenge_dataset.json', 'r') as file:
    data = json.load(file)

df = pd.json_normalize(data['records'])

print(df)

df = df.drop_duplicates()

# Convert types if necessary
df['attendance'] = pd.to_numeric(df['attendance'], errors='coerce')
df['new_attendees'] = pd.to_numeric(df['new_attendees'], errors='coerce')
df['repeat_attendees'] = pd.to_numeric(df['repeat_attendees'], errors='coerce')
df['no_show_count'] = pd.to_numeric(df['no_show_count'], errors='coerce')

# For the attendance, new_attendees, repeat_attendees, no_show_count, fill missing or null values with 0
df = df.fillna({
    'attendance': 0,
    'new_attendees': 0,
    'repeat_attendees': 0,
    'no_show_count': 0,
})

# Cast to int after filling missing values
df = df.astype({
    'attendance': 'int',
    'new_attendees': 'int',
    'repeat_attendees': 'int',
    'no_show_count': 'int'
})

# Noramlize event_type names
df['event_type'] = (
    df['event_type']
    .str.strip()
    .str.lower()
    .replace({
        'work shop': 'workshop',
    })
    .str.title()
)

top_5 = df.sort_values(by='attendance', ascending=False).head(5)
print(top_5[['event_name', 'attendance']])

new_attendees_by_type = df.groupby('event_type')['new_attendees'].sum()
print(new_attendees_by_type)

# CODE ENDS HERE
    
# REPORT YOUR VALUES IN THE DOCSTRING BELOW

"""
Which 5 events had the highest attendance?
Answer: Holiday Social, Design Thinking Lab, Women in Leadership Panel, Community Picnic, Volunteer Day



How many new attendees were there by event type?
Answer: 

Forum         709
Networking    759
Panel         821
Roundtable    768
Social        536
Talk          538
Workshop      944


What data quality issues exist in the dataset, and how would you handle them before analyzing attendance?
Answer: Some attendance values were missing or null or as a string. To handle this I would fill missing or null values with 0 and convert the attendance column to numeric type to ensure all values are numeric.
For event_type, there were inconsistencies in naming (e.g., "work shop" vs "workshop") and some differences in capitalization. To handle this I would normalize it by stripping whitespace, converting to lowercase, replacing variations, and then capitalizing.


"""