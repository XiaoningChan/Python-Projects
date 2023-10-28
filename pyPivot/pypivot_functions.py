
pivot_table_fields = {'Columns':[],'Rows':[],'Values':{}} #{'Columns':[],'Rows':[],'Values':{'Age':'Average','Salary':'Sum','Display':'Row_wise'}}
def add_column(database):
    # Add a new column to the dataset

    while True:


            str = input('Enter the name of the column for adding:').capitalize()

            if len(database) > 0 and str in database[0]:
                print(f'{str} already exist!')
                ans = input('add more column?(y for yes;n for no):')
                if ans == 'n':
                    break
            else:

                if len(database) == 0:
                    value = input('Enter value of column {}:'.format(str)).capitalize()
                    dict = {}
                    dict[str] = value
                    database.append(dict)
                else:
                    for i in range(len(database)):
                        default_value = input(f"Enter the  value for the {str} for row {i + 1}: ").capitalize()
                        database[i][str] = default_value

                ans = input('add more column?(y for yes;n for no):')
                if ans == 'n':
                    break


        #可能需要考虑下row的索引,已考虑

def delete_column(database):
    # Delete an existing column
    while True:

        col_del = input('Enter the name of the column for deleting:').capitalize()
        for dict in database:
            if col_del in dict:
                dict.pop(col_del)
            else:
                print(f"The column '{col_del}' does not exist in the dataset.")
        ans = input('Delete more column?(y for yes;n for no):')
        if ans == 'n':
            break

def add_row(database):
    # Add a new row to the dataset
    while True:
        dict = {}
        if len(database) == 0:
            print('There should be at least one column in the database! Add column first!')
        else:
            for key in database[0].keys():
                value = input('Enter value of column {}:'.format(key)).capitalize()
                dict[key] = value
        database.append(dict)

        break

def delete_row(database):
    # Delete an existing row
    while True:
        a = int(input(f'Enter the index number(1-{len(database)})of the row for deleting:').strip())
        if len(database) < a-1:
            print('the row of index number{} doesn\'t exist!'.format(a))
        else:
            database.pop(a - 1)
        ans = input('Delete more row?(y for yes;n for no):')
        if ans == 'n':
            break
def view_pivot_table_fields():
    # View the list of current pivot table fields
    for field_type,attribute_name in pivot_table_fields.items():
        print('{}:'.format(field_type))
        if field_type == 'Values':
            for key,value in attribute_name.items():
                print('\t{}-{}'.format(key,value))
        else:
            for value in attribute_name:
                print('\t{}'.format(value))
def add_pivot_table_field():
    # Add a pivot table field

    while True:
        try:
            field_type = int(input('Enter field_type(1 for Columns;2 for Rows;3 for Values;4 for Exit ):'))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if field_type == 1:
            while True:
                attribute_name = input('Enter corresponding attribute name(must be lowercase):').capitalize()
                pivot_table_fields['Columns'].append(attribute_name)
                ans = input('add more attribute name for Columns?(y for yes;n for no):')
                if ans == 'n':
                    break
        elif field_type == 2:
            while True:
                attribute_name = input('Enter corresponding attribute name(must be lowercase):').capitalize()
                pivot_table_fields['Rows'].append(attribute_name)
                ans = input('add more attribute name for Rows?(y for yes;n for no):')
                if ans == 'n':
                    break
        elif field_type == 3:
            while True:
                attribute_name = input('Enter corresponding attribute name(must be lowercase):').capitalize()
                ag_funcs = input('Select aggregation function for the attribute name(must be lowercase):').capitalize()
                pivot_table_fields['Values'][attribute_name] = ag_funcs
                ans = input('add more attribute name for Values?(y for yes;n for no):')
                if ans == 'n':
                    if len(pivot_table_fields['Values']) > 1:
                        display = input('Display row_wise or column_wise(r for row_wise;c for column_wise):')
                        if display == 'r':
                            pivot_table_fields['Values']['Display'] = 'Row_wise'
                        else:
                            pivot_table_fields['Values']['Display'] = 'Column_wise'
                    break
        else:
            break
def delete_pivot_table_field():
    # Delete an existing pivot table field
    # {'Columns':[],'Rows':[],'Values':{'Age':'Average','Salary':'Sum','Display':'Row_wise'}}
    while True:
        del_attr = input('Enter attribute_name for deleting(eg.Age,Gender,Salary,Employee):').capitalize()
        notFound = True
        for key,value in pivot_table_fields.items():
            if del_attr in value:
                if type(value) == list:
                    pivot_table_fields[key].remove(del_attr)
                    notFound = False
                else:
                    pivot_table_fields[key].pop(del_attr)
                    notFound = False

        if notFound:
            print('{} does not exist!'.format(del_attr))
        ans = input('Delete more ?(y for yes;n for no):')
        if ans != 'y':
            view_pivot_table()
            break

