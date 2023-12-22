import requests

# Hacer la solicitud a la API
url = "https://dummy.restapiexample.com/api/v1/employees"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    # Obtener la lista de empleados
    employees = data["data"]

    # Número de empleados
    num_employees = len(employees)

    # Calcular el promedio de salario
    average_salary = round(sum([employee["employee_salary"] for employee in employees]) / num_employees, 2)


    # Calcular el promedio de edad
    average_age = round(sum([employee["employee_age"] for employee in employees]) / num_employees)

    # Encontrar salario mínimo y máximo
    min_salary = min([employee["employee_salary"] for employee in employees])
    max_salary = max([employee["employee_salary"] for employee in employees])

    # Encontrar edad mínima y máxima
    min_age = min([employee["employee_age"] for employee in employees])
    max_age = max([employee["employee_age"] for employee in employees])

    print(f"------------------------------")
    print(f"Datos:")
    print(f"------------------------------")
    print(f"Número de empleados: {num_employees}")
    print(f"Promedio de salario: {average_salary}")
    print(f"Promedio de edad: {average_age}")
    print(f"Salario mínimo: {min_salary}")
    print(f"Salario máximo: {max_salary}")
    print(f"Edad mínima: {min_age}")
    print(f"Edad máxima: {max_age}")
    print(f"------------------------------")

