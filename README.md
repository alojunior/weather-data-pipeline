# Weather Data Pipeline

Pipeline ETL profissional para coleta, transformação e armazenamento de dados climáticos usando Python e Open-Meteo API.

## Objetivo

Demonstrar habilidades em:
- Arquitetura orientada a objetos (OOP)
- Padrões de design (Design Patterns)
- Engenharia de dados (ETL)
- Desenvolvimento CLI profissional

## Tecnologias

- **Python 3.11+**
- **Pandas** - Manipulação de dados
- **Typer** - Interface CLI moderna
- **Rich** - Output formatado no terminal
- **Poetry** - Gerenciamento de dependências
- **Open-Meteo API** - Fonte de dados climáticos

## Instalação
```bash
# Clone o repositório
git clone https://github.com/alojunior/weather-data-pipeline.git
cd weather-data-pipeline

# Instale as dependências
poetry install
```

## Uso
```bash
# Executar pipeline com configurações padrão
poetry run python -m datapipeline.cli pipeline

# Modo verbose (detalhes de progresso)
poetry run python -m datapipeline.cli pipeline --verbose

# Modo debug (dados brutos)
poetry run python -m datapipeline.cli pipeline --debug

# Ambos
poetry run python -m datapipeline.cli pipeline --debug --verbose
```

## Arquitetura

O projeto segue o padrão ETL (Extract, Transform, Load) com design orientado a objetos:
```
Extract (OpenMeteoSource) → Transform (BasicTransform) → Load (CSVSink)
```

### Componentes Principais

- **Source**: Interface abstrata para extração de dados
- **Transformer**: Interface abstrata para transformações
- **Sink**: Interface abstrata para persistência
- **DataPipeline**: Orquestrador que conecta os componentes
- **PipelineConfig**: Gerenciamento centralizado de configurações

## Estrutura do Projeto
```
weather-data-pipeline/
├── src/
│   └── datapipeline/
│       ├── core/          # Interfaces e lógica central
│       ├── sources/       # Fontes de dados
│       ├── processing/    # Transformações
│       └── storage/       # Sinks (persistência)
├── output/               # Dados processados (CSV)
├── pyproject.toml       # Dependências
└── README.md
```

## Roadmap

- [x] Pipeline ETL básico com CSV
- [x] CLI com Typer
- [x] Logging (debug/verbose)
- [ ] PostgreSQL como destino
- [ ] Docker + Docker Compose
- [ ] Testes automatizados
- [ ] CI/CD

## Licença

MIT

## Autor

**André Luis de Oliveira Junior**
- LinkedIn: [linkedin.com/in/alojunior](https://linkedin.com/in/alojunior)
- GitHub: [github.com/alojunior](https://github.com/alojunior)