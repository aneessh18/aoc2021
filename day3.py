import sys

def compute_power_consumption(report):
    rows = len(report)
    columns = len(report[0])
    
    gamma_rate = ""
    epsilon_rate = ""
    for j in range(columns):
        s = 0
        for i in range(rows):
            s += int(report[i][j])
        
        gamma_rate += '1' if s>rows-s else '0'
        epsilon_rate += '0' if s>rows-s else '1'
    return int(gamma_rate,2)*int(epsilon_rate,2)

def get_common_bit(reports, column, common_type):
    rows = len(reports)
    s = 0
    for i in range(rows):
        s += int(reports[i][column])
    
    if common_type == "most":
        return "1" if s>=rows-s else "0"
    else:
        return "0" if s>=rows-s else "1"

def compute_life_support_rating(reports):

    columns = len(reports[0])
    oxygen_generator_rating = ""
    co2_scrubber_rating = ""
    reports1 = reports.copy()
    reports2 = reports.copy()
    column = 0
    while len(reports1) != 1:
        # print(reports1)
        most_common_bit = get_common_bit(reports1, column, "most")
        reports1 = list(filter(lambda report1:report1[column] == most_common_bit, reports1))
        column = (column+1)%columns

    oxygen_generator_rating = reports1.pop()

    column = 0
    while len(reports2) != 1:
        least_common_bit = get_common_bit(reports2, column, "least")
        reports2 = list(filter(lambda report2:report2[column] == least_common_bit, reports2))
        column = (column+1)%columns
    co2_scrubber_rating = reports2.pop()

    return int(oxygen_generator_rating, 2)*int(co2_scrubber_rating, 2)
report =[]
filename = sys.argv[1]
with open(filename) as file:
    report= file.readlines()
    report = [report.rstrip() for report in report]
    
print(compute_power_consumption(report))
print(compute_life_support_rating(report))