from datetime import date
from pathlib import Path
from weasyprint import HTML


def gerar_relatorio(
    caminho_saida: str = "Relatorio_Executivo_Triagem_IA.pdf",
    repositorio: str = "github.com/MathGuerra/analisador-atendimento",
    data_geracao: str | None = None,
) -> str:
    """Lê o template HTML/CSS separado, injeta os metadados e gera o relatório PDF corporativo."""
    
    data_geracao = data_geracao or date.today().strftime("%d/%m/%Y")
    
    # Leitura do arquivo de template
    template_path = Path("template.html")
    if not template_path.exists():
        raise FileNotFoundError("O arquivo 'template.html' não foi encontrado no diretório atual.")
        
    template = template_path.read_text(encoding="utf8")
    
    # Substituição das variáveis dinâmicas no HTML
    html_processado = template.format(
        data_geracao=data_geracao,
        repositorio=repositorio
    )
    
    # Geração do PDF carregando automaticamente os estilos externos (styles.css)
    HTML(string=html_processado, base_url=".").write_pdf(caminho_saida)
    return caminho_saida


if __name__ == "__main__":
    caminho = gerar_relatorio()
    print(f"Relatório Corporativo gerado com sucesso! -> {caminho}")