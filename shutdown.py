def shutdown(answer):
    answer = answer.lower()
    if answer == "yes":
        print("Shutting down.")
    elif answer == "no":
        print("Shutdown Cancled.")
    else:
        print("Invalid answer/ sorry.")
user_answer = input("Do you want to shut down? Yes or no: ")
shutdown(user_answer)
