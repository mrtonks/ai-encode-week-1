from scripts import ChefGPT_2vJSPK

def display_instructions():
  print("Welcome to the Master ChefGP from Group 8.\n")
  print("Select the Chef you want to call:")
  print("1. 2vJSPK - Jesus Vera")
  print("\n")

def main():
  while True:
    display_instructions()
    user_input = input("Enter the number to run: ").strip()

    print("\n")

    if user_input == "1":
      ChefGPT_2vJSPK.run()
      break
    else:
      print("Invalid input. Please try again")

if __name__ == "__main__":
  main()