def view_pivot_table(*database):
    # Generate the pivot table
    #case1.1--{'Columns':['Employment'],'Rows':['Gender'],'Values':{'Salary':'Sum'}}的情况

    if pivot_table_fields == {'Columns':['Employment'],'Rows':['Gender'],'Values':{'Salary':'Sum'}} or \
       pivot_table_fields == {'Columns':['Employment'],'Rows':['Gender'],'Values':{'Age':'Sum'}}:
        key = list(pivot_table_fields['Values'].keys())[0]
        print(f'Sum of {key}\t\tColumn Labels')
        print('Row Labels\t\tEmployee\tself-Employed\tUnemployed\t\tGrand Total')
        print('Female\t\t', end='')
        print('\t{}\t\t\t{}\t\t\t\t{}\t\t\t\t{}'.format(sum('Female', 'Employee', key, *database),
                                                sum('Female', 'Self-Employed', key, *database),
                                                sum('Female', 'Unemployed', key, *database),
                                                subTotal('Gender', 'Female', key, *database)))
        print('Male\t\t', end='')
        print('\t{}\t\t\t{}\t\t\t\t{}\t\t\t\t{}'.format(sum('Male', 'Employee', key, *database),
                                                sum('Male', 'Self-Employed', key, *database),
                                                sum('Male', 'Unemployed', key, *database),
                                                subTotal('Gender', 'Male', key, *database)))
        print('GrandTotal\t\t', end='')
        print('{}\t\t\t{}\t\t\t\t{}\t\t\t\t{}'.format(subTotal('Employment', 'Employee', key, *database),
                                              subTotal('Employment', 'Self-Employed', key, *database),
                                              subTotal('Employment', 'Unemployed', key, *database),
                                              grandTotal(key, *database)))

    # case1.2--{'Columns':['Employment'],'Rows':['Gender'],'Values':{'Salary':'Average'}}的情况
    elif pivot_table_fields == {'Columns':['Employment'],'Rows':['Gender'],'Values':{'Salary':'Average'}} or \
       pivot_table_fields == {'Columns':['Employment'],'Rows':['Gender'],'Values':{'Age':'Average'}}:
        key = list(pivot_table_fields['Values'].keys())[0]
        print(f'Average of {key}\tColumn Labels')
        print('Row Labels\t\t\tEmployee\tself-Employed\tUnemployed\tGrand Total')
        print('Female\t\t\t', end='')
        print('\t{}\t\t{}\t\t\t{}\t\t{}'.format(average('Female', 'Employee', key, *database),
                                                average('Female', 'Self-Employed', key, *database),
                                                average('Female', 'Unemployed', key, *database),
                                                subAverage('Gender', 'Female', key, *database)))
        print('Male\t\t\t', end='')
        print('\t{}\t\t{}\t\t\t{}\t\t{}'.format(average('Male', 'Employee', key, *database),
                                                average('Male', 'Self-Employed', key, *database),
                                                average('Male', 'Unemployed', key, *database),
                                                subAverage('Gender', 'Male', key, *database)))
        print('GrandTotal\t\t\t', end='')
        print('{}\t\t{}\t\t\t{}\t\t{}'.format(subAverage('Employment', 'Employee', key, *database),
                                              subAverage('Employment', 'Self-Employed', key, *database),
                                              subAverage('Employment', 'Unemployed', key, *database),
                                              grandTotal_aver(key, *database)))

    # case1.3--{'Columns':['Employment'],'Rows':['Gender'],'Values':{'Salary':'Count'}}的情况
    elif pivot_table_fields == {'Columns': ['Employment'], 'Rows': ['Gender'], 'Values': {'Salary': 'Count'}} or \
       pivot_table_fields == {'Columns': ['Employment'], 'Rows': ['Gender'], 'Values': {'Age': 'Count'}}:
        key = list(pivot_table_fields['Values'].keys())[0]
        print(f'Count of {key}\tColumn Labels')
        print('Row Labels\t\tEmployee\tself-Employed\tUnemployed\tGrand Total')
        print('Female\t\t', end='')
        print('\t{}\t\t\t{}\t\t\t\t{}\t\t\t{}'.format(count('Female', 'Employee', *database),
                                                      count('Female', 'Self-Employed', *database),
                                                      count('Female', 'Unemployed', *database),
                                                      subCount('Gender', 'Female',*database)))
        print('Male\t\t', end='')
        print('\t{}\t\t\t{}\t\t\t\t{}\t\t\t{}'.format(count('Male', 'Employee', *database),
                                                      count('Male', 'Self-Employed', *database),
                                                      count('Male', 'Unemployed', *database),
                                                      subCount('Gender', 'Male',*database)))
        print('GrandTotal\t\t', end='')
        print('{}\t\t\t{}\t\t\t\t{}\t\t\t{}'.format(subCount('Employment', 'Employee', *database),
                                                    subCount('Employment', 'Self-Employed', *database),
                                                    subCount('Employment', 'Unemployed', *database),
                                                    20))

    # case1.4--{'Columns':['Employment'],'Rows':['Gender'],'Values':{'Salary':'Maximum'}}的情况
    elif pivot_table_fields == {'Columns': ['Employment'], 'Rows': ['Gender'], 'Values': {'Salary': 'Maximum'}} or \
       pivot_table_fields == {'Columns': ['Employment'], 'Rows': ['Gender'], 'Values': {'Age': 'Maximum'}}:
        key = list(pivot_table_fields['Values'].keys())[0]
        print(f'Maximum of {key}\tColumn Labels')
        print('Row Labels\t\t\tEmployee\tself-Employed\tUnemployed\tGrand Total')
        print('Female\t\t\t', end='')
        print('\t{}\t\t{}\t\t\t{}\t\t{}'.format(maximum('Female', 'Employee', key, *database),
                                                maximum('Female', 'Self-Employed', key, *database),
                                                maximum('Female', 'Unemployed', key, *database),
                                                subMax('Gender', 'Female', key, *database)))
        print('Male\t\t\t', end='')
        print('\t{}\t\t{}\t\t\t{}\t\t{}'.format(maximum('Male', 'Employee', key, *database),
                                                maximum('Male', 'Self-Employed', key, *database),
                                                maximum('Male', 'Unemployed', key, *database),
                                                subMax('Gender', 'Male', key, *database)))
        print('GrandTotal\t\t\t', end='')
        print('{}\t\t{}\t\t\t{}\t\t{}'.format(subMax('Employment', 'Employee', key,  *database),
                                              subMax('Employment', 'Self-Employed', key,  *database),
                                              subMax('Employment', 'Unemployed', key,  *database),
                                              grandTotal_max(key, *database)))

    # case1.5--{'Columns':['Employment'],'Rows':['Gender'],'Values':{'Salary':'Minimum'}}的情况
    elif pivot_table_fields == {'Columns': ['Employment'], 'Rows': ['Gender'], 'Values': {'Salary': 'Minimum'}} or \
       pivot_table_fields == {'Columns': ['Employment'], 'Rows': ['Gender'], 'Values': {'Age': 'Minimum'}}:
        key = list(pivot_table_fields['Values'].keys())[0]
        print(f'Minimum of {key}\tColumn Labels')
        print('Row Labels\t\t\tEmployee\tself-Employed\tUnemployed\tGrand Total')
        print('Female\t\t\t', end='')
        print('\t{}\t\t{}\t\t\t{}\t\t{}'.format(minimum('Female', 'Employee', key, *database),
                                                minimum('Female', 'Self-Employed', key, *database),
                                                minimum('Female', 'Unemployed', key, *database),
                                                subMin('Gender', 'Female', key, *database)))
        print('Male\t\t\t', end='')
        print('\t{}\t\t{}\t\t\t{}\t\t{}'.format(minimum('Male', 'Employee', key, *database),
                                                minimum('Male', 'Self-Employed', key, *database),
                                                minimum('Male', 'Unemployed', key, *database),
                                                subMin('Gender', 'Male', key, *database)))
        print('GrandTotal\t\t\t', end='')
        print('{}\t\t{}\t\t\t{}\t\t{}'.format(subMin('Employment', 'Employee', key, *database),
                                              subMin('Employment', 'Self-Employed', key, *database),
                                              subMin('Employment', 'Unemployed', key, *database),
                                              grandTotal_min(key, *database)))

    #case1.6--{'Columns':['Employment'],'Rows':['Gender'],'Values':{'Salary': 'Count','Salary': 'Average','Display':'Column_wise'}}的情况
    elif pivot_table_fields == {'Columns': ['Employment'], 'Rows': ['Gender'], 'Values': {'Salary': 'Average','Age': 'Count','Display':'Column_wise'}} or \
       pivot_table_fields == {'Columns': ['Employment'], 'Rows': ['Gender'], 'Values': {'Age': 'Count','Salary': 'Average','Display':'Column_wise'}}:
        if pivot_table_fields['Values']['Salary'] == 'Average':
            key = 'Salary'
        else:
            key = 'Age'

        print('\t\t\tColumn Labels')
        print(f'\t\t\tEmployee\t\t\t\t\t\tself-Employed\t\t\t\t\t\t\tUnemployed\t\t\t\t\t\t\tTotal Count of S/N\tTotal Average of {key}')
        print(f'Row Labels\tCount of S/N\tAverage of {key}\tCount of S/N\tAverage of {key}\tCount of S/N\tAverage of {key}')
        for gender in ['Female','Male']:
            print('{:12}{:12}{:13}{:14}{:30}{:13}{:13}{:17}{:27}'.format(gender,
                                                                        count(gender, 'Employee', *database),
                                                                        average(gender, 'Employee', key, *database),
                                                                        count(gender, 'Self-Employed',*database),
                                                                        average(gender, 'Self-Employed', key, *database),
                                                                        count(gender, 'Unemployed', *database),
                                                                        average(gender, 'Unemployed', key, *database),
                                                                        subCount('Gender', gender, *database),
                                                                        subAverage('Gender', gender, key, *database)))
        print('{:12}{:12}{:13}{:14}{:30}{:13}{:13}{:17}{:27}'.format('GrandTotal',
                                                                        subCount('Employment', 'Employee', *database),
                                                                        subAverage('Employment', 'Employee', key, *database),
                                                                        subCount('Employment', 'Self-Employed', *database),
                                                                        subAverage('Employment', 'Self-Employed', key, *database),
                                                                        subCount('Employment', 'Unemployed', *database),
                                                                        subAverage('Employment', 'Unemployed', key, *database),
                                                                        20,
                                                                        grandTotal_aver(key, *database),))

    # case1.7--{'Columns':['Employment'],'Rows':['Gender'],'Values':{'Salary': 'Count','Salary': 'Average','Display':'Row_wise'}}的情况
    elif pivot_table_fields == {'Columns': ['Employment'], 'Rows': ['Gender'],'Values': {'Salary': 'Average','Age': 'Count', 'Display': 'Row_wise'}} or \
            pivot_table_fields == {'Columns': ['Employment'], 'Rows': ['Gender'],'Values': {'Age': 'Count','Salary': 'Average', 'Display': 'Row_wise'}}:
        if pivot_table_fields['Values']['Salary'] == 'Average':
            key = 'Salary'
        else:
            key = 'Age'
        print('\t\t\t\t\t\tColumn Labels')
        print('Row Labels\t\t\t\tEmployee\tself-Employed\tUnemployed\t\tGrand Total')
        for gender in ['Female','Male']:

            print('{:25}\n{:13}\t{:13}\t{:13}\t{:13}\t{:13}\n{:13}\t{:13}\t{:13}\t{:13}\t{:13}'.format(gender,
                                                                                                    'Count of S/N',
                                                                                                    count(gender, 'Employee', *database),
                                                                                                    count(gender, 'Self-Employed', *database),
                                                                                                    count(gender, 'Unemployed', *database),
                                                                                                    subCount('Gender', gender, *database),
                                                                                                    'Average of Salary',
                                                                                                    average(gender, 'Employee', key, *database),
                                                                                                    average(gender, 'Self-Employed', key, *database),
                                                                                                    average(gender, 'Unemployed', key, *database),
                                                                                                    subAverage('Gender', gender, key, *database)))
            is_first_line = False

        print('{:25}{:5}{:15}{:16}{:16}'.format('Total Count of S/N',
                                                        subCount('Employment', 'Employee', *database),
                                                        subCount('Employment', 'Self-Employed', *database),
                                                        subCount('Employment', 'Unemployed', *database),
                                                        20,))


        print('{:25}{:8}{:16}{:16}{:16}'.format('Total Average of Salary',
                                                        subAverage('Employment', 'Employee', key, *database),
                                                        subAverage('Employment', 'Self-Employed', key, *database),
                                                        subAverage('Employment', 'Unemployed', key, *database),
                                                        grandTotal_aver('Salary', *database), ))

    # case2.1(行列对调)--{'Columns':['Gender'],'Rows':['Employment'],'Values':{'Salary': 'Sum'}} or {'Columns':['Gender'],'Rows':['Employment'],'Values':{'Age': 'Sum'}}的情况
    elif pivot_table_fields == {'Columns':['Gender'],'Rows':['Employment'],'Values':{'Salary':'Sum'}} or \
       pivot_table_fields == {'Columns':['Gender'],'Rows':['Employment'],'Values':{'Age':'Sum'}}:
        key = list(pivot_table_fields['Values'].keys())[0]
        print(f'Sum of {key}\t\t\tColumn Labels')
        print('Row Labels\t\t\tFemale\t\tMale\tGrand Total')
        for employment in ['Employee','Self-Employed','Unemployed']:
            print('{:15}{:11}{:10}{:13}'.format(employment,
                                                    sum('Female', employment, key, *database),
                                                    sum('Male', employment, key, *database),
                                                    subTotal('Employment', employment, key, *database)))
        print('{:15}{:11}{:10}{:13}'.format('GrandToatal',
                                            subTotal('Gender', 'Female', key, *database),
                                            subTotal('Gender', 'Male', key, *database),
                                            grandTotal(key, *database)))

    #case2.2(行列对调)--{'Columns':['Gender'],'Rows':['Employment'],'Values':{'Salary': 'Average'}} or {'Columns':['Gender'],'Rows':['Employment'],'Values':{'Age': 'Average'}}的情况
    elif pivot_table_fields == {'Columns':['Gender'],'Rows':['Employment'],'Values':{'Salary':'Average'}} or \
       pivot_table_fields == {'Columns':['Gender'],'Rows':['Employment'],'Values':{'Age':'Average'}}:
        key = list(pivot_table_fields['Values'].keys())[0]
        key = 'Age'
        print(f'Average of {key}\t\tColumn Labels')
        print('Row Labels\t\t\tFemale\t\tMale\tGrand Total')
        for employment in ['Employee','Self-Employed','Unemployed']:
            print('{:15}{:11}{:10}{:13}'.format(employment,
                                                average('Female', employment, key, *database),
                                                average('Male', employment, key, *database),
                                                subAverage('Employment', employment, key, *database)))
        print('{:15}{:11}{:10}{:13}'.format('GrandToatal',
                                            subAverage('Gender', 'Female', key, *database),
                                            subAverage('Gender', 'Female', key, *database),
                                            grandTotal_aver(key, *database)))

    # case2.3(行列对调)--{'Columns':['Gender'],'Rows':['Employment'],'Values':{'Salary': 'Count'}} or {'Columns':['Gender'],'Rows':['Employment'],'Values':{'Age': 'Count'}}的情况
    elif pivot_table_fields == {'Columns': ['Gender'], 'Rows': ['Employment'], 'Values': {'Salary': 'Count'}} or \
            pivot_table_fields == {'Columns': ['Gender'], 'Rows': ['Employment'], 'Values': {'Age': 'Count'}}:
        key = list(pivot_table_fields['Values'].keys())[0]
        key = 'Age'
        print(f'Count of {key}\t\tColumn Labels')
        print('Row Labels\t\t\tFemale\t\tMale\tGrand Total')
        for employment in ['Employee', 'Self-Employed', 'Unemployed']:
            print('{:15}{:11}{:10}{:13}'.format(employment,
                                                count('Female', employment, *database),
                                                count('Male', employment, *database),
                                                subCount('Employment', employment, *database)))
        print('{:15}{:11}{:10}{:13}'.format('GrandToatal',
                                            subCount('Gender', 'Female', *database),
                                            subCount('Gender', 'Male', *database),
                                            20))
    # case2.3(行列对调)--{'Columns':['Gender'],'Rows':['Employment'],'Values':{'Salary': 'Maximum'}} or {'Columns':['Gender'],'Rows':['Employment'],'Values':{'Age': 'Maximum'}}的情况
    elif pivot_table_fields == {'Columns': ['Gender'], 'Rows': ['Employment'], 'Values': {'Salary': 'Maximum'}} or \
            pivot_table_fields == {'Columns': ['Gender'], 'Rows': ['Employment'], 'Values': {'Age': 'Maximum'}}:
        key = list(pivot_table_fields['Values'].keys())[0]
        print(f'Maximum of {key}\t\tColumn Labels')
        print('Row Labels\t\t\tFemale\t\tMale\tGrand Total')
        for employment in ['Employee', 'Self-Employed', 'Unemployed']:
            print('{:15}{:11}{:10}{:13}'.format(employment,
                                                maximum('Female', employment, key, *database),
                                                maximum('Male', employment, key, *database),
                                                subMax('Employment', employment, key, *database)))
        print('{:15}{:11}{:10}{:13}'.format('GrandToatal',
                                            subMax('Employment', employment, key, *database),
                                            subMax('Employment', employment, key, *database),
                                            subMax('Employment', employment, key, *database),
                                            grandTotal_max(key, *database)))

    #case2.3(行列对调)--{'Columns':['Gender'],'Rows':['Employment'],'Values':{'Salary': 'Minimum'}} or {'Columns':['Gender'],'Rows':['Employment'],'Values':{'Age': 'Minimum'}}的情况
    elif pivot_table_fields == {'Columns': ['Gender'], 'Rows': ['Employment'], 'Values': {'Salary': 'Minimum'}} or \
            pivot_table_fields == {'Columns': ['Gender'], 'Rows': ['Employment'], 'Values': {'Age': 'Minimum'}}:
        key = list(pivot_table_fields['Values'].keys())[0]
        print(f'Minimum of {key}\t\tColumn Labels')
        print('Row Labels\t\t\tFemale\t\tMale\tGrand Total')
        for employment in ['Employee', 'Self-Employed', 'Unemployed']:
            print('{:15}{:11}{:10}{:13}'.format(employment,
                                                minimum('Female', employment, key, *database),
                                                minimum('Male', employment, key, *database),
                                                subMin('Employment', employment, key, *database)))
        print('{:15}{:11}{:10}{:13}'.format('GrandToatal',
                                            subMin('Employment', employment, key, *database),
                                            subMin('Employment', employment, key, *database),
                                            grandTotal_min(key, *database)))
    else:
        print('There may be input typos or the pivot table is beyond implementation!')
        print('Please try another combination of pivot table fields!')


