mzs=[1499.33, 1522.8131810038001, 1537.1035546140799, 2678.32, 2790.1282213525478, 2818.8131810038039]
normal_mzs=[1526, 1536, 2791, 2819]

mzs_adjacents=[]    

for normal_mz in normal_mzs:
    d=10
    m=0
    print(normal_mz)
    print(d)
    for mz in mzs:
        if abs(normal_mz-mz)<d:
            d=abs(normal_mz-mz)
            m=mz
            print('    -', abs(normal_mz-mz))
            print('    m', m)
            print('    d', d)
    mzs_adjacents.append(m)
print(mzs_adjacents)
