seconds = int(input('Enter number of seconds: '))

h_time = seconds // 3600
seconds = seconds % 3600
m_time = seconds // 60
seconds = seconds % 60

print(f'{h_time:02}:{m_time:02}:{seconds:02}')