def view_pivot_table_with_grouped_summary(*database):
    # Generate pivot table with grouped summary

    genders = list([])

    for person in database:
        genders.append(person['Gender'])

    genders = set(genders)
    genders = list(genders)
    genders.sort()

    crosstab = dict({})
    crosstab1 = dict({})

    for gender in genders:

        ages = list([])
        salarys = list([])

        for person in database:

            if person['Gender'] == gender:
                ages.append(person['Age'])
            if person['Gender'] == gender:
                salarys.append(person['Salary'])

        ages = set(ages)
        ages = list(ages)
        ages.sort()
        salarys = set(salarys)
        salarys = list(salarys)
        salarys.sort()

        crosstab[gender] = dict({})  # crosstab{Female:{age:count,age:count,..},Male:{age:count,age:count,..}}
        crosstab1[gender] = dict({})

        for age in ages:
            count_age = 0
            for person in database:
                if person['Gender'] == gender and person['Age'] == age:
                    count_age += 1
            crosstab[gender][age] = count_age

        for salary in salarys:
            count_salary = 0
            for person in database:
                if person['Gender'] == gender and person['Salary'] == salary:
                    count_salary += 1
            crosstab1[gender][salary] = count_salary
    # case2.1--{'Columns':['Employment'],'Rows':['Gender','Age'],'Values':{'Salary':'Sum'}}的情况
    if pivot_table_fields == {'Columns': ['Employment'], 'Rows': ['Gender','Age'], 'Values': {'Salary': 'Sum'}} or \
            pivot_table_fields == {'Columns': ['Employment'], 'Rows': ['Age','Gender'], 'Values': {'Salary': 'Sum'}}:
        print('Sum of Salary\tColumn Labels')
        print('Row Labels\t\tEmployee\t\tself-Employed\tUnemployed\t\tGrand Total')

        for gender, age_count in crosstab.items():
            print('{:4}\t{:14}\t{:13}\t{:13}\t{:13}'.format(gender, sum(gender, 'Employee', 'Salary', *database),
                                                                sum(gender, 'Self-Employed', 'Salary', *database),
                                                                sum(gender, 'Unemployed','Salary', *database),
                                                                subTotal('Gender', gender,'Salary', *database)))

            for age, count_age in age_count.items():
                print('{:4}\t{:14}\t{:13}\t{:13}\t{:13}'.format(age,groupSum(gender, 'Employee', 'Age', age,'Salary', *database),
                                                                    groupSum(gender, 'Self-Employed', 'Age', age,'Salary', *database),
                                                                    groupSum(gender, 'Unemployed', 'Age', age,'Salary', *database),
                                                                    groupSubTotal('Gender', gender, 'Age', age,'Salary', *database)))

        print('{:13}\t{:4}\t{:13}\t{:13}\t{:13}'.format('GrandTotal', subTotal('Employment', 'Employee','Salary', *database),
                                                            subTotal('Employment', 'Self-Employed','Salary', *database),
                                                            subTotal('Employment', 'Unemployed','Salary', *database),
                                                            grandTotal('Salary', *database)))

    # case2.2--{'Columns':['Employment'],'Rows':['Gender','Age'],'Values':{'Salary':'Average'}}的情况
    elif pivot_table_fields == {'Columns': ['Employment'], 'Rows': ['Gender','Age'], 'Values': {'Salary': 'Average'}} or \
            pivot_table_fields == {'Columns': ['Employment'], 'Rows': ['Age','Gender'], 'Values': {'Salary': 'Average'}}:

        print('Average of Salary\tColumn Labels')
        print('Row Labels\t\tEmployee\t\tself-Employed\tUnemployed\t\tGrand Total')

        for gender, age_count in crosstab.items():
            print('{:4}\t{:13}\t{:13}\t{:13}\t{:13}'.format(gender, average(gender, 'Employee', 'Salary', *database),
                                                            average(gender, 'Self-Employed', 'Salary', *database),
                                                            average(gender, 'Unemployed', 'Salary', *database),
                                                            subAverage('Gender', gender, 'Salary', *database)))

            for age, count_age in age_count.items():
                print('{:4}\t{:13}\t{:13}\t{:13}\t{:13}'.format(age, groupAverage(gender, 'Employee', 'Age', age, 'Salary', *database),
                                                                groupAverage(gender, 'Self-Employed', 'Age', age, 'Salary', *database),
                                                                groupAverage(gender, 'Unemployed', 'Age', age, 'Salary', *database),
                                                                groupSubAverage('Gender', gender, 'Age', age, 'Salary', *database)))

        print('{:13}\t{:4}\t{:13}\t{:13}\t{:13}'.format('GrandTotal', subAverage('Employment', 'Employee', 'Salary', *database),
                                                  subAverage('Employment', 'Self-Employed', 'Salary', *database),
                                                  subAverage('Employment', 'Unemployed', 'Salary', *database),
                                                  grandTotal_aver('Salary', *database)))

    # case2.3--{'Columns':['Employment'],'Rows':['Gender','Age'],'Values':{'Salary':'Count'}}的情况
    elif pivot_table_fields == {'Columns': ['Employment'], 'Rows': ['Gender','Age'], 'Values': {'Salary': 'Count'}} or \
            pivot_table_fields == {'Columns': ['Employment'], 'Rows': ['Age','Gender'], 'Values': {'Salary': 'Count'}}:

        print('Count of Salary\tColumn Labels')
        print('Row Labels\t\tEmployee\t\tself-Employed\tUnemployed\t\tGrand Total')

        for gender, age_count in crosstab.items():

            print('{:4}\t{:13}\t{:13}\t{:13}\t{:13}'.format(gender, count('Female', 'Employee', *database),
                                                            count('Female', 'Self-Employed', *database),
                                                            count('Female', 'Unemployed', *database),
                                                            subCount('Gender', 'Female',*database)))

            for age, count_age in age_count.items():
                print('{:4}\t{:13}\t{:13}\t{:13}\t{:13}'.format(age, groupCount(gender, 'Employee', 'Age', age, *database),
                                                                groupCount(gender, 'Self-Employed', 'Age', age, *database),
                                                                groupCount(gender, 'Unemployed','Age', age, *database),
                                                                GroupSubCount('Gender', gender,'Age', age, *database)))

        print('{:13}\t{:4}\t{:13}\t{:13}\t{:13}'.format('GrandTotal', subCount('Employment', 'Employee', *database),
                                                        subCount('Employment', 'Self-Employed', *database),
                                                        subCount('Employment', 'Unemployed', *database),
                                                        20))

    # case2.4--{'Columns':['Employment'],'Rows':['Gender','Age'],'Values':{'Salary':'Maximum'}}的情况
    elif pivot_table_fields == {'Columns': ['Employment'], 'Rows': ['Gender','Age'], 'Values': {'Salary': 'Maximum'}} or \
            pivot_table_fields == {'Columns': ['Employment'], 'Rows': ['Age','Gender'], 'Values': {'Salary': 'Maximum'}}:

        print('Maximum of Salary\tColumn Labels')
        print('Row Labels\t\tEmployee\t\tself-Employed\tUnemployed\t\tGrand Total')

        for gender, age_count in crosstab.items():
            print('{:4}\t{:13}\t{:13}\t{:13}\t{:13}'.format(gender, maximum('Female', 'Employee', 'Salary', *database),
                                                            maximum('Female', 'Self-Employed', 'Salary', *database),
                                                            maximum('Female', 'Unemployed', 'Salary', *database),
                                                            subMax('Gender', 'Female', 'Salary', *database)))

            for age, count_age in age_count.items():
                print('{:4}\t{:13}\t{:13}\t{:13}\t{:13}'.format(age, groupMax(gender, 'Employee', 'Age', age, 'Salary', *database),
                                                                groupMax(gender, 'Self-Employed', 'Age', age, 'Salary', *database),
                                                                groupMax(gender, 'Unemployed', 'Age', age, 'Salary', *database),
                                                                groupSubMax('Gender', gender, 'Age', age, 'Salary', *database)))
        print('{:13}\t{:4}\t{:13}\t{:13}\t{:13}'.format('GrandTotal', subMax('Employment', 'Employee', 'Salary',  *database),
                                                        subMax('Employment', 'Self-Employed', 'Salary',  *database),
                                                        subMax('Employment', 'Unemployed', 'Salary',  *database),
                                                        grandTotal_max('Salary', *database)))

    # case2.5--{'Columns':['Employment'],'Rows':['Gender','Age'],'Values':{'Salary':'Minimum'}}的情况
    elif pivot_table_fields == {'Columns': ['Employment'], 'Rows': ['Gender','Age'], 'Values': {'Salary': 'Minimum'}} or \
            pivot_table_fields == {'Columns': ['Employment'], 'Rows': ['Age','Gender'], 'Values': {'Salary': 'Minimum'}}:

        print('Minimum of Salary\tColumn Labels')
        print('Row Labels\t\tEmployee\t\tself-Employed\tUnemployed\t\tGrand Total')

        for gender, age_count in crosstab.items():
            print('{:4}\t{:13}\t{:13}\t{:13}\t{:13}'.format(gender, minimum('Female', 'Employee', 'Salary', *database),
                                                            minimum('Female', 'Self-Employed', 'Salary', *database),
                                                            minimum('Female', 'Unemployed', 'Salary', *database),
                                                            subMin('Gender', 'Female', 'Salary', *database)))

            for age, count_age in age_count.items():
                print('{:4}\t{:13}\t{:13}\t{:13}\t{:13}'.format(age, groupMin(gender, 'Employee', 'Age', age, 'Salary', *database),
                                                                groupMin(gender, 'Self-Employed',  'Age', age, 'Salary', *database),
                                                                groupMin(gender, 'Unemployed',  'Age', age, 'Salary', *database),
                                                                groupSubMin('Gender',gender, 'Age', age, 'Salary', *database)))

        print('{:13}\t{:4}\t{:13}\t{:13}\t{:13}'.format('GrandTotal', subMin('Employment', 'Employee', 'Salary', *database),
                                                         subMin('Employment', 'Self-Employed', 'Salary', *database),
                                                         subMin('Employment', 'Unemployed', 'Salary', *database),
                                                         grandTotal_min('Salary', *database)))

    # case2.6--{'Columns':['Employment'],'Rows':['Gender','Salary'],'Values':{'Age':'Sum'}}的情况
    elif pivot_table_fields == {'Columns':['Employment'],'Rows':['Gender','Salary'],'Values':{'Age':'Sum'}} or pivot_table_fields == {'Columns':['Employment'],'Rows':['Salary','Gender'],'Values':{'Age':'Sum'}}:
        print('Sum of Age\tColumn Labels')
        print('Row Labels\t\tEmployee\t\tself-Employed\tUnemployed\t\tGrand Total')

        for gender, salary_count in crosstab1.items():
            print('{:4}\t{:13}\t{:13}\t{:13}\t{:13}'.format(gender, sum(gender, 'Employee', 'Age', *database),
                                                            sum(gender, 'Self-Employed', 'Age', *database),
                                                            sum(gender, 'Unemployed', 'Age', *database),
                                                            subTotal('Gender', gender, 'Age', *database)))

            for salary, count_salary in salary_count.items():
                print('{:4}\t{:13}\t{:13}\t{:13}\t{:13}'.format(salary, groupSum(gender, 'Employee', 'Salary',salary, 'Age', *database),
                                                                groupSum(gender, 'Self-Employed', 'Salary',salary, 'Age', *database),
                                                                groupSum(gender, 'Unemployed','Salary',salary, 'Age', *database),
                                                                groupSubTotal('Gender', gender, 'Salary', salary, 'Age', *database)))

        print('{:13}\t{:4}\t{:13}\t{:13}\t{:13}'.format('GrandTotal', subTotal('Employment', 'Employee', 'Age', *database),
                                                      subTotal('Employment', 'Self-Employed', 'Age', *database),
                                                      subTotal('Employment', 'Unemployed', 'Age', *database),
                                                      grandTotal('Age', *database)))

    # case2.7--{'Columns':['Employment'],'Rows':['Gender','Salary'],'Values':{'Age':'Average'}}的情况
    elif pivot_table_fields == {'Columns':['Employment'],'Rows':['Gender','Salary'],'Values':{'Age':'Average'}} or \
            pivot_table_fields == {'Columns':['Employment'],'Rows':['Salary','Gender'],'Values':{'Age':'Average'}}:
        print('Average of Age\tColumn Labels')
        print('Row Labels\t\tEmployee\t\tself-Employed\tUnemployed\t\tGrand Total')

        for gender, salary_count in crosstab1.items():
            print('{:4}\t{:13}\t{:13}\t{:13}\t{:13}'.format(gender, average('Female', 'Employee', 'Age', *database),
                                                            average('Female', 'Self-Employed', 'Age', *database),
                                                            average('Female', 'Unemployed', 'Age', *database),
                                                            subAverage('Gender', 'Female', 'Age', *database)))

            for salary, count_salary in salary_count.items():
                print('{:4}\t{:13}\t{:13}\t{:13}\t{:13}'.format(salary,
                                                                groupAverage(gender, 'Employee', 'Salary', salary, 'Age',  *database),
                                                                groupAverage(gender, 'Self-Employed', 'Salary', salary,'Age',  *database),
                                                                groupAverage(gender, 'Unemployed', 'Salary', salary, 'Age',  *database),
                                                                groupSubAverage('Gender', gender, 'Salary', salary, 'Age', *database)))

        print('{:13}\t{:4}\t{:13}\t{:13}\t{:13}'.format('GrandTotal',
                                                        subAverage('Employment', 'Employee', 'Age', *database),
                                                        subAverage('Employment', 'Self-Employed', 'Age', *database),
                                                        subAverage('Employment', 'Unemployed', 'Age', *database),
                                                        grandTotal_aver('Age', *database)))

    # case2.8--{'Columns':['Employment'],'Rows':['Gender','Salary'],'Values':{'Age':'Count'}}的情况
    elif pivot_table_fields == {'Columns':['Employment'],'Rows':['Gender','Salary'],'Values':{'Age':'Count'}} or \
            pivot_table_fields == {'Columns':['Employment'],'Rows':['Salary','Gender'],'Values':{'Age':'Count'}}:
        print('Count of Age\tColumn Labels')
        print('Row Labels\t\tEmployee\t\tself-Employed\tUnemployed\t\tGrand Total')

        for gender, salary_count in crosstab1.items():

            print('{:4}\t{:13}\t{:13}\t{:13}\t{:13}'.format(gender, count('Female', 'Employee', *database),
                                                            count('Female', 'Self-Employed', *database),
                                                            count('Female', 'Unemployed', *database),
                                                            subCount('Gender', 'Female', *database)))

            for salary, count_salary in salary_count.items():
                print('{:4}\t{:13}\t{:13}\t{:13}\t{:13}'.format(salary, groupCount(gender, 'Employee', 'Salary', salary, *database),
                                                                groupCount(gender, 'Self-Employed', 'Salary', salary, *database),
                                                                groupCount(gender, 'Unemployed', 'Salary', salary, *database),
                                                                GroupSubCount('Gender', gender, 'Salary', salary, *database)))

        print('{:13}\t{:4}\t{:13}\t{:13}\t{:13}'.format('GrandTotal', subCount('Employment', 'Employee', *database),
                                                        subCount('Employment', 'Self-Employed', *database),
                                                        subCount('Employment', 'Unemployed', *database),
                                                        20))

    # case2.9--{'Columns':['Employment'],'Rows':['Gender','Salary'],'Values':{'Age':'Maximum'}}的情况
    elif pivot_table_fields == {'Columns': ['Employment'], 'Rows': ['Gender','Salary'], 'Values': {'Age': 'Maximum'}} or \
            pivot_table_fields == {'Columns': ['Employment'], 'Rows': ['Salary','Gender'], 'Values': {'Age': 'Maximum'}}:

        print('Maximum of Age\tColumn Labels')
        print('Row Labels\t\tEmployee\t\tself-Employed\tUnemployed\t\tGrand Total')

        for gender, salary_count in crosstab1.items():
            print('{:4}\t{:13}\t{:13}\t{:13}\t{:13}'.format(gender, maximum('Female', 'Employee', 'Age', *database),
                                                            maximum('Female', 'Self-Employed', 'Age', *database),
                                                            maximum('Female', 'Unemployed', 'Age', *database),
                                                            subMax('Gender', 'Female', 'Age', *database)))

            for salary, count_salary in salary_count.items():
                print('{:4}\t{:13}\t{:13}\t{:13}\t{:13}'.format(salary, groupMax(gender, 'Employee', 'Salary', salary, 'Age', *database),
                                                                groupMax(gender, 'Self-Employed', 'Salary', salary, 'Age', *database),
                                                                groupMax(gender, 'Unemployed', 'Salary', salary, 'Age', *database),
                                                                groupSubMax('Gender', gender, 'Salary', salary, 'Age', *database)))
        print('{:13}\t{:4}\t{:13}\t{:13}\t{:13}'.format('GrandTotal', subMax('Employment', 'Employee', 'Age', *database),
                                                        subMax('Employment', 'Self-Employed', 'Age', *database),
                                                        subMax('Employment', 'Unemployed', 'Age', *database),
                                                        grandTotal_max('Age', *database)))

    # case2.10--{'Columns':['Employment'],'Rows':['Gender','Salary'],'Values':{'Age':'Minimum'}}的情况
    elif pivot_table_fields == {'Columns': ['Employment'], 'Rows': ['Gender','Salary'], 'Values': {'Age': 'Minimum'}} or \
            pivot_table_fields == {'Columns': ['Employment'], 'Rows': ['Salary','Gender'], 'Values': {'Age': 'Minimum'}}:

        print('Minimum of Age\tColumn Labels')
        print('Row Labels\t\tEmployee\t\tself-Employed\tUnemployed\t\tGrand Total')

        for gender, salary_count in crosstab1.items():
            print('{:4}\t{:13}\t{:13}\t{:13}\t{:13}'.format(gender, minimum('Female', 'Employee', 'Age', *database),
                                                            minimum('Female', 'Self-Employed', 'Age', *database),
                                                            minimum('Female', 'Unemployed', 'Age', *database),
                                                            subMin('Gender', 'Female', 'Age', *database)))

            for salary, count_salary in salary_count.items():
                print('{:4}\t{:13}\t{:13}\t{:13}\t{:13}'.format(salary, groupMin(gender, 'Employee', 'Salary', salary, 'Age', *database),
                                                                groupMin(gender, 'Self-Employed', 'Salary', salary, 'Age', *database),
                                                                groupMin(gender, 'Unemployed', 'Salary', salary, 'Age', *database),
                                                                groupSubMin('Gender', gender,  'Salary', salary, 'Age', *database)))

        print('{:13}\t{:4}\t{:13}\t{:13}\t{:13}'.format('GrandTotal', subMin('Employment', 'Employee', 'Age', *database),
                                                        subMin('Employment', 'Self-Employed', 'Age', *database),
                                                        subMin('Employment', 'Unemployed', 'Age', *database),
                                                        grandTotal_min('Age', *database)))
    else:
        print('There may be input typos or the pivot table is beyond implementation!')
        print('Please try another combination of pivot table fields!')

