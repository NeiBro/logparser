from collections import Counter
import re

pattern = (
    r'(?P<ip>\d+\.\d+\.\d+\.\d+)'
    r'.* \[(?P<datetime>[^\]]+)\]'
    r' "(?P<method>[A-Z]+) (?P<resource>[^\s]+) (?P<http_version>HTTP/\d\.\d)" '
    r'(?P<status_code>\d+) (?P<size>\d+) "(?P<user_agent>[^"]+)"'
)

def display_menu():
    print('Which statistic you want to perform?')
    print('1. IP')
    print('2. HTTP Method')
    print('3. Datetime')

def get_answer():
    while True:
        try:
            statistic_answer = int(input())
            if 1 <= statistic_answer <= 3:
                return statistic_answer
            else:
                print('Please enter number between 1 and 3.')
        except ValueError:
            print('Please enter valid number.')

def count_ip(entry_log):
    ip_list = []
    with open(entry_log, 'r', encoding='utf-8') as data:
        for line in data:
            match = re.match(pattern, line)
            if match:
                ip_list.append(match.groupdict()['ip'])
        ip_counter = Counter(ip_list)
        return ip_counter.most_common()

def count_method(entry_log):
    method_list = []
    with open(entry_log, 'r', encoding='utf-8') as data:
        for line in data:
            match = re.match(pattern, line)
            if match:
                method_list.append(match.groupdict()['method'])
        method_counter = Counter(method_list)
        return method_counter
def count_datetime(entry_log):
    datetime_list = []
    with open(entry_log, 'r', encoding='utf-8') as data:
        for line in data:
            match = re.match(pattern, line)
            if match:
                datetime_list.append(match.groupdict()['datetime'])
        datetime_counter = Counter(datetime_list)
        return datetime_counter
    
def statistic():
    display_menu()
    statistic_answer = get_answer()
    if statistic_answer == 1:
        ip_statistic = count_ip(entry_log='access.log')
        print(ip_statistic)
    if statistic_answer == 2:
        method_statistic = count_method(entry_log='access.log')
        print(method_statistic)
    if statistic_answer == 3:
        datetime_statistic = count_datetime(entry_log='access.log')
        print(datetime_statistic)

if __name__ == '__main__':
    statistic()