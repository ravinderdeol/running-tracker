best_distance = int(input("What's Your Best Distance? "))
best_pace = int(input("What's Your Best Pace? "))

current_distance = int(input("What's Your Current Distance? "))
current_pace = int(input("What's Your Current Pace? "))

if current_distance > best_distance:
    best_distance = current_distance
    print(f"New Distance Record: {best_distance} KM")

if current_pace > best_pace:
    best_pace = current_pace
    print(f"New Best Pace: {best_pace} Min/KM")
