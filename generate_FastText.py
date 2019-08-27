import csv
def get_labels(path):
    f = open(path, 'r', encoding='utf-8')

    second_labels = {}
    index = 1
    for line in f.readlines():
        label = line.strip()
        second_labels[label] = index
        index += 1

    return second_labels

if __name__ == '__main__':


    with open('data/folder/labeled_train', 'w', encoding='utf-8') as f:
        with open('data/apptype_train.dat', encoding='utf-8') as file:
            #csv_reader = csv.reader(csv_file, delimiter='\t')
            lines = file.readlines()
            label = get_labels('data/secondlabel/second_labels.txt')
            print(label)
            line_count = 0
            for row in lines:
                row = row.strip().split('\t')
                conment = row[2]
                label1 = row[1].split('|')[0]
                if '|' in row[1]:
                    label2 = row[1].split('|')[1]
                    line = "__label__{0} __label__{1} {2}".format(label[label1], label[label2], conment)
                else:
                    line = "__label__{0} {1}".format(label[label1], conment)
                line_count += 1
                f.write(line+'\n')
                # if line_count > 10:
                #     break
            print(f'Processed {line_count} lines.')
