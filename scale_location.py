import json
import numpy as np
scale = [800,600]
scale_x = (scale[0]/1600)
scale_y = (scale[1]/928)
file_json = "/home/ubuntu/Workspace/phat-intern-dev/VinAI/6Img-to-3D-at-VinAI/data_test/transform_ego.json"

with open(file_json, 'r') as f:
    input_data = json.load(f)

frame = input_data["transform"]
for key in frame.keys():
    frame[key] = np.array(frame[key])
    frame[key][0,3] *= scale_x 
    frame[key][1,3] *= scale_y

    frame[key] = frame[key].tolist()

input_data["img_size"] = scale

with open(file_json, 'w') as f:
    json.dump(input_data, f)
print("Updated data has been saved successfully.")
