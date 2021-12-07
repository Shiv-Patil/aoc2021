fish_list = [*map(int, input().split(','))]
fish_dict = {}

for fish in fish_list:
    fish_dict[fish] = fish_dict.get(fish, 0) + 1

for day in range(256):
    new_fish_dict = {}
    for timer, count in fish_dict.items():
        if timer == 0:
            new_fish_dict[8] = new_fish_dict.get(8, 0) + count
            timer = 7
        timer -= 1
        count = new_fish_dict.get(timer, 0) + count
        new_fish_dict[timer] = count
    fish_dict = new_fish_dict

print("***", sum(fish_dict.values()), "***")
