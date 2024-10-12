import os
import shutil
import filecmp
import config
from file_util import prepare_file_path
   

def deploy_learning():
    dst_pron_list_path = os.path.join(config.WEBUI_DEPLOY_DIR, config.PRON_LIST_DIR)
    prepare_file_path(dst_pron_list_path, is_dir=True, delete_if_exists=False, create_if_not_exists=True)

    onyomi_src = os.path.join(config.LEARNING_DIR, f'{config.ONYOMI_FILENAME}.md')
    onyomi_dst = os.path.join(dst_pron_list_path, f'{config.ONYOMI_FILENAME}_勉強中.md')
    if os.path.exists(onyomi_src):
        if not os.path.exists(onyomi_dst) or not filecmp.cmp(onyomi_src, onyomi_dst, shallow=False):
            shutil.copy(onyomi_src, onyomi_dst)

    kunyomi_src = os.path.join(config.LEARNING_DIR, f'{config.KUNYOMI_FILENAME}.md')
    kunyomi_dst = os.path.join(dst_pron_list_path, f'{config.KUNYOMI_FILENAME}_勉強中.md')
    if os.path.exists(kunyomi_src):
        if not os.path.exists(kunyomi_dst) or not filecmp.cmp(kunyomi_src, kunyomi_dst, shallow=False):
            shutil.copy(kunyomi_src, kunyomi_dst)


if __name__ == '__main__':
    deploy_learning()