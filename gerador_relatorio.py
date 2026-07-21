from datetime import date
from pathlib import Path
from xhtml2pdf import pisa


def gerar_relatorio(
    caminho_saida: str = "Relatorio_Executivo_Triagem_IA.pdf",
    repositorio: str = "github.com/MathGuerra/analisador-atendimento",
    data_geracao: str | None = None,
) -> str:
    """Lê o template HTML/CSS, injeta os metadados e gera o relatório PDF compatível com Windows."""
    
    data_geracao = data_geracao or date.today().strftime("%d/%m/%Y")
    
    template_path = Path("template.html")
    if not template_path.exists():
        raise FileNotFoundError("O arquivo 'template.html' não foi encontrado.")
        
    template = template_path.read_text(encoding="utf8")
    
    # Injetando as variáveis no template
    html_processado = template.format(
        data_geracao=data_geracao,
        repositorio=repositorio
    )
    
    # Convertendo HTML para PDF com xhtml2pdf
    with open(caminho_saida, "wb") as arquivo_pdf:
        pisa_status = pisa.CreatePDF(
            src=html_processado,
            dest=arquivo_pdf,
            encoding="utf-8"
        )
        
    if pisa_status.err:
        raise Exception(f"Erro ao gerar o PDF: {pisa_status.err}")
        
    return caminho_saida


if __name__ == "__main__":
    caminho = gerar_relatorio()
    print(f"Relatório Corporativo gerado com sucesso! -> {caminho}")