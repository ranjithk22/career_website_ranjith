from flask import Flask, render_template, jsonify

app = Flask(__name__)

jobs = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Hyderabad',
        'salary': 100000
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Bengalore'
    },
    {
        'id': 3,
        'title': 'Backend Developer',
        'location': 'Pune',
        'salary': 150000
    },
]


@app.route('/')
def index():
    return render_template('index.html', jobs=jobs)


@app.route('/api/jobs')
def get_jobs():
    return jsonify(jobs)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
