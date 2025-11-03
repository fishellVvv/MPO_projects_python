import os
import time
from datetime import datetime

def make_snapshot(path):
    snap = {}
    for item in os.listdir(path):
        if item == "log.txt":
            continue

        src_path = os.path.join(path, item)
        if not os.path.isfile(src_path):
            continue
    
        try:
            item_stat = os.stat(src_path)
            snap[item] = (item_stat.st_mtime, item_stat.st_size)
        except Exception:
            continue
    
    return snap

def monitor_path(path):
    if not os.path.exists(path):
        raise FileNotFoundError("El directorio especificado no existe")
    if not os.path.isdir(path):
        raise NotADirectoryError(f"{path} no es un directorio")
    
    prev_snap = {}
    while True:
        # (si no existe estado anterior, crearlo)
        if not prev_snap:
            prev_snap = make_snapshot(path)
            time.sleep(3)
            continue

        # leer los archivos del directorio
        curr_snap = make_snapshot(path)
        # comparar con el último estado guardado
        # registrar los cambios
            # creados: claves en curr que no están en prev.
        created = curr_snap.keys() - prev_snap.keys()
            # eliminados: claves en prev que no están en curr.
        deleted = prev_snap.keys() - curr_snap.keys()
        # modificados: intersección de claves donde (mtime, size) difiere.
        modified = {item for item in (curr_snap.keys() & prev_snap.keys()) if curr_snap[item] != prev_snap[item]}

        if created or deleted or modified:
            with open(os.path.join(path, "log.txt"), "a", encoding="utf-8") as log:
                for item in sorted(created):
                    mtime, size = curr_snap[item]
                    mtime_formated = datetime.fromtimestamp(mtime).isoformat(timespec="seconds")
                    dt_sec = datetime.now().isoformat(timespec="seconds")
                    log_line = (f"{dt_sec} | CREATED | {item} | {size} bytes | {mtime_formated}\n")
                    log.write(log_line)
                    print(log_line, end="")
                for item in sorted(deleted):
                    mtime, size = prev_snap[item]
                    mtime_formated = datetime.fromtimestamp(mtime).isoformat(timespec="seconds")
                    dt_sec = datetime.now().isoformat(timespec="seconds")
                    log_line = (f"{dt_sec} | DELETED | {item} | {size} bytes | {mtime_formated}\n")
                    log.write(log_line)
                    print(log_line, end="")
                for item in sorted(modified):
                    mtime, size = curr_snap[item]
                    mtime_formated = datetime.fromtimestamp(mtime).isoformat(timespec="seconds")
                    dt_sec = datetime.now().isoformat(timespec="seconds")
                    log_line = (f"{dt_sec} | MODIFIED | {item} | {size} bytes | {mtime_formated}\n")
                    log.write(log_line)
                    print(log_line, end="")

        # guardar el estado actual
        prev_snap = curr_snap

        time.sleep(3)

path = input("Indica la ruta que quieres monitorear:\n")

try:
    monitor_path(path)
except KeyboardInterrupt:
    print("\nDetenido por el usuario.")
except Exception as e:
    print(e)
