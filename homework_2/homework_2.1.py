def bug_test(n: int) -> str:
    if n % 3 == 0 and n % 5 == 0:
        return "BugTest"
    elif n % 3 == 0:
        return "Bug"
    elif n % 5 == 0:
        return "Test"
    else:
        return str(n)

for number in range(1, 31):
    print(bug_test(number))