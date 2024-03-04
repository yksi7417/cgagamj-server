import multiprocessing
import subprocess

def run_script(script_path):
    try:
        subprocess.run(['python', script_path])
    except KeyboardInterrupt:
        print('Process running {} received KeyboardInterrupt. Exiting...'.format(script_path))

if __name__ == "__main__":
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

    print('Main program exits gracefully')
