import string
import secrets  

def generar_contraseña(longitud: int) -> str:
    """
    Generar una contraseña segura de la longitud especificada.
    
    Args:
        longitud: Número de caracteres que tendrá la contraseña.
        
    Returns:
        Una cadena de texto.
    """
     
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
     
    contraseña = "".join(secrets.choice(caracteres) for _ in range(longitud))
    
    return contraseña

def main():
    """
    Función principal que solicita datos al usuario y ejecuta la generación.
    """
    while True:
        try:
            
            longitud_str = input("Ingrese el tamaño deseado de la contraseña: ")
            longitud = int(longitud_str)
            
             
            if longitud < 8:
                print("⚠️ Para mayor seguridad, se recomienda una longitud de al menos 8 caracteres.")
            if longitud <= 0:
                print("❌ Error: La longitud debe ser un número positivo. Inténtalo de nuevo.")
                continue
 
            contraseña_generada = generar_contraseña(longitud)
            print("\n✅ Tu contraseña segura es: " + contraseña_generada)
            break  

        except ValueError:
             
            print("❌ Error: Entrada no válida. Por favor, ingresa solo números.")

 
if __name__ == "__main__":
    main()
