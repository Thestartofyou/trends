import csv

# Define the CSV file paths
input_csv_file = 'llc_purchases.csv'
output_csv_file = 'llc_summary.csv'

# Create a dictionary to store LLC purchase data
llc_purchases = {}

# Read data from the input CSV file and populate the llc_purchases dictionary
with open(input_csv_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip the header row
    for row in csvreader:
        llc_name, item, location, price = row
        price = float(price)  # Convert price to a float
        if llc_name not in llc_purchases:
            llc_purchases[llc_name] = []
        llc_purchases[llc_name].append((item, location, price))

# Create a new CSV file to store the summary
with open(output_csv_file, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)

    # Write the header row
    csvwriter.writerow(['LLC Name', 'Total Purchases', 'Average Price'])

    # Calculate and write the summary for each LLC
    for llc_name, purchases in llc_purchases.items():
        total_purchases = len(purchases)
        total_price = sum(price for _, _, price in purchases)
        average_price = total_price / total_purchases if total_purchases > 0 else 0
        csvwriter.writerow([llc_name, total_purchases, average_price])

print("LLC purchase summary has been written to", output_csv_file)
