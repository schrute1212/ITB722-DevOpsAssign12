
# Read the HTML files
with open('home.html', 'r', encoding='utf-8') as f:
    home_content = f.read()

with open('login.html', 'r', encoding='utf-8') as f:
    login_content = f.read()

with open('register.html', 'r', encoding='utf-8') as f:
    register_content = f.read()

print("=== HOME.HTML ===")
print(home_content)
print("\n\n=== LOGIN.HTML ===")
print(login_content)
print("\n\n=== REGISTER.HTML ===")
print(register_content)
