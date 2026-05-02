# Bibliotecas necessárias: pip install pandas
import pandas as pd

def analisar_cenario_focus(dados):
    """
    Analisa os dados do Boletim Focus enviados pela Vitória 
    e gera recomendações estratégicas para a área de Supply Chain.
    """
    print("=" * 65)
    print("   RELATÓRIO DE INTELIGÊNCIA ECONÔMICA | VITÓRIA AMARAL")
    print("=" * 65)
    print("Data de Referência das Projeções: Abril/Maio de 2026\n")

    # Utilizando o Pandas para exibir um quadro resumo visualmente agradável
    df_resumo = pd.DataFrame(dados).T
    print("--- QUADRO RESUMO DAS PROJEÇÕES ---")
    print(df_resumo)
    print("\n" + "=" * 65 + "\n")

    for mes, valores in dados.items():
        print(f"🔹 ANÁLISE PARA {mes.upper()}:")
        cambio = valores['Cambio']
        selic = valores['Selic']
        ipca = valores['IPCA']
        igpm = valores['IGPM']
        
        print(f"  - Câmbio projetado: R$ {cambio:.2f}")
        print(f"  - Selic projetada:  {selic:.2f}%")
        print(f"  - IPCA (Inflação):  {ipca:.2f}%")
        print(f"  - IGP-M:            {igpm:.2f}%\n")

        print("  [INSIGHTS ESTRATÉGICOS]")
        
        # Lógica de Negócio Aplicada (O diferencial da Vitória)
        if cambio < 5.10:
            print("  💡 INSIGHT BUYING: Tendência de estabilidade/queda no câmbio. Bom momento para negociar contratos dolarizados ou antecipar importações.")
        else:
            print("  ⚠️ ALERTA BUYING: Câmbio pressionado (>= R$ 5,10). Avaliar hedge cambial com o time financeiro antes de fechar grandes lotes.")
            
        if selic > 13.00:
            print("  ⚠️ ATENÇÃO FINANCEIRA: Selic elevada aumenta o custo de capital. Evitar estoques excessivos parados e focar em giro rápido (Just-in-Time).")
            
        if igpm > 1.00:
            print("  ⚠️ ALERTA LOGÍSTICO: IGP-M mensal alto. Cuidado com o impacto em reajustes de aluguéis de galpões e contratos de longo prazo de frete.")

        print("-" * 65)

# Dados extraídos das imagens/planilhas (Mediana abr-mai/2026)
dados_focus_vitoria = {
    'Abril/2026': {
        'IPCA': 0.70,
        'Cambio': 5.05,
        'Selic': 14.50,
        'IGPM': 2.29
    },
    'Maio/2026': {
        'IPCA': 0.38,
        'Cambio': 5.10,
        'Selic': 14.25,
        'IGPM': 0.47
    }
}

if __name__ == "__main__":
    analisar_cenario_focus(dados_focus_vitoria)
