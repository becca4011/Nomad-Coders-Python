#list(mutable sequence - 값이 변할 수 있음)
days = ["Mon", "Tue", "Wed", "Thur", "Fri"];

print(type(days));
print("Mon" in days);
print(days[2]);
print(len(days));

print(days);
days.append("Sat"); #추가
days.reverse(); #역방향
print(days);