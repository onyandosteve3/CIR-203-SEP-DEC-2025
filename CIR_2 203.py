# Question 2: LIST OF 10 DELIVERY ROUTES
routes = [
    "North Ridge Express",
    "South Valley Line",
    "East Point Courier",
    "West Bay Haul",
    "Central Loop",
    "Northern Trail",
    "Southern Cross",
    "Eastern Horizon",
    "Western Pathway",
    "Midtown Shuttle"
]

# Append a new route
routes.append("Lakeside Drive")

# Remove a discontinued route
routes.remove("Central Loop")#assuming this route is discontinued

# Sorting the list alphabetically and reversing it
routes.sort()      # Sort alphabetically
routes.reverse()   # Reverse the sorted list

# Routes starting with latter 'N'
count_N = sum(route.startswith("N") for route in routes)

# Routes longer than 10 characters
long_routes = [route for route in routes if len(route) > 10]

# Output results
print("Updated Routes List:",routes)
print("Number of Routes Starting with 'N':",count_N)
print("Long Routes List:",long_routes)