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

def get_key_by_val(target, dict):
    for key, val in dict.items():
        if target == val:
            return key
        
def available_row_by_key(key, dict): # Return the first row with available seat (using table label)
    col_index = dict[0].index(key)
    for row in dict:
        if row[col_index] == 'o': # row[col_index] reference the position of the table in that row
            return row[0] # Return the first column of the row (Row ID/ Label)

def all_available_row_by_key(key, dict): # Return all the rows with available seat (using table label)
    col_index = dict[0].index(key)
    breakpoint()
    available_rows = []
    for row in dict:
        if row[col_index] == 'o':
            available_rows.append(row[0])
    return available_rows

# -------------------------------------------------------------------------------------

# LEVEL 1
def print_tables(tables):
    print("\n=================================\n") # Divider
    for row in tables:
        for col in row:
            if row == restaurant_tables[0]: # Check if its the first row
                if col == row[0]: # Check if its the first column
                    print(col, end = "  ")
                else:
                    print(col, end = "  ")
            else: 
                print(col, end = "  ")
                if col != row[0]: # Check if its not the first column
                    print("  ", end = "  ")
        print() # Print a new line
    print("\no = open\nx = occupied") # Print a key

# LEVEL 2
def find_fit_table(table): # table = the restaurant table used (restaurant_table or restaurant_table2)
    print("\n=================================\n")
    party_size = int(input("Party size: "))
    capacity = table_capacity(table)
    for cap in capacity.values():
        if cap >= party_size:
            key = get_key_by_val(cap, capacity)
            return key + ' - ' + str(available_row_by_key(key, table))
        return "No available table" # Place holder for no available table

# LEVEL 3 ------ FIX THIS LATER
def find_all_fit_table(layout): # ALL available tables instead of just 1
    print("\n=================================\n")
    party_size = int(input("Party size: "))
    capacity = table_capacity(layout)
    available_tables = [] # List to store available tables
    for i, cap in enumerate(capacity.values()):
        if cap >= party_size:
            key = get_key_by_val(cap, capacity)
            available_tables.append(key + ' - ' + str(all_available_row_by_key(key, layout))[i])
    if available_tables:
        return available_tables
    return "No available table" # Place holder for no available table

# LEVEL 4
def find_fit_table_adjacent(table): # Check if adjacent tables are available
    print("\n=================================\n")
    party_size = int(input("Party size: "))
    capacity = table_capacity(table)
    pass

# FOR FUN
def print_available_tables(available_tables, layout): # ['T1(2) - 2', 'T2(4) - 1', 'T4(6) - 1']
    new_layout = layout.copy()
    for table in available_tables.copy():
        row = int(table.split()[-1])
        table_ID = table[:5] # Only take the ID e.g. T1(2) - 2 ---> T1(2)
        col = layout[0].index(table_ID)
        new_layout[row][col] = '*'
    print_tables(new_layout)
    print("* = your option") # Additional key for user
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

print_tables(restaurant_tables2)
available_tables = find_all_fit_table(restaurant_tables2)
print()
print("Available table: ")
for table in available_tables:
    if available_tables == "No available table":
        print(available_tables)
    else:
        print(" * " + table) # Print table with a space in front

print_available_tables(available_tables, restaurant_tables2)