def sum(gender,employment,salary, *database):
    sum = 0
    for person in database:
        if person['Gender'] == gender and person['Employment'] == employment:
            sum += person[salary]
    return sum

def groupSum(gender, employment, Age, age, salary, *database):
    sum = 0
    for person in database:
        if person['Gender'] == gender and person['Employment'] == employment and person[Age] == age:
            sum += person[salary]
    if sum == 0:
        return ''
    return sum

def groupSubTotal(a, b, c, d, e,  *database):

    sum = 0
    for person in database:
        if person[a] == b and person[c] == d:
            sum += person[e]
    return sum
def subTotal(x, y, z, *database):

    sum = 0
    for person in database:
        if person[x] == y:
            sum += person[z]
    return sum

def grandTotal(y,*database):
    sum= 0
    for person in database:
        sum += person[y]
    return sum

def average(x, y, z, *database):
    sum = 0
    count = 0
    for person in database:
        if person['Gender'] == x and person['Employment'] == y:
            sum += person[z]
            count += 1
    rounded_result = round(sum / count,1)
    return rounded_result

def groupAverage(x, y, z, a, b, *database):
    sum = 0
    count = 0
    for person in database:
        if person['Gender'] == x and person['Employment'] == y and person[z] == a:
            sum += person[b]
            count += 1
    if  count == 0:
        return ''
    else:
        rounded_result = round(sum / count, 1)
        return rounded_result
