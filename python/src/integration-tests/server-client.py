import multiprocessing
import subprocess

def run_script(script_path):
    try:
        subprocess.run(['python', script_path])
    except KeyboardInterrupt:
        print('Process running {} received KeyboardInterrupt. Exiting...'.format(script_path))

def basic_server_client_test():
    print('=================================')
    print('Starting basic server client test')
    print('=================================')
    scripts = ['test-server.py', 'test-client.py']  
    processes = []
    for script in scripts:
        process = multiprocessing.Process(target=run_script, args=(script,))
        process.start()
        processes.append(process)
        print('Main program continues after starting process running {}'.format(script))

    try:
        for process in processes:
            process.join()
    except KeyboardInterrupt:
        print('Main program received KeyboardInterrupt. Terminating child processes...')
        for process in processes:
            process.terminate()

    print('=========================================')
    print('basic server client test exits gracefully')
    print('=========================================')

def game_server_basic_clients():
    print('=======================================')
    print('Starting Game Server Basic Clients test')
    print('=======================================')
    scripts = ['game-server-test.py', 
                'game-client-test.py Alice',
                'game-client-test.py Bob',
                'game-client-test.py Chris',
                'game-client-test.py Dan'
                ]  
    processes = []
    for script in scripts:
        process = multiprocessing.Process(target=run_script, args=(script,))
        process.start()
        processes.append(process)
        print('Main program continues after starting process running {}'.format(script))

    try:
        for process in processes:
            process.join()
    except KeyboardInterrupt:
        print('Main program received KeyboardInterrupt. Terminating child processes...')
        for process in processes:
            process.terminate()

    print('====================================')
    print('Game Server Basic Clients gracefully')
    print('====================================')

if __name__ == "__main__":
     basic_server_client_test()
    #  game_server_basic_clients()
