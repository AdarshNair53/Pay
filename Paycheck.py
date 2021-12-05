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
    with open ('{}_{}_{}_cpayment.txt'.format(value[1],value[0],data[0]), 'w') as f:
        f.write("*****COMPUTE PAYMENT*****\n\n")
        f.write("ID: {}\n".format(data[1]))
        #value = emp_data_dict[data[1]]
        f.write("Name: {}\n".format(value[0]+value[1]))
        f.write("Date: {}\n\n\n".format(data[0]))
#####
        f.write("Regular Hours Worked:  {}\n".format(value[3]))       
        reg_hours = int(value[3]) if int(data[2])>int(value[3]) else int(data[2])
        reg_pay = reg_hours * int(value[4])
        f.write("Regular Pay:           {}\n".format(reg_pay))
        f.write("Regular Rate:          {}\n".format(value[4]))
        ovr_hours = int(data[2]) - reg_hours
        a = int(value[4])*float(value[5])
        f.write("Overtime Rate:         {}\n".format(a))
        f.write("Overtime Hours Worked: {}\n".format(ovr_hours))
        f.write("Overtime Pay:          {}\n".format(a*ovr_hours))
        g_pay = reg_pay + (a*ovr_hours)
        f.write("Gross Pay:             {}\n".format(g_pay))
        f.write("Standard Rate Pay:     {}\n".format(value[7]))
        h_pay = g_pay - int(value[7])
        f.write("Heigher Rate Pay:      {}\n".format(h_pay))
        s_tax = int(value[7])*0.2
        f.write("Standard Tax:          {}\n".format(s_tax))
        f.write("Heigher Tax:           {}\n".format(h_pay*0.4))
        t_tax = s_tax + h_pay*0.4
        f.write("Total Tax:             {}\n".format(t_tax))
        f.write("Tax Credit:            {}\n".format(value[6]))
        f.write("Net Deductions:        {}\n".format(t_tax - int(value[6])))
        f.write("Net Pay:               {}\n".format(int(value[7])-(t_tax - int(value[6]))))
