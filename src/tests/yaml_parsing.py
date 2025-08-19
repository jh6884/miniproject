import yaml, os

dir_path = '../../data/dataset/yaml/'
lst = os.listdir(dir_path)
vehicles = ['car', 'truck', 'scooter', 'motorcycle', 'bus']
passanger = ['person', 'wheelchair']
count = 1

for file in lst:
    file_path = os.path.join(dir_path+file)
    with open(file_path) as f:
        data = yaml.safe_load(f)
        img = data['annotations']['image']
        for i in range(len(img)):
            box = img[i]['box']
            if type(box) is list:
                for j in range(len(box)):
                    xtl = float(box[j]['xtl'])
                    xbr = float(box[j]['xbr'])
                    ytl = float(box[j]['ytl'])
                    ybr = float(box[j]['ybr'])
                    lable = box[j]['label']
                    if lable in vehicles:
                        class_num = 0
                    elif lable in passanger:
                        class_num = 1
                    elif lable == 'traffic_light':
                        class_num = 2
                    else:
                        class_num = 3
                    x_center = round((xtl+xbr)/(2*1920),6)
                    y_center = round((ytl+ybr)/(2*1080),6)
                    width = round((xbr-xtl)/1920,6)
                    height = round((ybr-ytl)/1080,6)
                    with open(os.path.join('../../data/dataset/txt/'+img[i]['name'][0:-4]+'.txt'), 'a') as t:
                        t.write(f'{class_num} {x_center} {y_center} {width} {height}\n')
                        print(f'{count}개 영역 annotation 완료, {img[i]['name']}')
                        count += 1
                        t.close()
            else:
                xtl = float(box['xtl'])
                xbr = float(box['xbr'])
                ytl = float(box['ytl'])
                ybr = float(box['ybr'])
                lable = box['label']
                if lable in vehicles:
                    class_num = 0
                elif lable in passanger:
                    class_num = 1
                elif lable == 'traffic_light':
                    class_num = 2
                else:
                    class_num = 3
                x_center = round((xtl+xbr)/(2*1920),6)
                y_center = round((ytl+ybr)/(2*1080),6)
                width = round((xbr-xtl)/1920,6)
                height = round((ybr-ytl)/1080,6)
                with open(os.path.join('../../data/dataset/txt/'+img[i]['name'][0:-4]+'.txt'), 'a') as t:
                    t.write(f'{class_num} {x_center} {y_center} {width} {height}\n')
                    print(f'{count}개 영역 annotation 완료, {img[i]['name']}')
                    count += 1
                    t.close()