def subAverage(x, y, z, *database):
    sum = 0
    count = 0
    for person in database:
        if person[x] == y :
            sum += person[z]
            count += 1
    rounded_result = round(sum / count, 1)
    return rounded_result

def groupSubAverage(x, y, z, a, b, *database):
    sum = 0
    count = 0
    for person in database:
        if person[x] == y and person[z] == a:
            sum += person[b]
            count += 1
    if count == 0:
        return ''
    else:
        rounded_result = round(sum / count, 1)
        return rounded_result
def grandTotal_aver(y, *database):
    sum= 0
    count = 0
    for person in database:
        sum += person[y]
        count += 1
    rounded_result = round(sum / count, 1)
    return rounded_result

def count(gender, employment, *database):
    count = 0
    for person in database:
        if person['Gender'] == gender and person['Employment'] == employment:
            count += 1
    if count == 0:
        return ''
    else:
        return count

def groupCount(x, y, z, a, *database):
    count = 0
    for person in database:
        if person['Gender'] == x and person['Employment'] == y and person[z] == a:
            count += 1
    if count == 0:
        return ''
    else:
        return count

def subCount(x, y, *database):
    count = 0
    for person in database:
        if person[x] == y :
            count += 1
    return count

def GroupSubCount(x, y, z, a, *database):
    count = 0
    for person in database:
        if person[x] == y and person[z] == a:
            count += 1
    return count

