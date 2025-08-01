def contribution(salary):
    employee_contribution = salary *0.08
    employer_contribution = salary * 0.10

    employee_dict = {
        "employee_contribution": employee_contribution,
        "employer_contribution": employer_contribution,
        "total_contribution": employee_contribution + employer_contribution

    }

    return employee_dict


print(contribution(50000))