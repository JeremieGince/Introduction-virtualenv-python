
if __name__ == '__main__':
    try:
        import sklearn

        print(f"Scikit-learn version: {sklearn.__version__}")
    except ImportError:
        print('Scikit-learn not installed')
