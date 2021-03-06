# Criando o primeiro aplicativo

import sys

# Iniciando a sessão do spark
from pyspark.sql import SparkSession

# Importando as funções (para calcular o ano)
from pyspark.sql.functions import * 

# Criando o módulo
if __name__ == "__main__":
	spark = SparkSession.builder.appName("Exemplo").getOrCreate()
	arqschema = "id INT, nome STRING, status STRING, cidade STRING, vendas INT, data STRING"
	despachante = spark.csv(sys.argv[1], header=False, schema = arqschema)
	# Calculando as vendas por ano
	calculo = despachantes.select("data").groupBy(year("data")).count()
	calculo.write.format("console").save()
	spark.stop()
	
	
# Chamando o arquivo no terminal: spark-submit aplicativo2.py /home/bruno/download/despachantes.csv
