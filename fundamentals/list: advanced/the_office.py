# employee_happiness = map(int, input().split())
# factor = int(input())
# factored_happiness = []
# total_happiness = 0
# for curr_employee in employee_happiness:
#     factored_happiness.append(curr_employee * factor)
#
# for curr_employee in factored_happiness:
#     total_happiness += curr_employee
#
# average_happiness = total_happiness / len(factored_happiness)
#
# happy_employee_count = 0
#
# for i in factored_happiness:
#     if i >= average_happiness:
#         happy_employee_count += 1
#
# if happy_employee_count >= len(factored_happiness)/2:
#     print(f'Score: {happy_employee_count}/{len(factored_happiness)}. Employees are happy!')
# else:
#     print(f'Score: {happy_employee_count}/{len(factored_happiness)}. Employees are not happy!')

employees = input().split(" ")
factor = int(input())

employees = list(map(lambda x: int(x) * factor, employees))
filtered = list(filter(lambda x: x >= (sum(employees)/ len(employees)), employees))

if len(filtered) >= len(employees)/2:
    print(f'Score: {len(filtered)}/{len(employees)}. Employees are happy!')
else:
    print(f'Score: {len(filtered)}/{len(employees)}. Employees are not happy!')
