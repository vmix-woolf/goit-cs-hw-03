from colorama import Fore
from connection import connect_db


def execute_queries(connection, queries):
    cursor = connection.cursor()
    for query in queries:
        try:
            cursor.execute(query)
            results = cursor.fetchall()
            print(f"{Fore.RED}Results for the query: \n{Fore.YELLOW}{query}{Fore.RESET}" )
            for row in results:
                print(row)
            print("\n" + "-" * 40)
        except Exception as e:
            print(f"Query execution error: {e}")
    cursor.close()


def read_queries_from_file(filename):
    with open(filename, 'r') as file:
        queries = file.read().split(';')
        queries = [query.strip() for query in queries if query.strip()]
    return queries


def main():
    queries = read_queries_from_file('task01/queries.sql')
    connection = connect_db()
    if connection:
        execute_queries(connection, queries)
        connection.close()


if __name__ == "__main__":
    main()