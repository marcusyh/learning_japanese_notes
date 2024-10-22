import os
from fabric import Connection, task
from invoke import Collection, Program
from invoke import run as local_run
import config


def sync_files(src, dest, is_remote, conn):
    if is_remote and conn:
        # 确保目标目录存在
        conn.run(f'mkdir -p {os.path.dirname(dest)}')
        # 使用rsync进行远程同步
        local_run(f'rsync -avz --delete -e "ssh -i {conn.connect_kwargs["key_filename"][0]}" {src} {conn.user}@{conn.host}:{dest}')
    else:
        local_run(f'rsync -avr --delete {src} {dest}')


def do_deploy(
        run_func, 
        target_dir,
        clean=False,
        is_remote=False,
        conn=None
    ):
    data_root_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), config.LEARNING_DIR)

    for filename in os.listdir(data_root_path):
        target_path = os.path.join(target_dir, filename)
        if clean:
            if is_remote:
                conn.run(f'rm -rf {target_path}')
            else:
                local_run(f'rm -rf {target_path}')
        else:
            sync_files(
                os.path.join(data_root_path, filename), 
                target_path, 
                is_remote, 
                conn
            )

# parameters
deploy_parameters = {
    'clean': 'Remove files from target location',
}

# Create a namespace for our tasks
ns = Collection()

@task(help=deploy_parameters)
def dev(c, clean=False):
    """
    Deploy to development environment of ja_web repository
    """
    do_deploy(local_run, config.development_path, clean)


@task(help=deploy_parameters)
def local(c, clean=False):
    """
    Deploy to local machine
    """
    do_deploy(local_run, config.deployment_path, clean)


@task(help=deploy_parameters)
def ggl(c, clean=False):
    """
    Deploy to Google Cloud
    """
    rmtcfg = config.remote['ggl']
    with Connection(rmtcfg.hosts[0], user=rmtcfg.user, connect_kwargs={"key_filename": rmtcfg.key_filename}) as conn:
        do_deploy(conn.run, config.deployment_path, clean, is_remote=True, conn=conn)
    

@task(help=deploy_parameters)
def ali(c, clean=False):
    """
    Deploy to Alibaba Cloud
    """
    rmtcfg = config.remote['ali']
    with Connection(rmtcfg.hosts[0], user=rmtcfg.user, connect_kwargs={"key_filename": rmtcfg.key_filename}) as conn:
        do_deploy(conn.run, config.deployment_path, clean, is_remote=True, conn=conn)
    

# Add tasks to namespace
ns.add_task(dev)
ns.add_task(local)
ns.add_task(ggl)
ns.add_task(ali)

# Create a custom program
program = Program(namespace=ns, )

# Use this if you want to run the script directly
if __name__ == "__main__":
    program.run()