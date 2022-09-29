from pathlib import Path

module_name1 = "-".join(Path(__file__).parts[3:]).replace(".py", "")
project_path = "/".join(Path(__file__).parts[3:-2]).replace(".py", "")
module_name2 = "-".join(Path(__file__).parts[3:1]).replace(".py", "")
print(module_name1)
print(project_path)
