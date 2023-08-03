import csv
from oss2 import Auth, Bucket

# 1. 从CSV文件读取文件名
def read_filenames_from_csv(csv_file):
    filenames = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            filenames.append(row[0])  # 假设文件名在CSV的第一列
    return filenames

# 2. 使用Alibaba Cloud的Python SDK从OSS下载文件
def download_from_oss(filenames, oss_config):
    auth = Auth(oss_config['access_key_id'], oss_config['access_key_secret'])
    bucket = Bucket(auth, oss_config['endpoint'], oss_config['bucket_name'])

    for filename in filenames:
        local_filename = filename  # 你可以更改这个，如果你想在本地使用不同的文件名
        bucket.get_object_to_file(filename, local_filename)

if __name__ == '__main__':
    csv_file = 'your_file.csv'  # 你的CSV文件路径
    oss_config = {
        'access_key_id': 'your_access_key_id',
        'access_key_secret': 'your_access_key_secret',
        'endpoint': 'oss-cn-hangzhou.aliyuncs.com',  # 根据你的bucket地域更改
        'bucket_name': 'your_bucket_name'
    }

    filenames = read_filenames_from_csv(csv_file)
    download_from_oss(filenames, oss_config)
