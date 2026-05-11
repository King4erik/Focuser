# TODO: Use csv module for logging the csv

from ctypes import byref, create_string_buffer, c_ulong, windll
from datetime import datetime

import signal
import os

import time
import sys

import re

presistence_list = []
failed_list = []
log_file = 'D:/Programming/Python/Focuser/Focuser_log.csv'

def log(message):
    try:
        with open(log_file, 'r') as f:
            lines = f.read().splitlines()
            if message in lines:
                print(f'\n[-] {message} already present')
                return

    except FileNotFoundError:
        pass

    with open(log_file, 'a') as fd:
        fd.write(f'{message}\r')
        print(f'[+] Logged: {message}')

def get_current_process():
    hwnd = windll.user32.GetForegroundWindow()
    pid = c_ulong(0)
    windll.user32.GetWindowThreadProcessId(hwnd, byref(pid))
    process_id = f'{pid.value}'

    executable = create_string_buffer(512)
    h_process = windll.kernel32.OpenProcess(0x400 | 0x10, False, pid)
    windll.psapi.GetModuleBaseNameA(h_process, None, byref(executable), 512)

    window_title = create_string_buffer(512)
    windll.user32.GetWindowTextA(hwnd, byref(window_title), 512)

    try:
        current_window = window_title.value.decode('utf-8')
    except UnicodeDecodeError as e:
        print(f'[-] Error: {e}')

        try:
            current_window = window_title.value.decode('latin-1')
        except:
            pass

    windll.kernel32.CloseHandle(hwnd)
    windll.kernel32.CloseHandle(h_process)

    return process_id, executable.value.decode(), current_window

def presistence_block(wordlist):
    with open(wordlist, 'r') as f:
        titles = [line.strip() for line in f if line.strip()]

    for title in titles:
        review = re.search(r'#(.*)', title)

        if review:
            app = review.group(1).strip()

            if app not in presistence_list:
                presistence_list.append(app)

def check_wordlist(initial_file, current_titles):
    with open(wordlist, 'r') as f:
        titles = [line.strip() for line in f if line.strip()]

    if titles != current_titles:
        return True
    else:
        return False

def kill(pid):
    try:
        os.kill(int(pid), signal.SIGTERM)
        return True

    except Exception as e:
        print(f'[-][SIGTERM] Error: {e}')

        try:
            os.kill(int(pid), signal.CTRL_C_EVENT)
        except Exception as e:
            print(f'[-][CTRL_C_EVENT] Error: {e}')
        
            try:
                os.kill(int(pid), signal.CTRL_BREAK_EVENT)
            except Exception as e:
                print(f'[-][CTRL_BREAK_EVENT] Error: {e}')
                return False

def run(wordlist):
    with open(wordlist, 'r') as f:
        titles = [line.strip() for line in f if line.strip()]
        print(f'\n {titles}')

    previous = None
    
    head = 'Date Time, PID, Executable, Window Title, Status'
    log(head)

    try:
        while True:
            current = get_current_process()

            try:
                if current != previous:
                    print("\n[i] PID:", current[0], "| Executable:", current[1], "| Window Title:", current[2])
                    sys.stdout.flush()

                    if current[1] in titles or current[2] in titles or current[1] in presistence_list or current[2] in presistence_list:
                        print(f'\n[+] Killed process: PID: {current[0]} Executable: {current[1]} Window Title: {current[2]}')
                        result = kill(current[0])

                        if result == True:
                            time_now = datetime.now()
                        
                            record = (f'{time_now}, {current[0]}, {current[1]}, {current[2]}, Success')
                            log(record)

                        else:
                            if current[0] in failed_list:
                                continue

                            else:
                                time_now = datetime.now()

                                record = (f'{time_now}, {current[0]}, {current[1]}, {current[2]}, Failed')
                                log(record)

                                failed_list.append(current[0])

                        previous = current

                    else:
                        time.sleep(1)

                else:
                    time.sleep(1)

                previous = current
                presistence_block(wordlist)
                # print("[DEBUG] ", presistence_list)

                if check_wordlist(wordlist, titles) is True:
                    with open(wordlist, 'r') as f:
                        titles = [line.strip() for line in f if line.strip()]
                        print("\n[+] The wordlist has been updated")

                else:
                    continue

            except Exception as e:
                print(f"\n[-] Error: {e}")

    except KeyboardInterrupt:
        print("\n[!!] Program ended by the user..")

if __name__ == '__main__':
    wordlist = 'D:/Programming/Python/Focuser/blocked_apps.txt'

    print("[+] The program has started")
    print("[*] The wordlist is specified in the destination: ", wordlist)
  
    print('\n[*] Description: This program is made for focusing on learning by blocking applications given by the user')
    print("\n[*] CTRL-C to exit the program")

    print('\n[*] These specific applications will be blocked:')
    
    presistence_block(wordlist)
    run(wordlist)
