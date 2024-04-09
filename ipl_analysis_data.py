import pandas as pd
import time
import sqlalchemy
import matplotlib.pyplot as plt

df = pd.DataFrame()
csv_file = "matches.csv"


def introduction():
    msg = '''

          In this project we are going to analyse the same dataset using Python Pandas on windows machine but
          the project can be run on any machine support Python and Pandas. Besides pandas we also used 
          matplotlib python module for visualization of this dataset. 
 
          The whole project is divided into four major parts ie reading, analysis, visualization and export. all these
          part are further divided into menus for easy navigation.'''
    for x in msg:
        print(x, end='')
        time.sleep(0.002)
    wait = input('Press any key to continue.....')


def made_by():
    msg = ''' 
            IPL Data Analysis made by       : Pallav agrawal
            Roll No                         : 2242157 
            College Name                     : S.S Jain Subodh PG college
            session                         : 2023-24
            
            Thanks for evaluating my Project.
            \n\n\n
        '''

    for x in msg:
        print(x, end='')
        time.sleep(0.002)

    wait = input('Press any key to continue.....')


def read_csv_file():
    df = pd.read_csv(csv_file)
    print(df)

# name of function      : clear
# purpose               : clear output screen


def clear():
    for x in range(65):
               print()


def data_analysis_menu():
        df = pd.read_csv(csv_file)
        while True:
            clear()
            print('\n\nD A T A   A N A L Y S I S   M E N U  ')
            print('_'*100,'\n')
            print('1.   Show Whole DataFrame')
            print('2.   Show Columns')
            print('3.   Show Top Rows')
            print('4.   Show Bottom Rows')
            print('5.   Show Specific Column')
            print('6.   Add a New Record')
            print('7.   Add a New Column')
            print('8.   Delete a Column')
            print('9.   Delete a Record')
            print('10.  Match win By Maximum Runs')
            print('11.  Match win By Minimum Runs')
            print('12.  Match win By Maximum Wickets')
            print('13.  Match win By Minimum Wickets')
            print('14.  Top 5 Match Winners Team')
            print('15.  Top 10 man of the macth Player')
            print('16.  Data Summery')
            print('17.  Exit (Move to main menu)')
            ch = int(input('\n\nEnter your choice:'))
            if ch == 1:
                print(df)
                wait = input('\n\n\n Press any key to continuee.....')
            if ch == 2:
                print(df.columns)
                wait = input('\n\n\n Press any key to continuee.....')
            if ch == 3:
                n = int(input('Enter Total rows you want to show :'))
                print(df.head(n))
                wait = input('\n\n\n Press any key to continuee.....')
            if ch == 4:
                n = int(input('Enter Total rows you want to show :'))
                print(df.tail(n))
                wait = input('\n\n\n Press any key to continuee.....')
            if ch == 5:
                print(df.columns)
                col_name = input('Enter Column Name that You want to print : ')
                print(df[col_name])
                wait = input('\n\n\n Press any key to continuee.....')
            if ch == 6:
                a = input('Enter Match ID :')
                b = input('Enter IPL season :')
                c = input('Enter City Name :')
                d = input('Enter Match date :')
                e = input('Enter Team 1 Name  :')
                f = input('Enter Team 2 Name :')
                g = input('Enter Toss Winner :')
                h = input('Enter Toss Decision :')
                i = input('Enter Result (Normal /tie/ DL ) :')
                j = input('Enter Duckwoth Lewis Method applied (0 for No, 1 for Yes ) :) :')
                k = input('Enter Winner Team :')
                l = input('Enter Win By runs :')
                m = input('Enter Win By Wickets :')
                n = input('Enter Man of the Match Player :')
                data = {'id': a, 'season': b, 'city': c,
                        'date': d, 'team1': e, 'team2': f, 'toss_winner': g,
                        'toss_decision':h,'result':i,'dl_applied':j,'winner':k,
                        'win_by_runs':l,'win_by_wickets':m,'player_of_match':n
                        
                        }
                df = df.append(data, ignore_index=True)
                print(df)
                wait = input('\n\n\n Press any key to continuee.....')
            if ch == 7:
                col_name = input('Enter new column name :')
                col_value = input('Enter default column value :')
                df[col_name] = col_value
                print(df)
                print('\n\n\n Press any key to continue....')
                wait = input()

            if ch == 8:
                col_name = input('Enter column Name to delete :')
                del df[col_name]
                print(df)
                print('\n\n\n Press any key to continue....')
                wait = input()

            if ch == 9:
                index_no = int(
                    input('Enter the Index Number that You want to delete :'))
                df = df.drop(df.index[index_no])
                print(df)
                print('\n\n\n Press any key to continue....')
                wait = input()

            if ch == 10:
                df1= df.sort_values('win_by_runs',ascending=False).head(1)
                print(df1)
                wait = input('\n\n\n Press any key to continue....')

            if ch == 11:
                df1 = df.sort_values('win_by_runs').head(1)
                print(df1)
                wait = input('\n\n\n Press any key to continue....')
            if ch == 12: #macth won by maximum wicket
                df1 = df.sort_values('win_by_wickets',ascending=False).head(1)
                print(df1)
                wait = input('\n\n\n Press any key to continue....')
            if ch == 13:  # macth won by minimum wicket
                df1 = df.sort_values('win_by_wickets').head(1)
                print(df1)
                wait = input('\n\n\n Press any key to continue....')
            if ch == 14: #most macth winner team
                df1 = df.groupby('winner').count()
                df2=df1.sort_values('result',ascending=False).head(5)
                print(df2)
                wait = input('\n\n\n Press any key to continue....')
            
            if ch == 15:  # most man of the macth player
                df1 = df.groupby('player_of_match').count()
                df2 = df1.sort_values('result', ascending=False).head(10)
                print(df2)
                wait = input('\n\n\n Press any key to continue....')
            if ch == 16:
                print(df.describe()) 
                wait = input('\n\n\n Press any key to continue....')
            if ch == 17:
                break


