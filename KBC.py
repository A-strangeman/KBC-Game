questions=[["What is the capital of india","New Delhi","Kathmandu","Kolkata","Mumbai",1],
          ["What is the capital of Nepal","Pokhara","Lumbini","Kathmandu","Biratnagar",3],
          ["A byte corresponds to a cluster of how many bits","6 bits","8 bits","10 bits","12 bits",2],
          ["CPU is also reffered to as","Microchip","Decoder","Coder","Microprocessor",4],
          ["what is capital of china","Beijing","taizing","Hongkong","Dhaka",1],
          ["what is national bird of India","peacock","Danfe","parrot","eagle",1],
          ["what is national bird of Nepal","peacock","Danfe","parrot","eagle",2],
          ["Among the following, which is a network","MAN","WAN","LAN","All of these",4],
          ["What does Fn mean in Fn key of the computer keyboard","Function","Finish","Fun","Final",1],
          ["The full form of GB is","Giga Boot","Giga Bot","Giga Byte","Giga Bar",3],
          ["what is the full form of RAM","Random Application Machine","Random Access Memory","Real Absolute Memory","Read Access Manual",2],
          ["what is the full form of WWW","World Wide Web ","World Website Web","World Widely Web","World Wing Web",1],
          ["What is the Height of the Mount Everest",8848,8858,8888,8844,1]
          ]
levels=[1000,2000,4000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000,70000000]
money=0
for i in range(0,len(questions)):
    question=questions[i]
    print(f"questions for amount Rs",levels[i])
    print(question[0])
    print("a.",question[1],                 "b.",question[2])
    print("c.",question[3],                 "d.",question[4])
    reply=int(input("Enter a number between 1 to 4 :"))
    if reply==question[5]:
        print("Correct Answer, You Have Won Rs.",levels[i])
        print("__________________________________________")
        if (i==3):
            money=10000
        elif(i==8):
            money=320000
        elif(i==13):
            money=10000000
    else:
        print("wrong Answer")
        break
print("You earn a ",money)