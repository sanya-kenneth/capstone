from app import create_app


APP = create_app("Development")

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
