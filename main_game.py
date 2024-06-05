def lobby(x, y, world_map, account):
    if world_map[y][x] == '':
        world_map[y][x] = 'H'
    elif world_map[y][x] == 'T':
        world_map[y][x] = 'H/T'
    elif world_map[y][x] == 'K':
        world_map[y][x] = 'H/K'
    for i in world_map:
        print('\n' + '+---' * 8 + '+')
        for j in i:
            print('|{:^3}'.format(j), end='')
        print('|', end='')
    print('\n' + '+---' * 8 + '+')