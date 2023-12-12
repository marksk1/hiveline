import os

base_path = os.getenv("PROJECT_PATH")

if not base_path.endswith("/"):
    base_path += "/"

bin_path = base_path + "routing/bin"
data_path = base_path + "routing/data"
delay_path = base_path + "routing/delay_statistics"