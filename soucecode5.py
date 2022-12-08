#Print the songs for the user
user_id1 = u[5]
user_items1 = is_model.get_user_items(user_id1)
print("------------------------------------------------------------------------------------")
print("Songs played by first user %s:" % user_id1)
print("------------------------------------------------------------------------------------")
for user_item in user_items1:
    print(user_item)
print("----------------------------------------------------------------------")
print("Similar songs recommended for the first user:")
print("----------------------------------------------------------------------")
#Recommend songs for the user using personalized model
is_model.recommend(user_id1)