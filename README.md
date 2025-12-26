# Directory Inspector JSON

*Portuguese/English*

## Português

Um utilitário simples em Python para listar arquivos e diretórios de um caminho específico e retornar essas informações em um formato JSON compatível.
É recomendado criar um arquivo em seu projeto e importar a função desejada como um componente (sinta-se livre para personalizar o algoritmo para suas necessidades).

O script identifica:
- Arquivos (nome e extensão)
- Diretórios (nome)

Por padrão, o exemplo incluído lista o conteúdo do diretório atual.

### Funcionalidades

- Detecta automaticamente o diretório de execução
- Lista arquivos e pastas utilizando `pathlib`
- Retorna os dados em uma estrutura JSON organizada
- Código simples, legível e fácil de manter ou expandir

### Requisitos

- Python 3.9 ou superior

Bibliotecas utilizadas:
- pathlib (biblioteca padrão)
- json (biblioteca padrão)

### Como usar

1. Clone o repositório:

```bash
git clone https://github.com/Dum2601/directory-inspector-json.git
````

2. Execute o script:

```bash
python main.py
```

3. O resultado será exibido no terminal em formato JSON, contendo os arquivos e diretórios do caminho analisado.

### Exemplo de saída

```json
[
    {
        "type": "file",
        "name": "example",
        "extension": ".py"
    },
    {
        "type": "directory",
        "name": "src"
    }
]
```

---

## English

A simple Python utility to list files and directories from a given path and return this information in a JSON-compatible format.
It's recommended create a file in your project and import the function in desired file as a component (feel free for personalize the algorithm for your case/use).

The script identifies:

* Files (name and extension)
* Directories (name)

By default, the provided example lists the contents of the current working directory.

### Features

* Automatically detects the current working directory
* Lists files and folders using `pathlib`
* Outputs data in a clean and structured JSON format
* Simple, readable and easy-to-extend codebase

### Requirements

* Python 3.9 or higher

Libraries used:

* pathlib (standard library)
* json (standard library)

### How to use

1. Clone the repository:

```bash
git clone https://github.com/Dum2601/directory-inspector-json.git
```

2. Run the script:

```bash
python main.py
```

3. The output will be printed to the terminal in JSON format, showing the files and directories from the analysed path.

### Output example

```json
[
    {
        "type": "file",
        "name": "example",
        "extension": ".py"
    },
    {
        "type": "directory",
        "name": "src"
    }
]
```

---

## Project structure

```text
.
├── main.py
└── README.md
```

---

## Licence

This project is licensed under the MIT Licence.
See the LICENSE file for more information.

```
