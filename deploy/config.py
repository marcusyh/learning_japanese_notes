import os
from dotenv import load_dotenv
from argparse import Namespace

# Load environment variables from .env file
load_dotenv(os.path.expanduser('~/documents/machines'))

local = Namespace(
    hosts = ['localhost'],
    user = os.getenv('LOCAL_USER'),
    http_user = 'http'
)

remote = {
    "ggl": Namespace(
        hosts = [os.getenv('GOOGLE_VM_HOST')],
        user = os.getenv('GOOGLE_VM_USER'),
        key_filename = os.path.expanduser(os.getenv('GOOGLE_VM_KEY_FILE')),
        http_user = 'www-data'
    ),
    "ali": Namespace(
        hosts = [os.getenv('ALIYUN_VM_HOST')],
        user = os.getenv('ALIYUN_VM_USER'),
        key_filename = os.path.expanduser(os.getenv('ALIYUN_VM_KEY_FILE')),
        http_user = 'www-data'
    )
}

# development path
development_path = '~/code/mine/ja_web/data/kanji/pron/pron_list/'

# deployment path
deployment_path = '/opt/japanese_learning_web/data/kanji/pron/pron_list/'



################################
# learning source directory
################################
LEARNING_DIR = 'notes'
NOTEBOOK_DIR = 'joplin'

ONYOMI_FILENAME = '日本語_音読み'
KUNYOMI_FILENAME = '日本語_訓読み'