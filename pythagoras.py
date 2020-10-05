import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Dictionary',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    args = parser.parse_args()
    return args

def main():
    args = get_args()
    C = [39.2,36.5,37.5,0]
    F = [((float(9)/5)*c + 32)for c in C]
    print(F)
    #Pythagorean triples a^2 + b^2 = c^2
    P = []
    for a in range(1,30):
        for b in range(a,30):
            for c in range(b,30):
               if (a**2 + b**2)==c**2:
                   t=(a,b,c)
                   P.append(t)
    print(P)
    q = [(a,b,c) for a in range(1,30) for b in range(a,30) for c in range(b,30) if (a**2 + b**2)==c**2]
    print(q)
    colors = {"r","g","b","y"}
    things = {"house","car","tree"}
    print(' '.join([c + ',' + t for c in colors for t in things]))

if __name__ == '__main__':
    main()