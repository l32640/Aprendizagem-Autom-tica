import dist_euclidiana

def print_hi(name):
    
    print(f'Hello, {name}')  


if __name__ == '__main__':

    print_hi('Python')
    
    x = [1.2, 2, 3.8, 4.5]
    y = [0.5, 4.5, 9.6, 3.4]
    print(dist_euclidiana.dist_euclidiana_np(x, y))
