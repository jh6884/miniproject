import yaml, os
dir_path = 'C:\\Users\\405\\projects\\miniproject\\data\\Bbox_27_new\\'
yaml_path = 'P1025_07.yaml'
lst = os.listdir()
with open(yaml_path, 'r') as file:
    data = yaml.safe_load(file)

    for i in range(49):
        file_name = data['annotations']['image'][i]['name']
        print(file_name)
        for j in range(len(data['annotations']['image'][i]['box'])):
            box = data['annotations']['image'][i]['box'][j]
            x = box['xtl']
            y = box['ytl']
            w = float(box['xbr']) - float(box['xtl'])
            h = float(box['ybr']) - float(box['ytl'])
            print(f'{x}, {y}, {w:.2f}, {h:.2f}', end=' / ')
        print()