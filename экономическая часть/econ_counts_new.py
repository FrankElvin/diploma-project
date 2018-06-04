from numpy import array
a = array([40, 350, 250, 130, 45])
b = array([55, 380, 350, 160, 70])
r = array([1,  2,   2,   2,   1 ])


s = (3*a + 2*b)/5.

print "Rounded times:"
print s
print "Summarized times:"
print sum(a), sum(b), sum(s)

print "People number:"
print r

s_chd = s
print "Time in ChDs: %s" %str(s_chd)

s_wday = 1.*s_chd / r
print "Time in working days (Trab):"
print s_wday

s_calday = s_wday * 1.45
print "Time in calendar days (Tk):"
print s_calday

s_month = s_calday / 30.
print "Time in calendar month:"
print s_month

# lets count our money
# hour_money = 190.
hour_money = 210.
fot = sum(s) * hour_money
print "Fot is : %s roubles" %round(fot)

bills = fot * .3
naklad = fot * 1.8

people_money = fot + bills + naklad
print "Non-production costs: %.3f mil. rub." %(people_money/10**6)

all_money = people_money / 0.4
material_money = all_money - people_money
print "Production costs: %.3f mil. rub." %(material_money/10**6)
print "Full cost: %.3f mil. rub." %(all_money/10**6)
