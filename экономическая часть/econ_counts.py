from numpy import array
a = array([80, 200, 23, 120, 8, .5, 30, 25])
b = array([95, 230, 30, 160, 12, 2, 40, 50])
r = array([50, 80,  15, 200, 25, 35,30, 50])


s = (3*a + 2*b)/5.

print "Rounded times:"
print s
print "Summarized times:"
print sum(a), sum(b), sum(s)

print "People number:"
print r

s_chd = s * 0.12195 * 1000
print "Time in ChDs: %s" %str(s_chd)

s_wday = 1.*s_chd / r
print "Time in working days:"
print s_wday

s_calday = s_wday * 1.45
print "Time in calendar days:"
print s_calday

s_month = s_calday / 30.
print "Time in calendar month:"
print s_month

# lets count our money
# hour_money = 190.
hour_money = 210.
fot = sum(s) * 1000 * hour_money
print "Fot is : %s roubles" %round(fot)

bills = fot * .3
naklad = fot * 1.8

people_money = fot + bills + naklad
print "Non-production costs: %.3f mil. rub." %(people_money/10**6)

all_money = people_money / 0.4
material_money = all_money - people_money
print "Production costs: %.3f mil. rub." %(material_money/10**6)
print "Full cost: %.3f mil. rub." %(all_money/10**6)
