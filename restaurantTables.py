# ------------------------------------------------------------------------------------
# The following 2D lists mimic a restaurant seating layout, similar to a grid.
# 
# - Row 0 is a "header row":
#     - The first cell (index 0) is just a row label (0).
#     - The remaining cells are table labels with capacities in parentheses,
#       e.g., 'T1(2)' means "Table 1" has capacity 2.
#
# - Rows 1 through 6 each represent a distinct "timeslot" or "seating period":
#     - The first cell in each row (e.g., [1], [2], etc.) is that row's label (the timeslot number).
#     - Each subsequent cell shows whether the table (from the header row) is
#       free ('o') or occupied ('x') during that timeslot.
#
# In other words, restaurant_tables[row][column] tells you the status of a
# particular table (column) at a particular timeslot (row).
# ------------------------------------------------------------------------------------

# Shows the structure of the restaurant layout with all tables free ("o" = open).
restaurant_tables = [
    [0,        'T1(2)',  'T2(4)',  'T3(2)',  'T4(6)',  'T5(4)',  'T6(2)'],
    [1,        'o',      'o',      'o',      'o',      'o',      'o'],
    [2,        'o',      'o',      'o',      'o',      'o',      'o'],
    [3,        'o',      'o',      'o',      'o',      'o',      'o'],
    [4,        'o',      'o',      'o',      'o',      'o',      'o'],
    [5,        'o',      'o',      'o',      'o',      'o',      'o'],
    [6,        'o',      'o',      'o',      'o',      'o',      'o']
]

# -------------------------------------------------------------------------------------
def table_capacity(tables):
    row = tables[0].copy() # A copy of the first row
    row.pop(0) # Remove the first column
    table_capacity = {}
    for i, col in enumerate(row):
        table_capacity[col] = int(col[3])
    return table_capacity

        
def available_row_by_key(key, dict): # Return the first row with available seat (using table label)
    col_index = dict[0].index(key)
    for row in dict:
        if row[col_index] == 'o': # row[col_index] reference the position of the table in that row
            return row[0] # Return the first column of the row (Row ID/ Label)

def all_available_row_by_key(key, dict): # Return all the rows with available seat (using table label)
    col_index = dict[0].index(key)
    available_rows = []
    for row in dict:
        if row[col_index] == 'o':
            available_rows.append(row[0])
    return available_rows

# -------------------------------------------------------------------------------------

# LEVEL 4
# Note: Adjacent table are only the tables in the same row
def find_fit_table_adjacent(layout, party_size, available_tables = None): # Check if adjacent tables are available (ONLY use when normal tables cant fit)
    capacity = table_capacity(layout)
    combined_tables = []
    keys = list(capacity.keys())
    caps = list(capacity.values())
    breakpoint()
    for i in range(len(caps) - 1):
        available_rows = all_available_row_by_key(keys[i], layout)
        if available_tables != None:
            for table in available_tables:
                if keys[i] == table[:5]: # if its already available as a individual table
                    keys.pop(i) # Remove that key 
        for row in available_rows:
            col = layout[0].index(keys[i])
            if caps[i] + caps[i+1] >= party_size and layout[row][col] == 'o' and layout[row][col + 1] == 'o':
                combined_tables.append(f"{keys[i]} - {row} and {keys[i+1]} - {row} could seat {caps[i] + caps[i+1]} peoples")
    print(f"Combined_tables: {combined_tables}")
    return combined_tables

# LEVEL 1
def print_layout(layout):
    print("\n=================================\n") # Divider
    for row in layout:
        for col in row:
            if row == restaurant_tables[0]: # Check if its the first row
                print(col, end = "  ") # end = "  " means add 2 space after the varible instead of make a newline
            else: 
                print(col, end = "  ")
                if col != row[0]: # Check if its not the first column
                    print("  ", end = "  ")
        print() # Print a new line
    print("\no = open\nx = occupied") # Print a key

# LEVEL 2
def find_fit_table(layout): # layout = the restaurant layout used (restaurant_table or restaurant_table2)
    print("\n=================================\n")
    party_size = int(input("Party size: ")) # Ask user for the party size
    capacity = table_capacity(layout)
    for key, cap in capacity:
        if cap >= party_size:
            return key + ' - ' + str(available_row_by_key(key, layout))
        return find_fit_table_adjacent(layout, party_size) # Place holder for no available table

