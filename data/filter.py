# Import pandas and requests libraries
import pandas as pd
import requests

# Read the csv file into a dataframe and specify the column names
df = pd.read_csv("tranco_VX8LN.csv", names=["rank", "domain"])


# Define a function to extract the top-level domain from a domain name
def get_tld(domain):
    # Split the domain name by dots
    parts = domain.split(".")
    # Return the last two parts joined by a dot
    return ".".join(parts[-2:])


# Apply the function to the domain column and create a new column for the top-level domain
df["tld"] = df["domain"].apply(lambda x: get_tld(x))

# Drop any duplicates in the top-level domain column and keep the first occurrence
df = df.drop_duplicates(subset="tld", keep="first")


# Define a function to ping a domain and return True if it responds, False otherwise
def ping_domain(domain):
    # Try to send a GET request to the domain with a timeout of 5 seconds
    try:
        response = requests.get("http://" + domain, timeout=5)
        # Return True if the status code is 200 (OK)
        return response.status_code == 200
    # Handle any exceptions (such as connection errors, timeouts, etc.)
    except:
        # Return False if there is an error
        return False


# Initialize an empty list to store the ping results
ping_results = []
ctr = 1

# Loop through the rows of the dataframe
for index, row in df.iterrows():
    # Get the rank and domain from the row
    rank = row["rank"]
    domain = row["domain"]
    # Ping the domain and get the status
    status = ping_domain(domain)
    # Append a tuple of rank, domain, and status to the ping results list
    if status:
        ping_results.append((ctr, domain))
        ctr += 1
        print(ping_results[-1])
    # Check if the ping results list has reached 50 items
    if len(ping_results) == 50:
        break

# Convert the ping results list into a new dataframe with columns rank, domain, and ping
df2 = pd.DataFrame(ping_results, columns=["rank", "domain"])

# Save the filtered dataframe to a new csv file
df2.to_csv("filtered_rank_domain.csv", index=False)