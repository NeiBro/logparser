import re
import csv

search_field = {
    1: 'ip',
    2: 'datetime',
    3: 'method',
    4: 'resource',
    5: 'http_version',
    6: 'status_code',
    7: 'size',
    8: 'user_agent'
}

pattern = (
    r'(?P<ip>\d+\.\d+\.\d+\.\d+)'
    r'.* \[(?P<datetime>[^\]]+)\]'
    r' "(?P<method>[A-Z]+) (?P<resource>[^\s]+) (?P<http_version>HTTP/\d\.\d)" '
    r'(?P<status_code>\d+) (?P<size>\d+) "(?P<user_agent>[^"]+)"'
)

def display_menu():
    print('What parameter do you want to use to perform the search?')
    print('1. IP-adress')
    print('2. Date')
    print('3. Http method')
    print('4. Resource')
    print('5. Http Version')
    print('6. Status Code')
    print('7. Size')
    print('8. User-Agent')


def search_via_method(search_method):
     search_value = input('Enter the value for search: ')
     matches = []
     matches_count = 0
     
     try:
         with open('access.log', encoding='utf-8') as data:
            for dataline in data:
                match = re.match(pattern, dataline)
                if not match:
                    continue

                if match.group(search_field.get(search_method)) == search_value:
                    matches_count += 1
                    matches.append(match.groupdict())
                    print('IP-address:', match.group('ip'))
                    print('Date -', match.group('datetime'))
                    print('Http method -', match.group('method'))
                    print('Resource -', match.group('resource'))
                    print('Http Version -', match.group('http_version'))
                    print('Status Code -', match.group('status_code'))
                    print('Size -', match.group('size'))
                    print('User-Agent -', match.group('user_agent'))
            print(f'Found {matches_count} match(es)')
            
            if matches_count > 0:
                answer_csv = input('Save to csv file? (Y/N): ').lower()
                if answer_csv in ['y', 'yes']:
                    csv_filename = input('Name of the file?: ')
                    csv_filename = csv_filename + '.csv'
                    try:
                        with open(csv_filename, 'w', encoding='utf-8', newline='') as csvfile:
                            fieldnames = ['IP', 'Date', 'Method', 'Resource', 'HTTP_Version', 'Status_Code', 'Size', 'User_Agent']
                            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';', quoting=csv.QUOTE_ALL)
                            writer.writeheader()
                            
                            # Записываем каждое совпадение
                            for match in matches:
                                writer.writerow({
                                    'IP': match['ip'],
                                    'Date': match['datetime'],
                                    'Method': match['method'],
                                    'Resource': match['resource'],
                                    'HTTP_Version': match['http_version'],
                                    'Status_Code': match['status_code'],
                                    'Size': match['size'],
                                    'User_Agent': match['user_agent']
                                })
                        print(f'Data successfully saved to {csv_filename}')
                    except IOError as e:
                        print(f'Error saving to CSV file: {e}')
                    except Exception as e:
                        print(f'Unexpected error while saving: {e}')
     except FileNotFoundError:
         print("Файл access.log не найден")
         return

def get_search_method():
    while True:
        try:
            search_method = int(input('Enter your choice: '))
            if 1 <= search_method <= 8:
                return search_method
            else:
                print('Please enter number between 1 and 8.')
        except ValueError:
                print('Please enter valid number.')

def search():
    display_menu()
    search_method = get_search_method()
    search_via_method(search_method)

if __name__ == '__main__':
    search()