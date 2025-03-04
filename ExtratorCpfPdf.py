import fitz # PyMuPDF
import re

def extract_info_from_pdf(pdf_path):
    """Extrai informações específicas de um PDF."""
    with fitz.open(pdf_path) as doc:
        text = "\n".join([page.get_text("text") for page in doc])
        
        # Expressões regulares para encontrar os campos desejados
        processo_regex = r"Processo nº:\s*([\d\.\-/]+)"
        credor_regex = r"Credor\(s\):\s*([\w\s]+)"
        cpf_regex = r"CPF/CNPJ/RNE:\s*([\d\.\-]+)"
        
        # Busca os campos no texto
        processo_match = re.search(processo_regex, text)
        credor_match = re.search(credor_regex, text)
        cpf_match = re.search(cpf_regex, text)
        
        # Retorna os valores encontrados
        processo = processo_match.group(1) if processo_match else "Não encontrado"
        credor = credor_match.group(1).strip() if credor_match else "Não encontrado"
        cpf = cpf_match.group(1) if cpf_match else "Não encontrado"
        
        return processo, credor, cpf

def main():
    # Lista de caminhos dos PDFs (substitua pelos caminhos reais dos seus arquivos)
    pdf_paths = [
        r"C:\Users\admin\Documents\avila cred\Feito\doc_271227361.pdf",
        r"C:\Users\admin\Documents\avila cred\Feito\doc_274459962.pdf",
        r"C:\Users\admin\Documents\avila cred\Feito\doc_274461299.pdf",
        r"C:\Users\admin\Documents\avila cred\Feito\doc_274462516.pdf",
        r"C:\Users\admin\Documents\avila cred\Feito\doc_274463211.pdf"
    ]
    
    # Cria uma lista para armazenar os resultados
    resultados = []
    
    # Processa cada PDF
    for pdf_path in pdf_paths:
        processo, credor, cpf = extract_info_from_pdf(pdf_path)
        resultados.append((processo, credor, cpf))
    
    # Exibe os resultados em formato de tabela
    print("{:<30} {:<30} {:<15}".format("Processo nº", "Credor(s)", "CPF/CNPJ/RNE"))
    print("-" * 75)
    for resultado in resultados:
        print("{:<30} {:<30} {:<15}".format(resultado[0], resultado[1], resultado[2]))

if __name__ == "__main__":
    main()
