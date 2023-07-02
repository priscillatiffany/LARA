import LARAListens
import LARAExplains
import LARASummarizes

def main():
    print("------------------------------------------------------")
    print("|                     L. A. R. A.                     |")
    print("|    Linguistic Analysis and Repository Assistant     |")
    print("|                      Build 0.0                      |")
    print("-----------------------------------------------------")

    print("\n---\n")
    print("L.A.R.A.'s features:")
    print("  1. Listens - Listens and convert spoken language into written text")
    print("  2. Explains - Provides explanation of technical terms")
    print("  3. Summarizes - Provides summary of meetings")
    print("\n---\n")


    start = input("Do you want to start meeting [Y/N]? ")

    if start.lower() == 'y':
        transcriptFile = LARAListens.listensToSpeech()

        while True:
            print("\nL.A.R.A.'s commands:")
            print("  1. EXPLAIN - Explain technical terms")
            print("  2. SUMMARIZE - Summarize meetings")
            print("  3. EXIT - Exit L.A.R.A.") 

            postMeetingMenu = input("\nI want L.A.R.A to: ")
            if postMeetingMenu == '1' or postMeetingMenu.lower() == 'explain':
                LARAExplains.explainMeThis()
            elif postMeetingMenu == '2' or postMeetingMenu.lower() == 'summarize':
                LARASummarizes.summarizeDiscussion(transcriptFile)
            elif postMeetingMenu == '3' or postMeetingMenu.lower() == 'exit':
                print("\nSee you next time!")
                quit()
        
    elif start.lower() == 'n':
        print("\nSee you next time!")
    else:
        print("\nSorry. L.A.R.A. does not understand that")
        quit()

if __name__ == "__main__":
    main()