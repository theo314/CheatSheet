
import pandas as pd
import os
from pyexcel_ods import get_data

# Load the ods data using pyexcel_ods
data = get_data('CheatSheet.ods')

# Convert the ods data to a pandas DataFrame
df = pd.DataFrame(data['Sheet1'][1:], columns=data['Sheet1'][0])

def execute_command(command_number):
	#Find the command in the dataframe
	command_row = df.loc[df['Command Number'] == command_number]

	if command_row.empty:
		print("No such command number.")
		return

	command = command_row['Command/Script'].values[0]


	# Execute the command
	os.system(command)

command_number = int(input("Enter the command number: "))
execute_command(command_number)
