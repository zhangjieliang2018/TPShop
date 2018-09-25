import yaml


def data_analyze(name):
    file_name = "./" + name + "_data.yaml"
    data_values = []
    with open(file_name, 'r', encoding='utf-8') as f:
        data = yaml.load(f)
        for i in data.values():
            data_values.append(i)
        return data_values



