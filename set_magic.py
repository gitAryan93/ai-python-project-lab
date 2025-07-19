user_a = input("Enter favorite movies of User A (comma-separated): ")
user_b = input("Enter favorite movies of User B (comma-separated): ")

set_a = set(movie.strip().title() for movie in user_a.split(","))
set_b = set(movie.strip().title() for movie in user_b.split(","))

print("\n🎬 Common Favorites:", set_a & set_b)
print("🍿 Unique to Each User:", set_b ^ set_b)
print("📚 Total Unique Movies:", set_a | set_b)
