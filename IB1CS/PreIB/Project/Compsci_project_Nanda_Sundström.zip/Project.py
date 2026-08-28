date=input(str("Which date's moon phase would you like to know in 2026? (eg.27/01): "))
wxg=('01/01', '02/01', '27/01', '28/01', '29/01', '30/01', '31/01', '25/02', '26/02', '27/02', '28/02', '01/03', '02/03', '26/03', '27/03', '28/03', '29/03', '30/03', '31/03', '01/04', '25/04', '26/04', '27/04', '28/04', '29/04', '30/04', '24/05', '25/05', '26/05', '27/05', '28/05', '29/05', '30/05', '22/06', '23/06', '25/06', '25/06', '26/06', '27/06', '28/06', '29/06', '22/07', '23/07', '24/07', '25/07', '26/07', '27/07', '28/07', '21/08', '22/08', '23/08', '24/08', '25/08', '26/08', '27/08', '19/09', '20/09', '21/09', '22/09', '23/09', '24/09', '25/09', '19/10', '20/10', '21/10', '22/10', '23/10', '24/10', '25/10', '18/11', '19/11', '20/11', '21/11', '22/11', '23/11', '18/12', '19/12', '20/12', '21/12', '22/12', '23/12') #wxg for Waxing Gibbous
wng=('04/01', '05/01', '06/01', '07/01', '08/01', '09/01', '02/02', '03/02', '04/02', '05/02', '06/02', '07/02', '08/02', '04/03', '05/03', '06/03', '07/03', '08/03', '09/03', '10/03', '03/04', '04/04', '05/04', '06/04', '07/04', '08/04', '09/04', '02/05', '03/05', '04/05', '05/05', '06/05', '07/05', '08/05', '01/06', '02/06', '03/06', '04/06', '05/06', '06/06', '07/06', '01/07', '02/07', '03/07', '04/07', '05/07', '06/07', '30/07', '31/07', '01/08', '02/08', '03/08', '04/08', '05/08', '29/08', '30/08', '31/08', '01/09', '02/09', '03/09', '27/09', '28/09', '29/09', '30/09', '01/10', '02/10', '27/10', '28/10', '29/10', '30/10', '31/10', '25/11', '26/11', '27/11', '28/11', '29/11', '30/11', '25/12', '26/12', '27/12', '28/12', '29/12') #wng for Waning Gibbous
third=('10/01', '09/02', '11/03', '10/04', '09/05', '08/06', '07/07', '06/08', '04/09', '03/10', '01/11', '01/12', '30/12') #third for third quarter
wnc=('11/01', '12/01', '13/01', '14/01', '15/01', '16/01', '17/01', '10/02', '11/02', '12/02', '13/02', '14/02', '15/02', '12/03', '13/03', '14/03', '15/03', '16/03', '17/03', '18/03', '11/04', '12/04', '13/04', '14/04', '15/04', '16/04', '10/05', '11/05', '12/05', '13/05', '14/05', '15/05', '09/06', '10/06', '11/06', '12/06', '13/06', '14/06', '08/07', '09/07', '10/07', '11/07', '12/07', '13/07', '07/08', '08/08', '09/08', '10/08', '11/08', '05/09', '06/09', '07/09', '08/09', '09/09', '10/09', '04/10', '05/10', '06/10', '07/10', '08/10', '09/10', '02/11', '03/11', '04/11', '05/11', '06/11', '07/11', '08/11', '02/12', '03/12', '04/12', '05/12', '06/12', '07/12', '08/12', '31/12') #wnc for Waning Crescent
wxc=('19/01', '20/01', '21/01', '22/01', '23/01', '24/01', '25/01', '18/02', '19/02', '20/02', '21/02', '22/02', '23/02', '20/03', '21/03', '22/03', '23/03', '24/03', '18/04', '19/04', '20/04', '21/04', '22/04', '23/04', '17/05', '18/05', '19/05', '20/05', '21/05', '22/05', '16/06', '17/06', '18/06', '19/06', '20/06', '15/07', '16/07', '17/07', '18/07', '19/07', '20/07', '13/08', '14/08', '15/08', '16/08', '17/08', '18/08', '19/08', '12/09', '13/09', '14/09', '15/09', '16/09', '17/09', '11/10', '12/10', '13/10', '14/10', '15/10', '16/10', '17/10', '10/11', '11/11', '12/11', '13/11', '14/11', '15/11', '16/11', '10/12', '11/12', '12/12', '13/12', '14/12', '15/12', '16/12') #wxg for Waxing Crescent
first=('26/01', '24/02', '25/03', '24/04', '23/05', '21/06', '21/07', '20/08', '18/09', '18/10', '17/11', '17/12') #first for first quarter
new=('18/01', '17/02', '19/03', '17/04', '16/05', '15/06', '14/07', '12/08', '11/09', '10/10', '09/11', '09/12') #new for new moon
full=('03/01', '01/02', '03/03', '02/04', '01/05', '31/05', '30/06', '29/07', '28/08', '26/09', '26/10', '24/11', '24/12') #full for full moon

if date in wxg:
    moon='waxing gibbous moon'
    fs=1 #fs for fact start
    fe=6 #fe for fact end
    ms=2 #ms for myth start
    me=6 #me for myth end
elif date in wng:
    moon='waning gibbous moon'
    fs=7
    fe=12
    ms=6
    me=12
elif date in third:
    moon='third quarter moon'
    fs=12
    fe=17
    ms=12
    me=18
elif date in wnc:
    moon='waning crescent moon'
    fs=17
    fe=23
    ms=18
    me=22
elif date in wxc:
    moon='waxing crescent moon'
    fs=23
    fe=28
    ms=22
    me=28
elif date in first:
    moon='first quarter moon'
    fs=28
    fe=33
    ms=28
    me=33
elif date in new:
    moon='new moon'
    fs=33
    fe=39
    ms=33
    me=37
elif date in full:
    moon='full moon'
    fs=39
    fe=46
    ms=37
    me=43
else:
    print(f'{date} is not a valid date. Try again!')

print(f'{date} is a {moon}!')

know=str(input(f'What would you like to know about the {moon}? (fact/mythology/nothing): '))

if know=='fact':
    with open('facts.txt', "r") as v: #v for variable
        facts= v.readlines()[fs:fe] #readlines() returns a list of lines from the stream rather than characters like read()
        response=[line.strip() for line in facts] #readlines() adds \n and other useless things so we remove them
        print(str(response).strip("[]").strip("''").replace(",", "").replace("'", ""))
        next=input(str('Would you still like to know about the mythology? (yes/no): '))
        if next=='yes':
            with open('myths.txt') as v:
                myths= v.readlines()[ms:me]
                response=[line.strip() for line in myths]
                print(str(response).strip("[]").strip("''").replace(",", "").replace("'", ""))
elif know=='mythology':
    with open('myths.txt') as v:
        myths= v.readlines()[ms:me]
        response=[line.strip() for line in myths]
        print(str(response).strip("[]").strip("''").replace(",", "").replace("'", ""))
        next=input(str('Would you still like to know about the facts? (yes/no): '))
        if next =='yes':
            with open('facts.txt') as v:
                facts= v.readlines()[fs:fe]
                response=[line.strip() for line in facts]
                print(str(response).strip("[]").strip("''").replace(",", "").replace("'", ""))
        else:
            print('Okay')
elif know=='nothing':
    response='Oh... okay :('
    print(response)
else:
    response=f'''"{know}" is an invalid answer.'''
    print(response)