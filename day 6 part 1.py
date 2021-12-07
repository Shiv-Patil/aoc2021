fish_list = [*map(int, input().split(','))]
fish_count = len(fish_list)


def get_fish(_fish, total_count, days):
    current_fish_count = max(0, (days+6-_fish) // 7)
    total_count += current_fish_count
    days -= _fish+1
    for new_fish in range(current_fish_count):
        total_count = get_fish(8, total_count, days)
        days -= 7
    return total_count


for fish in fish_list:
    fish_count += get_fish(fish, 0, 80)

print("***", fish_count, "***")
