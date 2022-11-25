from modules_and_classes import User
from post import Post
from modules_and_classes import Restaurant
from modules_and_classes import L2_untrusted

app_user_1 = User("si@gmail.com", "Si", "password", "Dog", 5)
app_user_1.get_user_info()

app_user_1.change_job_title("Cat")
app_user_1.get_user_info()
app_user_1.greet_user()
app_user_1.increment_login_attempts(10)

app_user_1.reset_login_attempts(0)


app_user_2 = User("si@gmail.com", "Di", "password", "Mouse", 0)
app_user_2.get_user_info()






#!!this work  - just blocked for brevity of other stuff
dave = L2_untrusted()
dave.display_details()
print (dave.vlan)
print (dave.vni)

new_post = Post("secret", "simon")

new_post.get_post_info()

site1 = Restaurant("Murphys", "Stew")
site1.describe_restaurant()
print (site1)

site1.set_number_served(1000)

site1.increment_number_served(1200)
site1.is_open()
site1.customers_served()


