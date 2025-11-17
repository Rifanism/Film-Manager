from FilmDB import filmDB

database = filmDB('database\\films.db')


def byRating(db, asc=-1):
    keys = list(db.keys())

    def getValue(key):
        return (asc * float(db[key]['rating']))
    
    def partition(low, high):
        pivotKey = keys[high]
        pivotValue = getValue(pivotKey)

        i = low - 1

        for j in range(low, high):
            currentValue = getValue(keys[j])
            if currentValue < pivotValue:
                i = i + 1
                keys[i], keys[j] = keys[j], keys[i]
        
        keys[i + 1], keys[high] = keys[high], keys[i + 1]
        return i + 1
    
    def recursive(low, high):
        if low < high:
            pivot = partition(low, high)
            recursive(low, pivot - 1)
            recursive(pivot + 1, high)
        
    size = len(keys)
    recursive(0, size - 1)
    return keys

def byTitle(db, reverse=False):
    films = sorted(
        db.keys(),
        key=lambda title: (db[title]['title']),
        reverse=reverse
    )
    for i, title in enumerate(films):
        print(i+1, title)


if __name__ == '__main__':
    sorts = byRating(database)

    for i, title in enumerate(sorts):
        print(f'{i+1}. {title} | {database[title]['rating']}')