def maximum(x, y, z, *database):
    max = 0
    for person in database:
        if person['Gender'] == x and person['Employment'] == y:
            if person[z] > max:
                max = person[z]
    return max

def groupMax(x, y, z, a, b, *database):
    max = 0
    for person in database:
        if person['Gender'] == x and person['Employment'] == y and person[z] == a:
            if person[b] > max:
                max = person[b]
    if max == 0:
        return ''
    else:
        return max

def subMax(x, y, z, *database):
    subMax = 0
    for person in database:
        if person[x] == y:
            if person[z] > subMax:
                subMax = person[z]
    return subMax

def groupSubMax(x, y, z, a, b, *database):
    subMax = 0
    for person in database:
        if person[x] == y and person[z] == a:
            if person[b] > subMax:
                subMax = person[b]
    if subMax == 0:
        return ''
    else:
        return subMax

def grandTotal_max(x, *database):
    gMax = 0
    for person in database:
        if person[x] > gMax:
            gMax = person[x]
    return gMax

def minimum(x, y, z, *database):
    min = 100000
    for person in database:
        if person['Gender'] == x and person['Employment'] == y:
            if person[z] < min:
                min = person[z]
    return min

def groupMin(x, y, z, a, b, *database):
    min = 100000
    for person in database:
        if person['Gender'] == x and person['Employment'] == y and person[z] == a:
            if person[b] < min:
                min = person[b]
    if min == 100000:
        return ''
    else:
        return min

def subMin(x, y, z, *database):
    subMin = 100000
    for person in database:
        if person[x] == y:
            if person[z] < subMin:
                subMin = person[z]
    return subMin

def groupSubMin(x, y, z, a, b, *database):
    subMin = 100000
    for person in database:
        if person[x] == y and person[z] == a:
            if person[b] < subMin:
                subMin = person[b]
    if subMin == 100000:
        return ''
    else:
        return subMin

def grandTotal_min(x, *database):
    gMin = 100000
    for person in database:
        if person[x] < gMin:
            gMin = person[x]
    return gMin

def print_database(database):
    for person in database:
        print(person)






