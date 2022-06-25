import random
import string
import webbrowser

# Generate a random string of letters and digits between 4 and 20 characters
def random_string(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

# Use the random string to generate a unique name for an email address from gmail
def generate_email_address():
    return f"{random_string(9)}@gmail.com"

# associate a random email address with a random password
def generate_credentials():
    return (generate_email_address(), random_string(10))

print(generate_credentials())

# navigate to gmail.com
def navigate_to_gmail():
    webbrowser.open("https://gmail.com")
    # click on the "create account" button
    xpath = //*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div/button/span
    
