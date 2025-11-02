import os
import time
from datetime import datetime, timedelta

def period_safe_copy(path):
    if not os.path.exists(path):
        raise FileNotFoundError("El directorio especificado no existe")
    if not os.path.isdir(path):
        raise NotADirectoryError(f"{path} no es un directorio")

    while True:
        now = datetime.now()
        dt_now = now.replace(second=0, microsecond=0)
        dt_min = dt_now.strftime("%Y%m%d_%H%M")

        dest_dir = os.path.join(path, "backup", dt_min)
        os.makedirs(dest_dir, exist_ok=True)

        for item in os.listdir(path):
            if item == "backup":
                continue

            src_path = os.path.join(path, item)
            
            if not os.path.isfile(src_path):
                continue
        
            dest_path = os.path.join(dest_dir, item)
            try:
                # with open(src_path, "r") as src_file, open(dest_path, "w") as dest_file:
                #     dest_file.write(src_file.read())

                with open(src_path, "r", encoding="utf-8") as src_file:
                    data = src_file.read()
                with open(dest_path, "w", encoding="utf-8") as dest_file:
                    dest_file.write(data)
            except Exception as e:
                print(f"No se pudo copiar {item}: {e}")

        print(f"Realizada una copia de seguridad en {dest_dir} con éxito")
    
        next_min = dt_now + timedelta(minutes=1)
        now2 = datetime.now()
        time.sleep(max(0.0, (next_min - now2).total_seconds()))

path = input("Indica la ruta a la que quieres hacer copias de seguridad:\n")

try:
    period_safe_copy(path)
except KeyboardInterrupt:
    print("\nDetenido por el usuario.")
except Exception as e:
    print(e)
