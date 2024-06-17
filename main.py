from scripts import ChefGPT_2vJSPK
from scripts import ChefGTP_tJ5Mon
from scripts import ChefGPT_4bwGEs

def display_instructions():
  print("Welcome to the Master ChefGP from Group 8.\n")
  print("Select the Chef you want to call:")
  print("1. 2vJSPK - Jesus Vera")
  print("2. tJ5Mon - Sofia Orellano")
  print("3. 4bwGEs - Aleksandar Brayanov")
  print("\n")

def main():
  while True:
    display_instructions()
    user_input = input("Enter the number to run: ").strip()

    print("\n")

    if user_input == "1":
      ChefGPT_2vJSPK.run()
      break
    elif user_input == "2":
      ChefGTP_tJ5Mon.run()
      break
    elif user_input == "3":
      ChefGPT_4bwGEs.run()
      break
    else:
      print("Invalid input. Please try again")

if __name__ == "__main__":
  main()
