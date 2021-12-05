#### Paycheck

Create and test a function to compute net pay from
payment, work and tax credit information.

we read in a file (here named Employees.txt), which
contains the following information: (space separated)
<StaffID> <LastName> <FirstName> <RegHours>
<HourlyRate> <OTMultiple> <TaxCredit>
<StandardBand>

Read in a file (here named Hours.txt) which contains the
following information:
<StaffID> <Date> <HoursWorked>

We will assume a standard rate of 20% and a higher
rate of 40% (we will ignore PRSI, USC etc.)

***Conditions
-Netpay cannot exceed gross pay.
-Overtime pay or overtime hours cannot be negative .
-Regular hours cannot exceed hours worked.
-Hire tax cannot be negative .
-Net pay cannot be negative.

## Usage
Paycheck.py

##Output
  {First_Name}_{Last_Name}_{Date}_cpayment.txt