# LEVEL 3
def find_all_fit_table(layout): # ALL available tables instead of just 1
    print("\n=================================\n")
    party_size = int(input("Party size: "))
    capacity = table_capacity(layout) # {'T1(2)': 2, 'T2(4)': 4, 'T3(2)': 2, 'T4(6)': 6, 'T5(4)': 4, 'T6(2)': 2}
    available_tables = []  # List to store available tables
    for key, cap in capacity.items():  # Iterate over key-value pairs, key - capacity.key(), cap - capacity.values()
        if cap >= party_size:
            available_rows = all_available_row_by_key(key, layout)
            for row in available_rows:
                available_tables.append(f'{key} - {row}') 
    if available_tables == []: # If there's no available tables yet
        adjacent_tables = find_fit_table_adjacent(layout, party_size)
    else: # if there's already available tables
        adjacent_tables = find_fit_table_adjacent(layout, party_size, available_tables)
    if available_tables:
        available_tables.extend(adjacent_tables) # Add a list of adjacent tables to the end available table lists 
        return available_tables  # Return a list of available tables
    else:
        return adjacent_tables  # Placeholder for no available table

# FOR FUN
def print_available_tables(available_tables, layout): # ['T1(2) - 2', 'T2(4) - 1', 'T4(6) - 1']
    new_layout = layout.copy()
    for table in available_tables.copy():
        try: 
            row = int(table.split()[-1])
            table_ID = table[:5] # Only take the ID e.g. T1(2) - 2 ---> T1(2)
            col = layout[0].index(table_ID)
            new_layout[row][col] = '*'
        except ValueError:
            print(table)
            new_tables = table.split(' ')[:7] # Split the table and only take the first 7 parts of the splitted list 
            '''
            example: 
                table = 'T4(6) - 6 and T5(4) - 6 could seat 10 peoples'
                splitted_table = ['T4(6)', '-', '6', 'and', 'T5(4)', '-', '6', 'could', 'seat', '10', 'peoples']
                new_tables = ['T4(6)', '-', '6', 'and', 'T5(4)', '-', '6'] --> only show the [:7] part        
            '''
            new_tables = (" ").join(new_tables)
            new_tables = new_tables.split(' and ')
            for table2 in new_tables:
                row = int(table2.split()[-1])
                table_ID = table[:5]
                col = layout[0].index(table_ID)
                new_layout[row][col] = '-'
                new_layout[row][col+1] = '-'
            print(new_tables)
    print_layout(new_layout)
    print("* = your option\n- = joined tables") # Additional key for user
    print("\n=================================\n")
    
# ------------------------------------------------------------------------------------
# This second layout serves as a test case where some tables ('x') are already occupied.
# Use this for testing your logic to:
#   - Find free tables (marked 'o')
#   - Check if those tables meet a certain capacity (from the header row, e.g. 'T1(2)')
#   - Potentially combine adjacent tables if one alone isn't enough for a larger party.
# ------------------------------------------------------------------------------------

restaurant_tables2 = [
    [0,        'T1(2)',  'T2(4)',  'T3(2)',  'T4(6)',  'T5(4)',  'T6(2)'],
    [1,        'x',      'o',      'o',      'o',      'o',      'x'],
    [2,        'o',      'x',      'o',      'o',      'x',      'o'],
    [3,        'x',      'x',      'o',      'x',      'o',      'o'],
    [4,        'o',      'o',      'o',      'x',      'o',      'x'],
    [5,        'o',      'x',      'o',      'x',      'o',      'o'],
    [6,        'o',      'o',      'o',      'o',      'x',      'o']
]

print_layout(restaurant_tables2)
available_tables = find_all_fit_table(restaurant_tables2)
print()
print("Available table: ")
try: 
    for table in available_tables:
        print(" * " + table) # Print table with a space in front
    print_available_tables(available_tables, restaurant_tables2) # Only print out the chart if there's a seat for the customer
except ValueError:
    print("\n=================================\n")