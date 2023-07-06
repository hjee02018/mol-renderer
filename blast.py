import subprocess
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def blast_search():
    # 1:POST요청만 처리
    if request.method == 'POST':
        sequence = request.form.get('sequence')
        result = run_blast_search(sequence)
        return render_template('main.html', blast_results=result)
    # 2:POST요청이 없거나 GET요청인 경우
    return render_template('main.html')
# BlastSearch 수행
def run_blast_search(sequence):
    with open('query.fasta', 'w') as file:
        file.write(f'>query\n{sequence}')
    subprocess.run(['blastp', '-query', 'query.fasta', '-db', 'blast_db', '-out', 'result.txt'])
    with open('result.txt', 'r') as file:
        lines = file.readlines()
        result = ''.join(lines[22:])
#        result = file.read()
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
