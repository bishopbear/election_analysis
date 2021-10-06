# #How many votes did you get?
# my_votes = int(input("how man y votes did you get in the election? "))
# # Total votes in the election
# total_votes = int(input("What is the total votes in the election? "))
# # Calculate the percentage of votes you rceived
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of the total votes.")

counties = ["Arapahoe","Denver","Jefferson"]
# if counties[1] =='Denver':
#     print(counties[1])

# temperature = int(input("What is the temperature outside? "))

# if temperature > 80:
#     print("Turn on the AC. ")
# else:
#     print("Open the windows.")

# counties = ["Arapahoe","Denver","Jefferson"] 
# if "Arapahoe" in counties: 
#     print("True") 
# else: 
#     print("False")
# counties = ["Arapahoe","Denver","Jefferson"] 
# if "El Paso" not in counties: 
#     print("True") 
# else: 
#     print("False")

# if "Arapahoe" in counties and "El Paso" in counties:
#     print("Arapahoe and El Paso are in the list of counties.")
# else:
#     print("Arapahoe or El Paso is not in the list of counties.")

# if "Arapahoe" in counties or "El Paso" in counties:
#     print("Arapahoe or El Paso is in the list of counties.")
# else:
#     print("Arapahoe and El Paso are not in the list of counties.")

# for county in counties:
#     print(county)

# for i in range(len(counties)):
#     print(counties[i])

# counties_tuple = ("Arapahoe","Denver","Jefferson")

# for county in counties_tuple:

#       print(county)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county in counties_dict:
#     print(county)
# for county in counties_dict.keys():
#     print(county)
# for voters in counties_dict.values():
#     print(voters)
# for county in counties_dict:
#     print(counties_dict[county])
# for county in counties_dict:
#     print(counties_dict.get(county))
# for county in counties_dict:
#     print(counties_dict.get(county))
# for county, voters in counties_dict.items():
#     print(county, voters)
# for county, voters in counties_dict.items():
#     print(county, "county has", voters, "registered voters")


# for county, voters in counties_dict.items():
#     print(county + " county has " + str(voters) + " registered voters.")


# for county, voters in counties_dict.items():
#     print(f"{county} county has {voters} registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                 {"county":"Denver", "registered_voters": 463353},
                 {"county":"Jefferson", "registered_voters": 432438}]

# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of the total votes.")

# candidate_votes = int(input("How many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))
# message_to_candidate = (
#     f"You received {candidate_votes:,} number of votes. "
#     f"The total number of votes in the election was {total_votes:,}. "
#     f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

# print(message_to_candidate)

#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county, voters in counties_dict.items():
#     print(f"{county} county has {voters} registered voters.")

# Import the datetime class from the datetime module.
import datetime
# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the present time.
print("The time right now is ", now)

# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the present time.
print("The time right now is ", now)
