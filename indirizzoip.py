def is_valid_ipv4(address: str) -> bool:

    parts = address.split(".")

    if len(parts) != 4:
        return False
    
    for part in parts:
        if not part.isdigit():
            return False
        
        part = int(part)

        if part < 0 or part > 255:
            return False
        
    return True



print(is_valid_ipv4("192.168.0.1")) # True
print(is_valid_ipv4("255.255.255.255")) # True
print(is_valid_ipv4("256.100.10.1")) # False (256 è fuori range)
print(is_valid_ipv4("192.168.1")) # False (solo 3 parti)
print(is_valid_ipv4("192.168.1.a")) # False (parte non numerica)