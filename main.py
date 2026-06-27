#imports
import threading
from core.huginn import Huginn
from core.muninn import Muninn


#declare
def main():
    #state its starting
    print("Huginn and Muninn released")
    #try except
    try:
        #activate it
        muninn = Muninn()
        huginn = Huginn(muninn.alert_queue)
        huginn.start()
        muninn.start()
        muninn.join()
    except KeyboardInterrupt:
        print("Huginn and Muninn have returned")
    except Exception as e:
        import traceback
        traceback.print_exc()


#run it
if __name__ =="__main__":
    main()