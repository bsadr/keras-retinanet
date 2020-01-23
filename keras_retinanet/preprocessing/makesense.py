import os
import numpy as np
import argparse


def get_data(input_path):
    annot_path = os.path.join(input_path, 'annotations')
    imgs_path = os.path.join(input_path, 'images')
    annots = [os.path.join(annot_path, s) for s in os.listdir(annot_path)]
    classes = []
    train_lines = []
    test_lines = []
    filenames = []
    for annot in annots:
        with open(annot, 'r') as f:
            print('Parsing annotation files (made by makesense.ai) from {}'.format(annot))
            for line in f:
                line_split = line.strip().split(',')
                (class_name, xa, ya, xb, yb, filename, img_width, img_height) = line_split
                x1 = np.min(xa, xb)
                x2 = np.max(xa, xb)
                y1 = np.min(ya, yb)
                y2 = np.max(ya, yb)
                filepath = os.path.join(imgs_path, filename)
                if class_name not in classes:
                    classes.append(class_name)
                line_out = ",".join([filepath, x1, y1, x2, y2, class_name])
                line_out += '\n'
                if np.random.randint(0, 15) > 0 and filename not in filenames:
                    filenames.append(filename)
                    train_lines.append(line_out)
                else:
                    test_lines.append(line_out)
    class_lines = []
    for i, c in enumerate(classes):
        class_lines.append('{},{}\n'.format(c, i))
    with open(os.path.join(input_path, 'classes.csv'), "w") as f:
        f.writelines(class_lines)
    with open(os.path.join(input_path, 'train_annotations.csv'), "w") as f:
        f.writelines(train_lines)
    with open(os.path.join(input_path, 'val_annotations.csv'), "w") as f:
        f.writelines(test_lines)
    return


parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input_path', action='store', help='path to training data', required=True)
args = parser.parse_args()
get_data(args.input_path)
