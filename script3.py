
try:
    numero_acl = int(input("Ingrese el número de ACL IPv4: "))

    if 1 <= numero_acl <= 99:
        print("El número de ACL", numero_acl, "corresponde a una ACL Estándar.")
    elif 100 <= numero_acl <= 199:
        print("El número de ACL", numero_acl, "corresponde a una ACL Extendida.")
    else:
        print("El número de ACL", numero_acl, "no corresponde a una lista de acceso.")
except ValueError:
    print("Error: Por favor, ingrese un número válido.")

    