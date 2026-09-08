# data/processed/

Aqui ficam os dados **depois** de harmonizados — já com nomes de colunas padronizados entre os 3 anos, categorias recodificadas (G2 em binário, renda em `RENDA_FAMILIAR_2`, etc.) e os 3 anos concatenados num único arquivo por módulo.

## O que vai aparecer aqui (gerado pelo notebook de harmonização, não é para editar à mão)
- `domicilios_harmonizado.csv` — os 3 anos de Domicílios já juntos
- `individuos_harmonizado.csv` — os 3 anos de Indivíduos já juntos

## Sobre versionamento
Assim como os dados brutos, esses arquivos processados também tendem a ser grandes — avaliar se entram no `.gitignore` também, ou se sobem ao Git (depende do tamanho final depois da harmonização).
