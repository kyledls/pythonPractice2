enemies = 1

def increase_enemies():
    enemies = 0
    enemies += 1
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies inside function: {enemies}")
