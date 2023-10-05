import subprocess
import time

def git_push():
    try:
        subprocess.run(['git' , 'add' , '.'])
        subprocess.run(['git', 'commit', '-m', 'Automated hourly commit'])
        subprocess.run(['git', 'push', 'origin', 'master'])
        print("git push success")
    except:
        print("error!")

if __name__ == "__main__":

    while True: 

        git_push() 
        time.sleep(3600)



