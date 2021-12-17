target_y = abs(min(map(int, input()[15:].split(", ")[1][2:].split(".."))))
print("***", (target_y - 1) * target_y // 2, "***")
