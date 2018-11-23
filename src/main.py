import chsu_core
import calendar_core
from  threading import Thread
from queue import Queue


def main():
    MainQueue = Queue(31) 
    service=calendar_core.init()
    driver =chsu_core.init()        

    while True:
        print('Options:')
        print(' 1- Init node')
        print(' 2- Delete last node')
        print(' 3- Exit')
        x=input()
        
        if  x == '1':
            print("Enter correctly your group") 
            group = input()
            if  chsu_core.open_page(driver,group):
                
                thread_chsu = Thread(target=chsu_core.fill_list,args=(driver,MainQueue,))
                thread_calendar = Thread(target=calendar_core.event_maker,args=(service,MainQueue))

               
                thread_chsu.start()
                thread_calendar.start()

                thread_chsu.join()
                thread_calendar.join()

        elif x == '2':
            calendar_core.event_delete(service)
        else:
            driver.quit()
            break

if __name__=='__main__':
    main()

