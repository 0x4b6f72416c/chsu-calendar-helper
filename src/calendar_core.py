
import datetime
import googleapiclient.discovery 
import httplib2 
import oauth2client  
from oauth2client import file
import re

def parser(day,time):

    day = day.replace(' ','')
    day= re.split(r'[.]\s*',day)                
    day=day[2]+'-'+day[1]+'-'+day[0]
    day = day.replace(' ','')
    # '08-30 - 10-00'
    time = re.split(r'[-]\s*',time)
    start = time[0]+':'+time[1].replace(' ','')+':00'
    end = time[2].replace(' ','')+':'+time[3]+':00'
    return  [day+'T'+start,day+'T'+end]

def event_delete(service):

    with open('eventTable.txt','r')  as fb:

        node = fb.readline()
        if node:
            node=re.split(r'[:]\s*',node) 
            node.pop() 
            print(" eventId:") 
            for event in node:
                service.events().delete(calendarId='primary',eventId=event).execute()
                print("\t"+event)    
        else:
            print("Node list is empty")

#data = [day,[t a b],[t1 a1 b1]]
def event_maker(service,rq):
    eventNode =''
    GMT_OFF ='+03:00'
    while True:
        data=rq.get()
        if data == 'last':
            break
        else:
            for i in range(1,len(data)):
                time_this = parser(data[0],data[i][0]) 
                event = {
                'summary':data[i][1],
                'start':{'dateTime':time_this[0]+'%s'%GMT_OFF},
                'location':data[i][2],
                'colorId':'1',
                'end':{'dateTime':time_this[1]+'%s'%GMT_OFF}
                }
                cur_event = service.events().insert(calendarId='primary',sendNotifications=False,body=event).execute()
                eventNode+=str(cur_event['id'])+':' 
    with open('eventTable.txt','w') as fd:
        fd.write(eventNode+'\n')

def init(): 
    url ='https://www.googleapis.com/auth/calendar'
    flags = None
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = oauth2client.client.flow_from_clientsecrets('credentials.json', url)
        creds = oauth2client.tools.run_flow(flow, store)
    service = googleapiclient.discovery.build('calendar', 'v3',http=creds.authorize(httplib2.Http()))
    
    return service

