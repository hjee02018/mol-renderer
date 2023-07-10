import subprocess
from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/<sequence>')
def viewer1(sequence):
    pdb_id = sequence.replace('|', '.')
    pdb_filename = f'{pdb_id.upper()}.pdb'
    pdb_url = url_for('static', filename='pdbs/' + pdb_filename)
    return render_template('complex.html', data_href=pdb_url)

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
        result = ''.join(lines[27:])
        start_line = 29
        end_line = start_line
        for i, line in enumerate(lines[start_line:], start=start_line):
            if line.strip() == "":
                end_line = i
                break
        table_lines = lines[start_line:end_line]
        remaining_lines = lines[end_line:]
        result = {
            'table_lines': table_lines,
            'remaining_lines': remaining_lines
        }

#        result = file.read()
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
