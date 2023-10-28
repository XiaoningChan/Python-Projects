import pypivot_functions as pf

default_database =  [{'Name': 'Albert', 'Gender': 'Male', 'Age':21,'Employment':'Employee','Salary':4800},
                     {'Name': 'Bob', 'Gender': 'Male', 'Age':21,'Employment':'Employee','Salary':5000},
                     {'Name': 'Charles', 'Gender': 'Male', 'Age':22,'Employment':'Employee','Salary':6000},
                     {'Name': 'Derrick', 'Gender': 'Male', 'Age':23,'Employment':'Self-Employed','Salary':10000},
                     {'Name': 'Fred', 'Gender': 'Male', 'Age':23,'Employment':'Unemployed','Salary':1200},
                     {'Name': 'George', 'Gender': 'Male', 'Age':25,'Employment':'Self-Employed','Salary':12000},
                     {'Name': 'Hubert', 'Gender': 'Male', 'Age':26,'Employment':'Unemployed','Salary':1000},
                     {'Name': 'Issac', 'Gender': 'Male', 'Age':28,'Employment':'Employee','Salary':3000},
                     {'Name': 'John', 'Gender': 'Male', 'Age':30,'Employment':'Employee','Salary':2500},
                     {'Name': 'Kerry', 'Gender': 'Male', 'Age':30,'Employment':'Self-Employed','Salary':8500},
                     {'Name': 'Linda', 'Gender': 'Female', 'Age':21,'Employment':'Self-Employed','Salary':9000},
                     {'Name': 'Mindy', 'Gender': 'Female', 'Age':21,'Employment':'Self-Employed','Salary':8500},
                     {'Name': 'Nicole', 'Gender': 'Female', 'Age':22,'Employment':'Unemployed','Salary':2000},
                     {'Name': 'Oprah', 'Gender': 'Female', 'Age':22,'Employment':'Employee','Salary':6500},
                     {'Name': 'Penny', 'Gender': 'Female', 'Age':23,'Employment':'Employee','Salary':7500},
                     {'Name': 'Queenie', 'Gender': 'Female', 'Age':25,'Employment':'Employee','Salary':7000},
                     {'Name': 'Ruby', 'Gender': 'Female', 'Age':25,'Employment':'Employee','Salary':4000},
                     {'Name': 'Stacy', 'Gender': 'Female', 'Age':27,'Employment':'Employee','Salary':3500},
                     {'Name': 'Tiffany', 'Gender': 'Female', 'Age':27,'Employment':'Self-Employed','Salary':5000},
                     {'Name': 'Ursula', 'Gender': 'Female', 'Age':27,'Employment':'Unemployed','Salary':1500}]

def main():

    database = list([])

    while True:

        print('*** Welcome to PyPivot ***')
        print('A: Load Test Dataset')
        print('B: Add Column')
        print('C: Delete Column')
        print('D: Add Row')
        print('E: Delete Row')
        print('F: View Pivot Table Fields')
        print('G: Add Pivot Table Fields')
        print('H: Delete Pivot Table Fields')
        print('I: View Pivot Table')
        print('J: View Pivot Table with Group Summary')
        print('K: Exit')

        option = input('> ').strip().upper()


        if option == 'A':
            database = default_database
            pf.print_database(database)

        elif option == 'B':

            pf.add_column(database)
            pf.print_database(database)


        elif option == 'C':

            pf.delete_column(database)
            pf.print_database(database)

        elif option == 'D':

            pf.add_row(database)
            pf.print_database(database)


        elif option == 'E':

            pf.delete_row(database)
            pf.print_database(database)

        elif option == 'F':

            pf.view_pivot_table_fields()

        elif option == 'G':

            pf.add_pivot_table_field()

        elif option == 'H':

            pf.delete_pivot_table_field()

        elif option == 'I':

            pf.view_pivot_table(*database)

        elif option == 'J':

            pf.view_pivot_table_with_grouped_summary(*database)

        elif option == 'K':

            break

        else:
            print('Invalid input!Please select the from A-Z!')


    print('Goodbye :)')

if __name__ == '__main__':
    main()




