# name of function      : graph
# purpose               : To generate a Graph menu
def graph():
    df = pd.read_csv(csv_file)
    while True:
        clear()
        print('\nGRAPH MENU ')
        print('_'*100)
        print('\n1. Season wise Matches - Line Graph')
        print('\n2. Season wise Matches - Bar Graph')
        print('\n3. Season wise Matches - Horizontal Bar Graph')
        print('\n4.  Exit (Move to main menu)\n')
        ch = int(input('Enter your choice:'))

        if ch == 1:
            g = df.groupby('season')
            x = df['season'].unique()
            y = g['season'].count()
            #plt.xticks(rotation='vertical')
            plt.xlabel('Season')
            plt.ylabel('Matches')
            plt.title('Season wise Matches')
            plt.grid(True)
            plt.plot(x, y)  #line graph
            plt.show()

        if ch == 2:
            g = df.groupby('season')
            x = df['season'].unique()
            y = g['season'].count()
            #plt.xticks(rotation='vertical')
            plt.xlabel('Season')
            plt.ylabel('Matches')
            plt.title('Season wise Matches')
            plt.bar(x, y)  #bar graph
            plt.grid(True)
            plt.show()
            
        if ch == 3:
            g = df.groupby('season')
            x = df['season'].unique()
            y = g['season'].count()
            #plt.xticks(rotation='vertical')
            plt.xlabel('Season')
            plt.ylabel('Matches')
            plt.title('Season wise Matches')
            plt.grid(True)
            plt.barh(x, y)
            plt.show()
           
        if ch ==4:
            break


# function name          : export_menu
# purpose                : function to generate export menu
def export_menu():
    df = pd.read_csv(csv_file)
    while True:
        clear()
        print('\n\nE X P O R T    M  E N U ')
        print('_'*100)
        print()
        print('1.  CSV File\n')
        print('2.  Exit (Move to main menu)')
        ch = int(input('Enter your Choice : '))

        if ch == 1:
            df.to_csv('matches.csv')
            print('\n\nCheck your new file "matches.csv"  on C: Drive.....')
            wait = input('\n\n\n Press any key to continuee.....')


        if ch == 2:
            break


def main_menu():
           clear()
           introduction()
           while True:
                      clear()
                      print('MAIN MENU ')
                      print('_'*100)
                      print()
                      print('1.  Read CSV File\n')
                      print('2.  Data Analysis Menu\n')
                      print('3.  Graph Menu\n')
                      print('4.  Export Data\n')
                      print('5.  Exit\n')
                      choice = int(input("Enter your choice :"))

                      if choice == 1:
                                read_csv_file()
                                wait = input(
                                    '\n\n Press any key to continue....')

                      if choice == 2:
                                data_analysis_menu()
                                wait = input('\n\n Press any key to continue....')

                      if choice == 3:
                                graph()
                                wait = input('\n\n Press any key to continue....')
                      if choice == 4:
                                export_menu()
                                wait = input(
                                    '\n\n Press any key to continue....')

                      if choice == 5:
                                 break
           clear()
           made_by()


# call your main menu
main_menu()
