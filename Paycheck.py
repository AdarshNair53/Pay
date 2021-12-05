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
        f.write("Name: {}\n".format(value[0]+value[1]))
        f.write("Date: {}\n\n\n".format(data[0]))
        f.write("Regular Hours Worked:  {}\n".format(value[3]))
        def pay_print():
            reg_hours = int(value[3]) if int(data[2])>int(value[3]) else int(data[2])
            reg_pay = reg_hours * int(value[4])
            return reg_pay,reg_hours
        x,y = pay_print()
#####          
        f.write("Regular Pay:           {}\n".format(x))
        f.write("Regular Rate:          {}\n".format(value[4]))
        def hour_print():
            ovr_hours = int(data[2]) - y
            if ovr_hours < 0:
                ovr_hours = 0
            ovr_time = int(value[4])*float(value[5])
            return ovr_hours,ovr_time
        oh,ot = hour_print()
        ovr_hours = int(data[2]) - y
        a = int(value[4])*float(value[5])
        f.write("Overtime Rate:         {}\n".format(ot))
        f.write("Overtime Hours Worked: {}\n\n".format(oh))
        f.write("***************************\n")
        f.write("Overtime Pay:          {}\n".format(ot*oh))
        g_pay = x + (ot*oh)
        f.write("Gross Pay:             {}\n".format(g_pay))
        f.write("Standard Rate Pay:     {}\n".format(value[7]))
        def tax_print():
            h_pay = g_pay - int(value[7])
            if h_pay < 0:
                h_pay = 0
            s_tax = int(value[7])*0.2
            t_tax = s_tax + h_pay*0.4
            return h_pay, s_tax, t_tax
        hp,st,tt = tax_print()
        f.write("Heigher Rate Pay:      {}\n".format(hp))
        f.write("***************************\n")
        f.write("Standard Tax:          {}\n".format(st))
        f.write("Heigher Tax:           {}\n".format(hp*0.4))
        f.write("Total Tax:             {}\n".format(tt))
        f.write("Tax Credit:            {}\n\n".format(value[6]))
        f.write("***************************\n")
        f.write("Net Deductions:        {}\n".format(tt - int(value[6])))
        f.write("Net Pay:               {}\n".format(int(value[7])-(tt - int(value[6]))))
        f.write("***************************\n")
#####


