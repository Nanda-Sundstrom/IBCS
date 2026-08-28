s=int(input('Give systolic blood pressure: '))
d=int(input('Give diastolic blood pressure: '))
print(f'systolic blood pressure is {'normal' if s<120 else 'abnormal'}')
print(f'diastolic blood pressure is {'normal' if d<80 else 'abnormal'}')