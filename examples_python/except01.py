"""Exception.

`<https://www.youtube.com/watch?v=LRudk3FQLoM>`_
"""
from uu import Error


def main():
    d = {
        'website': 'google',
    }

    try:
        # add code only with exception
        data = d['url']
    except KeyError as e:
        data = 'http://'
        print('Inside except', data)
        return data
    else:
        # add another code
        pass
    finally:
        print('From finally, after except KeyError')


if __name__ == '__main__':
    result = main()
    print(result)
