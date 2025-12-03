def cnt_move(prev_east,prev_north,east,north,east_cnt,north_cnt):
        for k in range(prev_north,north+1):
            if k in north_cnt:
                north_cnt[k] += 1
            else:
                north_cnt[k] = 1    