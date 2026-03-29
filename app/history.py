def history(user_history):
    for index, command in enumerate(user_history, start=1):
        print(f"{index} {command}")