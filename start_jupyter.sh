#!/bin/bash

IMAGE_NAME="quay.io/jupyter/datascience-notebook"
CONTAINER_NAME="jupyter-datascience" # Nome opcional para o seu container

echo "Verificando se a imagem Docker '$IMAGE_NAME' existe localmente..."

# Verifica se a imagem já está baixada
if docker images --format "{{.Repository}}:{{.Tag}}" | grep -q "$IMAGE_NAME"; then
    echo "Imagem '$IMAGE_NAME' já existe localmente."
else
    echo "Imagem '$IMAGE_NAME' não encontrada. Baixando..."
    docker pull "$IMAGE_NAME"
    if [ $? -ne 0 ]; then
        echo "Erro ao baixar a imagem Docker. Saindo."
        exit 1
    fi
    echo "Download da imagem concluído."
fi

# Verifica se o container já está rodando
if docker ps -a --format "{{.Names}}" | grep -q "$CONTAINER_NAME"; then
    echo "Container '$CONTAINER_NAME' já existe. Tentando iniciar/reiniciar..."
    docker start "$CONTAINER_NAME"
    if [ $? -ne 0 ]; then
        echo "Erro ao iniciar o container existente. Tentando remover e criar um novo."
        docker rm -f "$CONTAINER_NAME"
        # Cria um novo container se o existente falhou ao iniciar
        docker run -p 8888:8888 \
                   -v "${PWD}:/home/jovyan/work" \
                   --user "$(id -u):$(id -g)" \
                   --name "$CONTAINER_NAME" \
                   "$IMAGE_NAME"
    fi
else
    echo "Container '$CONTAINER_NAME' não encontrado. Criando e iniciando um novo..."
    docker run -p 8888:8888 \
               -v "${PWD}:/home/jovyan/work" \
               --user "$(id -u):$(id -g)" \
               --name "$CONTAINER_NAME" \
               "$IMAGE_NAME"
fi

echo "Jupyter Notebook/Lab iniciado no container '$CONTAINER_NAME'."
echo "Aguarde a saída do Jupyter para obter o token de acesso no seu navegador (geralmente em http://127.0.0.1:8888)."

# Opcional: Anexar ao log do container para ver a URL do Jupyter
docker logs -f "$CONTAINER_NAME"