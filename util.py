import random
import string
import json
import os
import torch

def generate_id():
    sw_id = "".join(random.choice("".join([random.choice(
        string.ascii_letters + string.digits)
        for ch in range(4)])) for _ in range(4))
    return sw_id


def dump_json_config(conf_file_name, config):
    with conf_file_name.open("w+") as conf:
        json.dump(config, conf, indent=4, sort_keys=True,
                  default=lambda o: "<object>")


def check_dir(directory):
    # create the folder if it does not exit
    if not directory == "" and not os.path.exists(directory):
        print(f"Folder {directory} does not exist! Creating...")
        os.makedirs(directory)


def load_checkpoint(model, checkpoint_path, device="cpu"):
    device = torch.device(device)
    model_ckp = torch.load(checkpoint_path, map_location=device)
    model.load_state_dict(model_ckp["model_state_dict"])
    return model