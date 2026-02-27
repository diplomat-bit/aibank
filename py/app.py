
from flask import Flask
app = Flask(__name__)

@app.route('/')
def homepage():
    return '''
    <h1>Application Homepage</h1>
    <ul>
        <li><a href="/code_review">Automated Code Review</a></li>
        <li><a href="/documentation_generator">Documentation Generator</a></li>
        <li><a href="/codebase_monitoring">Codebase Health Monitoring</a></li>
        <li><a href="/code_search">Code Search Engine</a></li>
        <li><a href="/complexity_analysis">Code Complexity Analysis</a></li>
    </ul>
    '''

@app.route('/code_review')
def code_review():
    return '<h1>Automated Code Review</h1>'

@app.route('/documentation_generator')
def documentation_generator():
    return '<h1>Documentation Generator</h1>'

@app.route('/codebase_monitoring')
def codebase_monitoring():
    return '<h1>Codebase Health Monitoring</h1>'

@app.route('/code_search')
def code_search():
    return '<h1>Code Search Engine</h1>'

@app.route('/complexity_analysis')
def complexity_analysis():
    return '<h1>Code Complexity Analysis</h1>'

if __name__ == '__main__':
    app.run(debug=True)
