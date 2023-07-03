## Libreria `os` y `pathlib`

| `os` and `os.path`           | `pathlib`                                     |
| ---------------------------- | --------------------------------------------- |
| `os.path.abspath()`          | `Path.absolute()`                             |
| `os.path.realpath()`         | `Path.resolve()`                              |
| `os.chmod()`                 | `Path.chmod()`                                |
| `os.mkdir()`                 | `Path.mkdir()`                                |
| `os.makedirs()`              | `Path.mkdir()`                                |
| `os.rename()`                | `Path.rename()`                               |
| `os.replace()`               | `Path.replace()`                              |
| `os.rmdir()`                 | `Path.rmdir()`                                |
| `os.remove()`, `os.unlink()` | `Path.unlink()`                               |
| `os.getcwd()`                | `Path.cwd()`                                  |
| `os.path.exists()`           | `Path.exists()`                               |
| `os.path.expanduser()`       | `Path.expanduser()` and `Path.home()`         |
| `os.listdir()`               | `Path.iterdir()`                              |
| `os.path.isdir()`            | `Path.is_dir()`                               |
| `os.path.isfile()`           | `Path.is_file()`                              |
| `os.path.islink()`           | `Path.is_symlink()`                           |
| `os.link()`                  | `Path.hardlink_to()`                          |
| `os.symlink()`               | `Path.symlink_to()`                           |
| `os.readlink()`              | `Path.readlink()`                             |
| `os.path.relpath()`          | `PurePath.relative_to()`                      |
| `os.stat()`                  | `Path.stat()`, `Path.owner()`, `Path.group()` |
| `os.path.isabs()`            | `PurePath.is_absolute()`                      |
| `os.path.join()`             | `PurePath.joinpath()`                         |
| `os.path.basename()`         | `PurePath.name`                               |
| `os.path.dirname()`          | `PurePath.parent`                             |
| `os.path.samefile()`         | `Path.samefile()`                             |
| `os.path.splitext()`         | `PurePath.stem` and `PurePath.suffix`         |


---
## Libreria `json`

| `json`       | Accion                                             |
| ------------ | -------------------------------------------------- |
| `json.load`  | Obtener informacion de un archivo a un diccionario |
| `json.dump`  | Guardar informacion de un diccionario a un archivo |
| `json.loads` | Convierte un diccionario a un string               |
| `json.dumps` | Convierte un string a un diccionario               |


---
## Libreria `yaml` y `ruamel.yaml`

| `yaml`                                                                 | `ruamel.yaml`                                         |
| ---------------------------------------------------------------------- | ----------------------------------------------------- |
| `import yaml`                                                          | `from ruamel.yaml import YAML`                        |
| Iniciarlo: `none`                                                      | Iniciarlo: `yaml = YAML(typ="safe")`                  |
| `yaml.load(file, yaml.SafeLoader)`, <br>`yaml.safe_load(file)`         | `yaml.load(file)`                                     |
| `yaml.load_all(file, yaml.SafeLoader)`, <br>`yaml.safe_load_all(file)` | `yaml.load_all(file)`                                 |
| `yaml.dump(dict, file)`, <br>`yaml.safe_dump(dict, file)`              | `yaml.dump(dict, file)` or<br>`yaml.dump(dict, Path)` |


---
## Funcion `open()`

| Metodo | Accion                                                 |
| ------ | ------------------------------------------------------ |
| `"r"`  | Leer (Read), error si el archivo no existe             |
| `"a"`  | Agregar (Append), crea el archivo si no existe         |
| `"w"`  | Escribir (Write), crea el archivo si no existe         |
| `"x"`  | Leer (Read), error si el archivo existe                |
| `"t"`  | Texto (Text), Valor por defecto                        |
| `"b"`  | Binario (Binary), Archivos binarios (imagenes, audios) |
