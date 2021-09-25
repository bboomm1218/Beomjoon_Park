def normalize_data(n_cases, n_people, scale):
    # TODO: Calculate the number of cases per its population
    norm_cases = []
    for idx, n in enumerate(n_cases):
        rate = scale * (n / n_people[idx])
        norm_cases.append(rate)
    return norm_cases

regions  = ['Seoul', 'Gyeongi', 'Busan', 'Gyeongnam', 'Incheon', 'Gyeongbuk', 'Daegu', 'Chungnam', 'Jeonnam',
            'Jeonbuk', 'Chungbuk', 'Gangwon', 'Daejeon', 'Gwangju', 'Ulsan', 'Jeju', 'Sejong']
n_people = [9550227, 13530519, 3359527, 3322373, 2938429, 2630254, 2393626, 2118183, 1838353,
            1792476, 1597179, 1536270, 1454679, 1441970, 1124459, 675883, 365309] # 2021-08
n_covid  = [644, 529, 38, 29, 148, 28, 41, 62, 23, 27, 27, 33, 16, 40, 0, 5, 4] # 2021-09-21

sum_people = sum(n_people)
sum_covid  = sum(n_covid)
norm_covid = normalize_data(n_covid, n_people, 1000000) # The new cases per 1 million people

# Print population by region
print('### Korean Population by Region')
print('* Total population:', sum_people)
print('|   Region   | Population | Ratio (%) |')
print('|   ------   | ---------- | --------- |')
for idx, pop in enumerate(n_people):
    ratio = (pop / sum_people) * 100 # TODO: The ratio of the number of people in the region to the total population
    print(f"|{regions[idx].center(12, ' ')}|{str(pop).center(12, ' ')}|{str(round(ratio, 2)).center(11, ' ')}|")
print('')

# TODO: Print COVID-19 new cases by region
print('### The Number of New Cases by Region')
print('* The Number of Total Cases: ', sum_covid)
print('|   Region   | Number of Cases | Ratio (%) | Cases per 1M |')
print('|   ------   | --------------- | -------- | ------------ |')
for idx, case in enumerate(n_covid):
    ratio = (case / sum_covid) * 100
    print(f"|{regions[idx].center(12, ' ')}|{str(case).center(17, ' ')}|{str(round(ratio, 2)).center(11, ' ')}|"
          f"{str(round(norm_covid[idx], 2)).center(14, ' ')}|")

print('')