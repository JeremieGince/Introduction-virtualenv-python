

if __name__ == '__main__':
    try:
        import pandas

        print(f"Pandas version: {pandas.__version__}")
    except ImportError:
        print('Pandas not installed')
