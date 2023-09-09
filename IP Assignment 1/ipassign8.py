pop = [50, 1450, 1400, 1700, 1500, 600, 1200]

def count_year(pop):
    years = 0
    dec = 0.025
    cnt = 0
    for i in pop:
        growth = 0
        for y in range(13):
            i += (growth + dec)*i
            years = y + 1
            growth -= 0.001
        cnt += i
        dec -= 0.004
    print(int(cnt*1000000))
    print(years)
count_year(pop)