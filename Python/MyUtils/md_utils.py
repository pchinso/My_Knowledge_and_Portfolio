from datetime import datetime, timedelta


def generate_month_days_string_list(start_date, end_date):
  '''
  # Example usage:

  For a month calendar 
  start_date = '2024-01-01'
  end_date = '2024-01-30'

  result = generate_month_days_string_list(start_date, end_date)
  print(result) -> ['[[2024-02-01 Monday]]', '[[2024-02-02 Tuesday]]'... ]
  '''

  # Convert start and end dates_md to datetime objects
  start = datetime.strptime(start_date, '%Y-%m-%d')
  end = datetime.strptime(end_date, '%Y-%m-%d')
  
  # Initialize the result list
  month_days = []
  
  # Iterate through each day between start and end dates_md
  current = start
  while current <= end:
    # Format the date as desired "[[YYYY-MM-DD DayOfWeek]]"
    formatted_date = current.strftime('[[%Y-%m-%d %A]]')
    # Append the formatted date to the result list
    month_days.append(formatted_date)
    # Move to the next day
    current += timedelta(days=1)
  return month_days

def extract_weekday(date_str):
  '''
  # Example usage:

  # For
  date_str =  '[[2024-02-01 Thursday]]'

  weekday = extract_weekday(date_str)
  print(weekday) # -> 'Thursday'
  '''

  # Extract the date part from the string
  date_str = date_str.split()[0].strip('[')

  # Convert the date string to a datetime object
  date = datetime.strptime(date_str, "%Y-%m-%d")

  # Get the weekday name from the datetime object
  weekday = date.strftime("%A")

  return weekday

def extract_day(date_str):
  '''
  # Example usage:

  # For
  date_str =  '[[2024-02-01 Thursday]]'

  day = extract_weekday(date_str)
  print(day) # -> '01'
  '''  

  # Extract the date part from the string
  date_str = date_str.split()[0].strip('[')

  # Convert the date string to a datetime object
  date = datetime.strptime(date_str, "%Y-%m-%d")

  # Get the day name from the datetime object
  day = date.strftime("%d")

  return day

def generate_markdown_calendar(start_date = '2024-01-01',
                               end_date = '2024-12-31'):
  '''
  # Example usage:
  generate_markdown_calendar()

  # Create 2024 year calendar with my obsidian daily notes format 
  # date_str =  '[[2024-01-01 Monday]]'
  '''

  days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

  dates_md = generate_month_days_string_list(start_date, end_date)

  table_header = f'|          {days_of_week[0]}          |          {days_of_week[1]}          |           {days_of_week[2]}            |          {days_of_week[3]}          |          {days_of_week[4]}          |           {days_of_week[5]}           |          {days_of_week[6]}          |\n'
  table_divider = '|:---------------------:|:----------------------:|:------------------------:|:-----------------------:|:---------------------:|:-----------------------:|:---------------------|\n'
  
  markdown_table = table_header + table_divider

  # Locate the first cell of calendar star with preceding blank cells 
  first_week = 1
  
  for date_md in dates_md:

    weekday = extract_weekday(date_md)
    day = extract_day(date_md)

    # Preceding blank cells
    if day == '01'and first_week == 1:
      blank_spaces = days_of_week.index(weekday)
      first_week -= 1

      for i in range(0,blank_spaces):
        markdown_table += f'|       '
    
    # Fill Monday to Saturday 
    if weekday in  days_of_week[0:-1] :
      markdown_table += f'|   {date_md}   '
    
    elif weekday == 'Sunday':
      markdown_table += f'|   {date_md}   |'
      markdown_table += '\n'

  # Saves the calendar as Markdown 
  with open('output.md', 'w') as file:
    file.write(markdown_table)



