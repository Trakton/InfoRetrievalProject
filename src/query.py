from ranker.ranker import Ranker

index = 'indexes/indexNot Shortened.json'
documents = 'indexes/name.csv'

ranker = Ranker(index)

print('Ranker connected to {}\n'.format(index))

while(True):
    print('Please, select one option below:\n')
    print('1 - Make structured query')
    print('2 - Make plain text query')
    print('0 - Exit\n')
    ans = input('Your choice: ')
    if(ans == '0'):
        break
    elif(ans == '1'):
        print('\n-- New Query --')
        title = input('Title: ')
        statement = input('Statement: ')
        rank = ranker.getStructuredRank(title, statement)
        print(rank)
    elif(ans == '2'):
        print('\n-- New Query --')
        print('b')