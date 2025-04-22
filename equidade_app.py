from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dados de exemplo atualizados
mentores = [
    {'id': 1, 'nome': 'Ana Silva', 'area': 'Tecnologia', 'genero': 'Feminino', 'temas': ['Liderança Feminina', 'Carreira em TI']},
    {'id': 2, 'nome': 'Pedro Oliveira', 'area': 'Marketing', 'genero': 'Masculino', 'temas': ['Marketing Digital', 'Estratégia de Marca']},
    {'id': 3, 'nome': 'Laura Santos', 'area': 'Ciências Sociais', 'genero': 'Não Binário', 'temas': ['Inclusão LGBTQIA+', 'Estudos de Gênero']},
    {'id': 4, 'nome': 'Mariana Souza', 'area': 'Recursos Humanos', 'genero': 'Feminino', 'temas': ['Diversidade e Inclusão', 'Recrutamento Sem Viés']},
    {'id': 5, 'nome': 'Carlos Pereira', 'area': 'Empreendedorismo', 'genero': 'Masculino', 'temas': ['Financiamento para Mulheres', 'Crescimento de Startups']},
    {'id': 6, 'nome': 'Sofia Almeida', 'area': 'Artes', 'genero': 'Não Binário', 'temas': ['Representatividade na Mídia', 'Expressão de Gênero na Arte']}
]

@app.route('/')
def index():
    return render_template('index.html', mentores=mentores)

@app.route('/mentor/<int:mentor_id>')
def perfil_mentor(mentor_id):
    mentor = next((m for m in mentores if m['id'] == mentor_id), None)
    if mentor:
        return render_template('perfil_mentor.html', mentor=mentor)
    return "Mentor não encontrado"

@app.route('/buscar', methods=['GET', 'POST'])
def buscar_mentores():
    resultados = []
    termo = ""
    area_busca = request.form.get('area', '').lower()
    tema_busca = request.form.get('tema', '').lower()
    genero_busca = request.form.get('genero', '')

    if request.method == 'POST':
        termo = f"Área: {area_busca}, Tema: {tema_busca}, Gênero: {genero_busca if genero_busca else 'Qualquer'}"
        resultados = [
            m for m in mentores
            if (area_busca in m['area'].lower() if area_busca else True) and
               (tema_busca in ', '.join(m['temas']).lower() if m.get('temas') and tema_busca else True) and
               (m['genero'] == genero_busca if genero_busca else True)
        ]
        return render_template('resultados_busca.html', resultados=resultados, termo=termo)
    return render_template('buscar.html')

@app.route('/informativos')
def informativos():
    return render_template('informativos.html')

@app.route('/informativo/o-que-e-discriminacao')
def o_que_e_discriminacao():
    return render_template('o-que-e-discriminacao.html')

@app.route('/informativo/impacto-no-trabalho')
def impacto_no_trabalho():
    return render_template('impacto-no-trabalho.html')

@app.route('/informativo/legislacao')
def legislacao():
    return render_template('legislacao.html')

if __name__ == '__main__':
    app.run(debug=True)