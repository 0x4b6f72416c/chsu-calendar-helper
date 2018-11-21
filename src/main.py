import chsu_core
import calendar_core

def main():
    list=[]
    service=calendar_core.init()
    
    while True:
        print('Options:')
        print(' 1- Init ')
        print(' 2- Delete last event')
        print(' 3- Exit')
        x=input()
        if  x == '1':
            chsu_core.init(list)        # Collacting date from the site and fill the list 
            calendar_core.event_maker(list,service)
        elif x == '2':
            calendar_core.event_delete(service)
        else:
            break

if __name__=='__main__':
    main()

