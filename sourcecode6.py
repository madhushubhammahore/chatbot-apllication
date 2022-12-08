user_id2 = u[7]
#Fill in the code here
user_items2 = is_model.get_user_items(user_id2)
print("------------------------------------------------------------------------------------")
print("Songs played by second user %s:" % user_id2)
print("------------------------------------------------------------------------------------")
for user_item in user_items2:
    print(user_item)
print("----------------------------------------------------------------------")
print("Similar songs recommended for the second user:")
print("----------------------------------------------------------------------")
#Recommend songs for the user using personalized model
is_model.recommend(user_id2)