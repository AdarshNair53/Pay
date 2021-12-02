import csv

with open ('Employees.txt', 'r') as f:
    emp_data = [row for row in csv.reader(f,delimiter='\t')]
emp_data_dict = {}
for data in emp_data:
    emp_data_dict[data[0]] = data[1:]

with open ('hours.txt', 'r') as f:
    hour_data = [row for row in csv.reader(f,delimiter='\t')]

for data in hour_data:
    value = emp_data_dict[data[1]]
    with open ('{}_{}_computepayment.txt'.format(value[1],value[0]), 'w') as f:
        f.write("Compute Payment\n\n")
        f.write("ID: {}\n".format(data[1]))
        value = emp_data_dict[data[1]]
        f.write("Name: {}\n".format(value[1]+value[0]))
        f.write("Date: {}\n".format(data[0]))
        f.write("Regular Hours Worked: {}\n".format(value[3]))
        f.write("Overtime Hours Worked: {}\n".format(value[3]))
        f.write("Regular Rate: {}\n".format(value[3]))
        f.write("Overtime Rate: {}\n".format(value[3]))
        f.write("Regular Pay: {}\n".format(value[3]))
        f.write("            Hours     Rate      Total\n")
        reg_hours = int(value[3]) if int(data[2])>int(value[3]) else int(data[2])
        f.write("Regular     {}        {}        {}\n".format(reg_hours,int(value[4]),reg_hours*int(value[4])))
        ovr_hours = int(data[2]) - reg_hours
        f.write("Overtime     {}        {}        {}\n\n".format(ovr_hours,int(value[5]),ovr_hours*int(value[5])))
        f.write("Gross Pay     {}".format(reg_hours*int(value[4])+ovr_hours*int(value[5])))
