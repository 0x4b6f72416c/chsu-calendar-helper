import chsu_core
import calendar_core

def main():
    list=[]
    
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
            if chsu_core.open_page(driver,group):
                chsu_core.fill_list(driver,list)
            calendar_core.event_maker(list,service)

        elif x == '2':
            calendar_core.event_delete(service)
        else:
            driver.quit()
            break

if __name__=='__main__':
    main()

